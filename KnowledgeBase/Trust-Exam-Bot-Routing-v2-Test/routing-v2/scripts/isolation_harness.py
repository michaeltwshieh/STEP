#!/usr/bin/env python3
"""Reproducible filesystem-isolated answer/evaluator harness.

Answer inputs are copied into a candidate-specific read-only tree.  On macOS, answer
commands run under ``sandbox-exec`` with content reads limited to that tree and writes
limited to the candidate's output directory.  The manifest-mediated read API records
every requested path; an out-of-manifest request is a hard isolation failure.

Gold, KAP, prior answers and peer output can be supplied only when evaluator inputs are
created after every answer output hash has been locked.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
HARNESS_VERSION = "routing-isolation-harness-v1"
CANDIDATE_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]*$")
ANSWER_FORBIDDEN_CATEGORIES = ("gold", "kap", "prior_answer", "peer_output")
SANDBOX_PYTHON = Path("/Library/Developer/CommandLineTools/usr/bin/python3")
if not SANDBOX_PYTHON.is_file():
    SANDBOX_PYTHON = Path("/usr/bin/python3")


class HarnessError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    path.write_text(rendered, encoding="utf-8")


def safe_candidate(candidate_id: str) -> str:
    if not CANDIDATE_PATTERN.fullmatch(candidate_id):
        raise HarnessError(f"invalid candidate id: {candidate_id!r}")
    return candidate_id


def safe_virtual_path(value: str) -> str:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts:
        raise HarnessError(f"unsafe virtual path: {value!r}")
    return path.as_posix()


def ensure_within(path: Path, root: Path) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as error:
        raise HarnessError(f"source lies outside workspace root: {path}") from error
    if not resolved.is_file() or resolved.is_symlink():
        raise HarnessError(f"source must be a regular non-symlink file: {path}")
    return resolved


def run_paths(run_dir: Path, candidate_id: str) -> dict[str, Path]:
    candidate_id = safe_candidate(candidate_id)
    return {
        "input": run_dir / "answer-inputs" / candidate_id,
        "opened": run_dir / "opened-inputs" / candidate_id,
        "output": run_dir / "answer-outputs" / candidate_id,
        "manifest": run_dir / "manifests" / f"{candidate_id}.json",
        "events": run_dir / "events" / f"{candidate_id}.json",
        "sandbox": run_dir / "sandbox" / f"{candidate_id}.sb",
        "staged": run_dir / "staged-outputs" / f"{candidate_id}.json",
    }


def sandbox_quote(path: Path) -> str:
    value = str(path.resolve())
    if any(ord(character) < 32 or ord(character) == 127 for character in value):
        raise HarnessError(f"sandbox path contains a control character: {value!r}")
    return value.replace("\\", "\\\\").replace('"', '\\"')


def sandbox_profile(input_root: Path, output_root: Path) -> str:
    """Create a narrow macOS Seatbelt profile for answer commands."""

    return f'''(version 1)
(deny default)
(allow process*)
(allow signal (target self))
(allow sysctl-read)
(allow mach-lookup)
(allow file-read-metadata)
(allow file-read-data
    (literal "/")
    (subpath "/usr")
    (subpath "/bin")
    (subpath "/sbin")
    (subpath "/Library/Developer/CommandLineTools")
    (subpath "/System/Volumes/Preboot/Cryptexes/OS")
    (subpath "/private/var/db")
    (subpath "/dev")
    (literal "{sandbox_quote(Path.home() / '.CFUserTextEncoding')}")
    (subpath "{sandbox_quote(input_root)}")
    (subpath "{sandbox_quote(output_root)}"))
(allow file-write*
    (subpath "{sandbox_quote(output_root)}")
    (literal "/dev/null"))
(allow file-write-data (literal "/dev/dtracehelper"))
(allow file-ioctl (literal "/dev/dtracehelper"))
(allow ipc-posix-shm-read-data)
'''


def make_read_only_tree(root: Path) -> None:
    for path in sorted(root.rglob("*"), key=lambda item: len(item.parts), reverse=True):
        if path.is_symlink():
            raise HarnessError(f"symlink found in isolated input tree: {path}")
        if path.is_file():
            path.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        elif path.is_dir():
            path.chmod(stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
    root.chmod(stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)


def prepare_answer_inputs(
    run_dir: Path,
    workspace_root: Path,
    candidate_id: str,
    question: Path,
    workflow_files: Iterable[Path],
    course_files: Iterable[Path],
) -> dict[str, Any]:
    paths = run_paths(run_dir, candidate_id)
    workflow_files = list(workflow_files)
    course_files = list(course_files)
    if (run_dir / "answer-lock.json").exists():
        raise HarnessError("answer hashes are already locked")
    if paths["input"].exists() or paths["manifest"].exists():
        raise HarnessError(f"candidate input already prepared: {candidate_id}")

    paths["input"].mkdir(parents=True)
    paths["output"].mkdir(parents=True)
    entries: list[dict[str, str]] = []
    seen_virtual: set[str] = set()

    sources: list[tuple[str, Path]] = [("question", question)]
    sources.extend(("workflow", item) for item in workflow_files)
    sources.extend(("course", item) for item in course_files)
    if not sources or not workflow_files or not course_files:
        raise HarnessError("question, selected workflow and at least one course file are required")

    for category, source in sources:
        resolved = ensure_within(source, workspace_root)
        virtual = safe_virtual_path(f"{category}/{resolved.name}")
        if virtual in seen_virtual:
            raise HarnessError(f"duplicate isolated virtual path: {virtual}")
        seen_virtual.add(virtual)
        destination = paths["input"] / virtual
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(resolved, destination)
        entries.append({
            "virtual_path": virtual,
            "category": category,
            "sha256": sha256(destination),
        })

    manifest = {
        "harness_version": HARNESS_VERSION,
        "candidate_id": candidate_id,
        "input_tree": f"answer-inputs/{candidate_id}",
        "forbidden_categories": list(ANSWER_FORBIDDEN_CATEGORIES),
        "files": sorted(entries, key=lambda item: item["virtual_path"]),
    }
    write_json(paths["manifest"], manifest)
    write_json(paths["input"] / "manifest.json", manifest)
    write_json(paths["events"], {"candidate_id": candidate_id, "events": []})
    paths["sandbox"].parent.mkdir(parents=True, exist_ok=True)
    paths["sandbox"].write_text(sandbox_profile(paths["opened"], paths["output"]), encoding="utf-8")
    make_read_only_tree(paths["input"])
    return manifest


def load_manifest(run_dir: Path, candidate_id: str) -> tuple[dict[str, Any], dict[str, Path]]:
    paths = run_paths(run_dir, candidate_id)
    try:
        manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise HarnessError(f"candidate manifest unavailable: {candidate_id}") from error
    return manifest, paths


def append_event(paths: dict[str, Path], event: dict[str, Any]) -> None:
    try:
        ledger = json.loads(paths["events"].read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise HarnessError("event ledger unavailable") from error
    event = {"sequence": len(ledger["events"]) + 1, **event}
    ledger["events"].append(event)
    write_json(paths["events"], ledger)


def request_open(run_dir: Path, candidate_id: str, requested_path: str) -> bytes:
    manifest, paths = load_manifest(run_dir, candidate_id)
    try:
        virtual = safe_virtual_path(requested_path)
    except HarnessError:
        append_event(paths, {
            "type": "hard_isolation_failure",
            "requested_path": requested_path,
            "permitted": False,
            "reason": "unsafe_or_absolute_path",
        })
        raise
    by_path = {item["virtual_path"]: item for item in manifest["files"]}
    if virtual not in by_path:
        append_event(paths, {
            "type": "hard_isolation_failure",
            "requested_path": virtual,
            "permitted": False,
            "reason": "outside_manifest",
        })
        raise HarnessError(f"requested path is outside manifest: {virtual}")
    if (paths["opened"] / "manifest.json").exists():
        raise HarnessError("opened-input tree is already frozen for answer execution")
    content = (paths["input"] / virtual).read_bytes()
    observed_hash = hashlib.sha256(content).hexdigest()
    if observed_hash != by_path[virtual]["sha256"]:
        append_event(paths, {
            "type": "hard_isolation_failure",
            "requested_path": virtual,
            "permitted": False,
            "reason": "input_hash_mismatch",
        })
        raise HarnessError(f"isolated input hash changed: {virtual}")
    opened_path = paths["opened"] / virtual
    opened_path.parent.mkdir(parents=True, exist_ok=True)
    opened_path.write_bytes(content)
    append_event(paths, {
        "type": "actual_open",
        "requested_path": virtual,
        "permitted": True,
        "sha256": observed_hash,
    })
    return content


def finalize_opened_tree(manifest: dict[str, Any], paths: dict[str, Path]) -> None:
    opened_manifest_path = paths["opened"] / "manifest.json"
    if opened_manifest_path.exists():
        return
    paths["opened"].mkdir(parents=True, exist_ok=True)
    opened_files = []
    for item in manifest["files"]:
        opened_path = paths["opened"] / item["virtual_path"]
        if opened_path.is_file():
            opened_files.append(item)
    opened_manifest = {
        **manifest,
        "input_tree": f"opened-inputs/{manifest['candidate_id']}",
        "files": opened_files,
    }
    write_json(opened_manifest_path, opened_manifest)
    make_read_only_tree(paths["opened"])


def sandbox_denials(process_id: int) -> list[dict[str, str]]:
    predicate = (
        'eventMessage CONTAINS[c] "Sandbox:" AND '
        f'eventMessage CONTAINS[c] "({process_id})" AND '
        'eventMessage CONTAINS[c] "deny("'
    )
    completed = subprocess.run(
        ["/usr/bin/log", "show", "--last", "1m", "--style", "compact", "--predicate", predicate],
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise HarnessError("cannot audit macOS sandbox denial log")
    denials: list[dict[str, str]] = []
    pattern = re.compile(r"deny\(\d+\)\s+(?P<operation>\S+)\s+(?P<path>.+?)\s*$")
    for line in completed.stdout.splitlines():
        if "Sandbox:" not in line or "deny(" not in line:
            continue
        match = pattern.search(line)
        if match:
            denials.append({
                "operation": match.group("operation"),
                "path": match.group("path"),
            })
    return sorted(
        {json.dumps(item, sort_keys=True): item for item in denials}.values(),
        key=lambda item: (item["path"], item["operation"]),
    )


def sandbox_command(
    paths: dict[str, Path],
    command: list[str],
) -> tuple[subprocess.CompletedProcess[str], list[dict[str, str]]]:
    sandbox_binary = shutil.which("sandbox-exec")
    if sandbox_binary is None:
        raise HarnessError("sandbox-exec is required for hard filesystem isolation")
    if not command:
        raise HarnessError("answer command is empty")
    manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    finalize_opened_tree(manifest, paths)
    temporary_root = paths["output"] / "tmp"
    temporary_root.mkdir(exist_ok=True)
    environment = {
        "PATH": "/usr/bin:/bin:/usr/sbin:/sbin",
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "ROUTING_INPUT_ROOT": str(paths["opened"].resolve()),
        "ROUTING_OUTPUT_ROOT": str(paths["output"].resolve()),
        "ROUTING_MANIFEST": str((paths["opened"] / "manifest.json").resolve()),
        "TMPDIR": str(temporary_root.resolve()),
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONNOUSERSITE": "1",
    }
    process = subprocess.Popen(
        [sandbox_binary, "-f", str(paths["sandbox"].resolve()), *command],
        cwd=paths["opened"],
        env=environment,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    completed = subprocess.CompletedProcess(
        args=process.args,
        returncode=process.returncode,
        stdout=stdout,
        stderr=stderr,
    )
    return completed, sandbox_denials(process.pid)


def run_answer(
    run_dir: Path,
    candidate_id: str,
    command: list[str],
    declared_opens: Iterable[str],
) -> dict[str, Any]:
    manifest, paths = load_manifest(run_dir, candidate_id)
    del manifest
    if (run_dir / "answer-lock.json").exists():
        raise HarnessError("answer hashes are already locked")
    for requested in declared_opens:
        request_open(run_dir, candidate_id, requested)
    completed, denials = sandbox_command(paths, command)
    stdout_path = paths["output"] / "answer.stdout"
    stderr_path = paths["output"] / "answer.stderr"
    stdout_path.write_text(completed.stdout, encoding="utf-8")
    stderr_path.write_text(completed.stderr, encoding="utf-8")
    result = {
        "returncode": completed.returncode,
        "stdout_sha256": sha256(stdout_path),
        "stderr_sha256": sha256(stderr_path),
        "command_sha256": hashlib.sha256("\0".join(command).encode("utf-8")).hexdigest(),
    }
    append_event(paths, {"type": "answer_command", **result})
    if denials:
        append_event(paths, {
            "type": "hard_isolation_failure",
            "requested_path": ", ".join(item["path"] for item in denials),
            "permitted": False,
            "reason": "sandbox_denial_during_answer",
            "stderr_sha256": result["stderr_sha256"],
            "denied_operations": sorted({item["operation"] for item in denials}),
        })
    return result


def probe_external_path(run_dir: Path, candidate_id: str, external_path: Path) -> dict[str, Any]:
    _, paths = load_manifest(run_dir, candidate_id)
    requested = str(external_path.resolve())
    completed, denials = sandbox_command(
        paths,
        [
            str(SANDBOX_PYTHON),
            "-c",
            "import pathlib,sys; pathlib.Path(sys.argv[1]).read_bytes(); print('READABLE')",
            requested,
        ],
    )
    blocked = bool(denials) and "READABLE" not in completed.stdout
    append_event(paths, {
        "type": "hard_isolation_failure",
        "requested_path": requested,
        "permitted": False,
        "reason": "intentional_escape_blocked" if blocked else "sandbox_escape_succeeded",
        "sandbox_returncode": completed.returncode,
    })
    if not blocked:
        raise HarnessError(f"sandbox unexpectedly read external path: {requested}")
    return {"blocked": True, "returncode": completed.returncode}


def stage_output(run_dir: Path, candidate_id: str, output_file: Path) -> dict[str, Any]:
    _, paths = load_manifest(run_dir, candidate_id)
    if (run_dir / "answer-lock.json").exists():
        raise HarnessError("answer hashes are already locked")
    resolved = output_file.resolve()
    try:
        virtual = resolved.relative_to(paths["output"].resolve()).as_posix()
    except ValueError as error:
        raise HarnessError("output must be inside the candidate output directory") from error
    if not resolved.is_file() or resolved.is_symlink():
        raise HarnessError("staged output must be a regular non-symlink file")
    output_record = {"path": virtual, "sha256": sha256(resolved), "bytes": resolved.stat().st_size}
    if paths["staged"].exists():
        record_data = json.loads(paths["staged"].read_text(encoding="utf-8"))
    else:
        record_data = {"candidate_id": candidate_id, "outputs": []}
    if any(item["path"] == virtual for item in record_data["outputs"]):
        raise HarnessError(f"output is already staged: {virtual}")
    record_data["outputs"].append(output_record)
    record_data["outputs"].sort(key=lambda item: item["path"])
    write_json(paths["staged"], record_data)
    append_event(paths, {"type": "output_staged", **output_record})
    return record_data


def lock_answers(run_dir: Path, candidate_ids: Iterable[str]) -> dict[str, Any]:
    lock_path = run_dir / "answer-lock.json"
    if lock_path.exists():
        raise HarnessError("answer hashes are already locked")
    candidates = sorted({safe_candidate(item) for item in candidate_ids})
    if not candidates:
        raise HarnessError("at least one candidate is required")
    locked: list[dict[str, Any]] = []
    for candidate_id in candidates:
        _, paths = load_manifest(run_dir, candidate_id)
        try:
            staged = json.loads(paths["staged"].read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise HarnessError(f"candidate has no staged output: {candidate_id}") from error
        staged_paths = {item["path"] for item in staged.get("outputs", [])}
        observed_paths = {
            path.relative_to(paths["output"]).as_posix()
            for path in paths["output"].rglob("*")
            if path.is_file() and "tmp" not in path.relative_to(paths["output"]).parts
        }
        if staged_paths != observed_paths:
            missing = sorted(observed_paths - staged_paths)
            extra = sorted(staged_paths - observed_paths)
            raise HarnessError(
                f"candidate outputs are not fully staged: {candidate_id}; unstaged={missing}, missing={extra}"
            )
        for item in staged.get("outputs", []):
            output_path = paths["output"] / item["path"]
            if sha256(output_path) != item["sha256"]:
                raise HarnessError(f"candidate output changed before lock: {candidate_id}/{item['path']}")
            output_path.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        locked.append(staged)
    result = {
        "harness_version": HARNESS_VERSION,
        "state": "LOCKED",
        "candidates": locked,
    }
    write_json(lock_path, result)
    lock_path.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    return result


def prepare_evaluator_inputs(
    run_dir: Path,
    workspace_root: Path,
    evaluation_files: Iterable[Path],
) -> dict[str, Any]:
    lock_path = run_dir / "answer-lock.json"
    if not lock_path.is_file():
        raise HarnessError("evaluator inputs cannot be created before answer hash lock")
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    evaluator_root = run_dir / "evaluator-inputs"
    if evaluator_root.exists():
        raise HarnessError("evaluator inputs already prepared")
    evaluator_root.mkdir(parents=True)
    entries: list[dict[str, Any]] = []

    for candidate in lock["candidates"]:
        candidate_id = candidate["candidate_id"]
        paths = run_paths(run_dir, candidate_id)
        for item in candidate["outputs"]:
            source = paths["output"] / item["path"]
            if sha256(source) != item["sha256"]:
                raise HarnessError(f"locked answer hash mismatch: {candidate_id}/{item['path']}")
            virtual = safe_virtual_path(f"answers/{candidate_id}/{item['path']}")
            destination = evaluator_root / virtual
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            entries.append({"virtual_path": virtual, "category": "answer", "sha256": sha256(destination)})

    for source in evaluation_files:
        resolved = ensure_within(source, workspace_root)
        virtual = safe_virtual_path(f"evaluation/{resolved.name}")
        destination = evaluator_root / virtual
        if destination.exists():
            raise HarnessError(f"duplicate evaluator input basename: {resolved.name}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(resolved, destination)
        entries.append({"virtual_path": virtual, "category": "evaluation", "sha256": sha256(destination)})

    manifest = {
        "harness_version": HARNESS_VERSION,
        "state": "EVALUATOR_READY_AFTER_LOCK",
        "answer_lock_sha256": sha256(lock_path),
        "files": sorted(entries, key=lambda item: item["virtual_path"]),
    }
    write_json(evaluator_root / "manifest.json", manifest)
    make_read_only_tree(evaluator_root)
    return manifest


def isolation_report(run_dir: Path) -> dict[str, Any]:
    event_files = sorted((run_dir / "events").glob("*.json"))
    candidates: list[dict[str, Any]] = []
    failures = 0
    for path in event_files:
        ledger = json.loads(path.read_text(encoding="utf-8"))
        candidate_failures = [item for item in ledger["events"] if item["type"] == "hard_isolation_failure"]
        failures += len(candidate_failures)
        candidates.append({
            "candidate_id": ledger["candidate_id"],
            "actual_open_count": sum(item["type"] == "actual_open" for item in ledger["events"]),
            "hard_isolation_failures": candidate_failures,
        })
    return {
        "harness_version": HARNESS_VERSION,
        "status": "FAIL" if failures else "PASS",
        "hard_isolation_failure_count": failures,
        "candidates": candidates,
    }


def parse_paths(values: Iterable[str]) -> list[Path]:
    return [Path(item) for item in values]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command_name", required=True)

    prepare = subparsers.add_parser("prepare-answer")
    prepare.add_argument("--run-dir", type=Path, required=True)
    prepare.add_argument("--workspace-root", type=Path, default=ROOT)
    prepare.add_argument("--candidate", required=True)
    prepare.add_argument("--question", type=Path, required=True)
    prepare.add_argument("--workflow", action="append", default=[], required=True)
    prepare.add_argument("--course", action="append", default=[], required=True)

    read = subparsers.add_parser("read")
    read.add_argument("--run-dir", type=Path, required=True)
    read.add_argument("--candidate", required=True)
    read.add_argument("--path", required=True)

    run = subparsers.add_parser("run-answer")
    run.add_argument("--run-dir", type=Path, required=True)
    run.add_argument("--candidate", required=True)
    run.add_argument("--declare-open", action="append", default=[])
    run.add_argument("answer_command", nargs=argparse.REMAINDER)

    probe = subparsers.add_parser("probe-external")
    probe.add_argument("--run-dir", type=Path, required=True)
    probe.add_argument("--candidate", required=True)
    probe.add_argument("--path", type=Path, required=True)

    stage = subparsers.add_parser("stage-output")
    stage.add_argument("--run-dir", type=Path, required=True)
    stage.add_argument("--candidate", required=True)
    stage.add_argument("--file", type=Path, required=True)

    lock = subparsers.add_parser("lock-answers")
    lock.add_argument("--run-dir", type=Path, required=True)
    lock.add_argument("--candidate", action="append", required=True)

    evaluator = subparsers.add_parser("prepare-evaluator")
    evaluator.add_argument("--run-dir", type=Path, required=True)
    evaluator.add_argument("--workspace-root", type=Path, default=ROOT)
    evaluator.add_argument("--evaluation-file", action="append", required=True)

    report = subparsers.add_parser("report")
    report.add_argument("--run-dir", type=Path, required=True)

    args = parser.parse_args()
    try:
        if args.command_name == "prepare-answer":
            result = prepare_answer_inputs(
                args.run_dir,
                args.workspace_root,
                args.candidate,
                args.question,
                parse_paths(args.workflow),
                parse_paths(args.course),
            )
        elif args.command_name == "read":
            sys.stdout.buffer.write(request_open(args.run_dir, args.candidate, args.path))
            return 0
        elif args.command_name == "run-answer":
            command = args.answer_command[1:] if args.answer_command[:1] == ["--"] else args.answer_command
            result = run_answer(args.run_dir, args.candidate, command, args.declare_open)
        elif args.command_name == "probe-external":
            result = probe_external_path(args.run_dir, args.candidate, args.path)
        elif args.command_name == "stage-output":
            result = stage_output(args.run_dir, args.candidate, args.file)
        elif args.command_name == "lock-answers":
            result = lock_answers(args.run_dir, args.candidate)
        elif args.command_name == "prepare-evaluator":
            result = prepare_evaluator_inputs(args.run_dir, args.workspace_root, parse_paths(args.evaluation_file))
        else:
            result = isolation_report(args.run_dir)
        print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True))
        return 0
    except HarnessError as error:
        print(json.dumps({"status": "ERROR", "error": str(error)}, sort_keys=True))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
