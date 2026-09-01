#!/usr/bin/env python3
"""Validate a source-bound structured pre-answer RoutePlan.

The validator intentionally reads no free-form answer prose.  It first enforces the
checked-in JSON Schema with a small dependency-free schema walker, then applies the
cross-field routing invariants that JSON Schema cannot express conveniently.

Exit codes are stable: 0 valid, 1 invalid RoutePlan, 2 input/schema/tool error.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SCHEMA = ROOT / "routing-v2/schema/route-plan.schema.json"
REPORT_VERSION = "route-plan-validation-report-v1"
SUCCESS_DISPOSITIONS = {"used - outcome", "used - content", "supported"}
INCLUDED_STATUSES = {"produced", "placeholder"}
# A corporate trustee, foundation council or other corporate fiduciary may be the
# actor signing the operative trust/foundation document.  Corporate member and
# corporate director roles remain supported for underlying corporate structures,
# but they are the only roles that require a distinct upstream authority instrument
# in this contract.
# A corporate trustee's own board/trustee resolution may supply authority for the
# trust act; requiring another synthetic upstream row would duplicate the act.
CORPORATE_UPSTREAM_CAPACITIES = {"corporate_member", "corporate_director"}
INVARIANT_CODES = (
    "NONEMPTY_PLAN",
    "FACT_CLAIM_DISPOSITIONS",
    "CLASSIFICATION_SUPPORT",
    "ENTITY_CARDINALITY_SUPPORT",
    "ENTITY_CAPACITY",
    "SOURCE_NAMESPACE",
    "SOURCE_ALLOWLIST",
    "SOURCE_FILE_INTEGRITY",
    "FORBIDDEN_SOURCE_ACCESS",
    "RELATIONSHIP_SELECTION",
    "BRANCH_DECIDING_FACT",
    "CORPORATE_ACTOR_AUTHORITY",
    "DOCUMENT_COUNT_RECONCILIATION",
    "ACTION_NOTICE_COMPONENTS",
    "COMPLEX_TRANSACTION_DOCUMENTS",
    "MATERIALS_GAP_PRESERVATION",
    "FINAL_ROUTE_TRACE",
    "RENDER_GATE",
)

CLASSIFICATION_FIELDS = (
    "jurisdiction_factors",
    "trust_architecture",
    "actor_capacities",
    "power_characteristics",
    "relationships",
    "lifecycle_stages",
    "governing_instruments",
    "standing",
)
COURSE_NAMESPACES = {"course_manual", "course_appendix"}


@dataclass(frozen=True, order=True)
class Issue:
    code: str
    path: str
    message: str
    severity: str = "critical"

    def as_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "code": self.code,
            "path": self.path,
            "message": self.message,
        }


class Collector:
    def __init__(self) -> None:
        self.issues: list[Issue] = []
        self.failed_invariants: set[str] = set()

    def add(self, invariant: str, path: str, message: str) -> None:
        self.failed_invariants.add(invariant)
        self.issues.append(Issue(invariant, path, message))

    def schema(self, path: str, message: str) -> None:
        self.failed_invariants.add("SCHEMA")
        self.issues.append(Issue("SCHEMA", path, message))


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return sha256_bytes(encoded)


def json_type_matches(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "string":
        return isinstance(value, str)
    if expected == "array":
        return isinstance(value, list)
    if expected == "object":
        return isinstance(value, dict)
    return False


def resolve_ref(schema_root: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise ValueError(f"unsupported schema reference: {ref}")
    current: Any = schema_root
    for token in ref[2:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        current = current[token]
    if not isinstance(current, dict):
        raise ValueError(f"schema reference does not resolve to an object: {ref}")
    return current


def schema_walk(
    value: Any,
    rule: dict[str, Any],
    schema_root: dict[str, Any],
    path: str,
    collector: Collector,
) -> None:
    """Validate the JSON-Schema subset used by route-plan.schema.json."""

    if "$ref" in rule:
        schema_walk(value, resolve_ref(schema_root, rule["$ref"]), schema_root, path, collector)
        return
    for subrule in rule.get("allOf", []):
        schema_walk(value, subrule, schema_root, path, collector)

    if "const" in rule and value != rule["const"]:
        collector.schema(path, f"must equal {rule['const']!r}")
    if "enum" in rule and value not in rule["enum"]:
        collector.schema(path, f"must be one of {rule['enum']!r}")

    expected = rule.get("type")
    if expected is not None:
        expected_types = [expected] if isinstance(expected, str) else expected
        if not any(json_type_matches(value, item) for item in expected_types):
            collector.schema(path, f"expected type {expected_types!r}, got {type(value).__name__}")
            return

    if isinstance(value, dict):
        required = rule.get("required", [])
        for key in required:
            if key not in value:
                collector.schema(f"{path}/{key}", "required property is missing")
        properties = rule.get("properties", {})
        if rule.get("additionalProperties") is False:
            for key in sorted(set(value) - set(properties)):
                collector.schema(f"{path}/{key}", "additional property is not permitted")
        for key, subvalue in value.items():
            if key in properties:
                schema_walk(subvalue, properties[key], schema_root, f"{path}/{key}", collector)

    if isinstance(value, list):
        if len(value) < rule.get("minItems", 0):
            collector.schema(path, f"array has fewer than {rule['minItems']} items")
        item_rule = rule.get("items")
        if isinstance(item_rule, dict):
            for index, item in enumerate(value):
                schema_walk(item, item_rule, schema_root, f"{path}/{index}", collector)
        if rule.get("uniqueItems"):
            seen: set[str] = set()
            for index, item in enumerate(value):
                marker = json.dumps(item, sort_keys=True, separators=(",", ":"))
                if marker in seen:
                    collector.schema(f"{path}/{index}", "array item must be unique")
                seen.add(marker)

    if isinstance(value, str):
        if len(value) < rule.get("minLength", 0):
            collector.schema(path, f"string is shorter than {rule['minLength']}")
        if "pattern" in rule and re.search(rule["pattern"], value) is None:
            collector.schema(path, f"string does not match pattern {rule['pattern']!r}")

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in rule and value < rule["minimum"]:
            collector.schema(path, f"value is below minimum {rule['minimum']}")


def index_unique(
    rows: Iterable[dict[str, Any]],
    collection_path: str,
    collector: Collector,
) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        row_id = row.get("id")
        if not isinstance(row_id, str):
            continue
        if row_id in indexed:
            collector.add("SCHEMA", f"{collection_path}/{index}/id", f"duplicate id {row_id!r}")
        indexed[row_id] = row
    return indexed


def reference_ids(
    ids: Iterable[str],
    known: dict[str, Any],
    invariant: str,
    path: str,
    collector: Collector,
) -> None:
    for index, item_id in enumerate(ids):
        if item_id not in known:
            collector.add(invariant, f"{path}/{index}", f"unknown reference {item_id!r}")


def is_safe_relative_path(value: str) -> bool:
    path = PurePosixPath(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts


def load_source_manifest(source_root: Path, collector: Collector) -> dict[str, str]:
    manifest_path = source_root / "SOURCE-MANIFEST.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        files = manifest["files"]
        if not isinstance(files, dict) or not all(isinstance(key, str) and isinstance(value, str) for key, value in files.items()):
            raise ValueError("files must map paths to SHA-256 strings")
        return files
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, ValueError) as error:
        collector.add("SOURCE_FILE_INTEGRITY", "/source_access", f"cannot load SOURCE-MANIFEST.json: {error}")
        return {}


def validate_invariants(plan: dict[str, Any], collector: Collector, source_root: Path) -> None:
    facts = index_unique(plan.get("facts", []), "/facts", collector)
    claims = index_unique(plan.get("claims", []), "/claims", collector)
    entities = index_unique(plan.get("entities", []), "/entities", collector)
    routes = index_unique(plan.get("routes", []), "/routes", collector)
    gaps = index_unique(plan.get("materials_gaps", []), "/materials_gaps", collector)
    trace = index_unique(plan.get("final_trace", []), "/final_trace", collector)

    if not facts or not routes or not entities:
        collector.add(
            "NONEMPTY_PLAN",
            "",
            "RoutePlan must contain at least one fact, entity and candidate route",
        )
    for field in CLASSIFICATION_FIELDS:
        if not plan.get(field):
            collector.add("NONEMPTY_PLAN", f"/{field}", "mandatory classification array is empty")

    # Every material fact and every MCQ option is represented by exactly one scalar disposition.
    for fact_id, fact in facts.items():
        if fact.get("material") and not isinstance(fact.get("disposition"), str):
            collector.add("FACT_CLAIM_DISPOSITIONS", f"/facts/{fact_id}", "material fact lacks one disposition")
    answer_unit = plan.get("answer_unit", {})
    option_subclaims: dict[str, list[str]] = {}
    option_conclusions: dict[str, list[str]] = {}
    for claim_id, claim in claims.items():
        if claim.get("kind") == "mcq_subclaim":
            option_subclaims.setdefault(str(claim.get("option")), []).append(claim_id)
        elif claim.get("kind") == "mcq_option_conclusion":
            option_conclusions.setdefault(str(claim.get("option")), []).append(claim_id)
    if answer_unit.get("mode") == "MCQ":
        options = answer_unit.get("mcq_options", [])
        selected = answer_unit.get("selected_option")
        closest = answer_unit.get("closest_options", [])
        authorization = plan.get("render_authorization", {})
        unresolved_mcq = selected is None
        if not options:
            collector.add("FACT_CLAIM_DISPOSITIONS", "/answer_unit/mcq_options", "MCQ must declare options")
        if unresolved_mcq:
            if authorization.get("decision") != "do_not_render" or authorization.get("materials_outcome") != "materials do not resolve":
                collector.add("FACT_CLAIM_DISPOSITIONS", "/answer_unit/selected_option", "null selected option is allowed only for a do-not-render, materials-do-not-resolve MCQ")
            if closest and (len(closest) != 2 or any(option not in options for option in closest)):
                collector.add("FACT_CLAIM_DISPOSITIONS", "/answer_unit/closest_options", "unresolved MCQ closest options must be empty or two declared options")
        else:
            if selected not in options:
                collector.add("FACT_CLAIM_DISPOSITIONS", "/answer_unit/selected_option", "selected option must be one declared MCQ option")
            if len(closest) != 2 or any(option not in options for option in closest):
                collector.add("FACT_CLAIM_DISPOSITIONS", "/answer_unit/closest_options", "resolved MCQ must identify two distinct declared closest options")
            elif selected not in closest:
                collector.add("FACT_CLAIM_DISPOSITIONS", "/answer_unit/closest_options", "closest options must include the selected answer")
        if answer_unit.get("polarity") is None:
            collector.add("FACT_CLAIM_DISPOSITIONS", "/answer_unit/polarity", "MCQ must record its exact polarity")
        for option in options:
            subclaims = option_subclaims.get(option, [])
            conclusions = option_conclusions.get(option, [])
            if not subclaims:
                collector.add(
                    "FACT_CLAIM_DISPOSITIONS",
                    "/claims",
                    f"MCQ option {option!r} must have at least one independently disposed subclaim",
                )
            if len(conclusions) != 1:
                collector.add(
                    "FACT_CLAIM_DISPOSITIONS",
                    "/claims",
                    f"MCQ option {option!r} must have exactly one option conclusion; found {len(conclusions)}",
                )
        extras = sorted((set(option_subclaims) | set(option_conclusions)) - set(options))
        if extras:
            collector.add("FACT_CLAIM_DISPOSITIONS", "/claims", f"orphan MCQ option claims: {extras}")
    elif (
        answer_unit.get("mcq_options")
        or answer_unit.get("selected_option") is not None
        or answer_unit.get("closest_options")
        or option_subclaims
        or option_conclusions
    ):
        collector.add("FACT_CLAIM_DISPOSITIONS", "/answer_unit", "non-MCQ unit cannot declare MCQ option analysis")
    elif answer_unit.get("polarity") is not None:
        collector.add("FACT_CLAIM_DISPOSITIONS", "/answer_unit/polarity", "non-MCQ unit must leave polarity null")

    # All eight classification arrays use the same supported lock contract.
    classification_ids: set[str] = set()
    for name in CLASSIFICATION_FIELDS:
        for index, lock in enumerate(plan.get(name, [])):
            path = f"/{name}/{index}"
            lock_id = lock.get("id")
            if lock_id in classification_ids:
                collector.add("CLASSIFICATION_SUPPORT", f"{path}/id", f"duplicate classification id {lock_id!r}")
            classification_ids.add(lock_id)
            state = lock.get("state")
            value = lock.get("value")
            fact_ids = lock.get("deciding_fact_ids", [])
            reference_ids(fact_ids, facts, "CLASSIFICATION_SUPPORT", f"{path}/deciding_fact_ids", collector)
            if state == "genuinely_unknown":
                if value is not None:
                    collector.add("CLASSIFICATION_SUPPORT", f"{path}/value", "genuinely unknown classification must have null value")
            else:
                if not isinstance(value, str) or not value.strip():
                    collector.add("CLASSIFICATION_SUPPORT", f"{path}/value", f"{state} classification requires a selected value")
                if not fact_ids:
                    collector.add("CLASSIFICATION_SUPPORT", f"{path}/deciding_fact_ids", f"{state} classification requires supporting facts")
                for fact_id in fact_ids:
                    if fact_id in facts and facts[fact_id].get("disposition") not in SUCCESS_DISPOSITIONS:
                        collector.add("CLASSIFICATION_SUPPORT", path, f"classification relies on non-supporting fact {fact_id!r}")

    # Exact role counts are supported only by typed facts for the same entity/value.
    for entity_id, entity in entities.items():
        entity_type = entity.get("entity_type")
        capacities = set(entity.get("capacities", []))
        impossible = (
            (entity_type == "trust" and capacities != {"trust"})
            or (entity_type == "purpose_trust" and capacities != {"purpose_trust"})
            or (
                entity_type == "foundation"
                and (
                    "foundation" not in capacities
                    or bool(capacities & {"trust", "purpose_trust", "corporate_trustee", "corporate_councillor", "corporate_member", "corporate_director"})
                )
            )
            or (entity_type == "human" and bool(capacities & {"trust", "purpose_trust", "foundation", "corporate_trustee", "corporate_councillor", "corporate_member", "corporate_director"}))
            or (entity_type == "corporate" and bool(capacities & {"trust", "purpose_trust", "foundation"}))
        )
        if impossible or not capacities:
            collector.add("ENTITY_CAPACITY", f"/entities/{entity_id}", "entity type and asserted capacities are incompatible")
        seen_kinds: set[str] = set()
        for index, cardinality in enumerate(entity.get("cardinalities", [])):
            path = f"/entities/{entity_id}/cardinalities/{index}"
            kind = cardinality.get("kind")
            count = cardinality.get("count")
            fact_ids = cardinality.get("fact_ids", [])
            if kind in seen_kinds:
                collector.add("ENTITY_CARDINALITY_SUPPORT", path, f"duplicate cardinality kind {kind!r}")
            seen_kinds.add(kind)
            reference_ids(fact_ids, facts, "ENTITY_CARDINALITY_SUPPORT", f"{path}/fact_ids", collector)
            if count is not None and not fact_ids:
                collector.add("ENTITY_CARDINALITY_SUPPORT", f"{path}/count", "exact cardinality lacks a supplied fact")
            for fact_id in fact_ids:
                fact = facts.get(fact_id, {})
                if fact.get("kind") != "cardinality" or fact.get("subject_id") != entity_id or fact.get("value") != count or fact.get("disposition") not in SUCCESS_DISPOSITIONS:
                    collector.add("ENTITY_CARDINALITY_SUPPORT", f"{path}/fact_ids", f"fact {fact_id!r} does not support this entity cardinality")

    # Namespace lists are authoritative, and all route/access paths must be safe and listed.
    namespace_paths = {
        namespace: set(paths)
        for namespace, paths in plan.get("namespaces", {}).items()
    }
    for namespace, paths in namespace_paths.items():
        for path in paths:
            if not is_safe_relative_path(path):
                collector.add("SOURCE_NAMESPACE", f"/namespaces/{namespace}", f"unsafe path {path!r}")
    for route_id, route in routes.items():
        source = route.get("source", {})
        namespace = source.get("namespace")
        path = source.get("path")
        if path not in namespace_paths.get(namespace, set()):
            collector.add("SOURCE_NAMESPACE", f"/routes/{route_id}/source", "route source is absent from its namespace")
        reference_ids(route.get("triggering_fact_ids", []), facts, "SOURCE_NAMESPACE", f"/routes/{route_id}/triggering_fact_ids", collector)
        reference_ids(route.get("deciding_fact_ids", []), facts, "BRANCH_DECIDING_FACT", f"/routes/{route_id}/deciding_fact_ids", collector)
        reference_ids(route.get("gap_ids", []), gaps, "MATERIALS_GAP_PRESERVATION", f"/routes/{route_id}/gap_ids", collector)

    access = plan.get("source_access", {})
    allowlist = access.get("allowlist", [])
    actual_open = access.get("actual_open", [])
    expected_allowlist_hash = hashlib.sha256(
        json.dumps(allowlist, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    if access.get("allowlist_sha256") != expected_allowlist_hash:
        collector.add(
            "SOURCE_ALLOWLIST",
            "/source_access/allowlist_sha256",
            "frozen allowlist hash does not match the declared allowlist",
        )
    allow_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for index, entry in enumerate(allowlist):
        key = (entry.get("namespace"), entry.get("path"))
        if key in allow_by_key:
            collector.add("SOURCE_ALLOWLIST", f"/source_access/allowlist/{index}", f"duplicate allowlist entry {key!r}")
        allow_by_key[key] = entry
        if entry.get("path") not in namespace_paths.get(entry.get("namespace"), set()):
            collector.add("SOURCE_NAMESPACE", f"/source_access/allowlist/{index}", "allowlist path is absent from its namespace")
    open_keys: set[tuple[str, str]] = set()
    actual_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    course_manifest = load_source_manifest(source_root, collector)
    for index, entry in enumerate(actual_open):
        key = (entry.get("namespace"), entry.get("path"))
        if key in open_keys:
            collector.add("SOURCE_ALLOWLIST", f"/source_access/actual_open/{index}", f"duplicate actual-open ledger entry {key!r}")
        open_keys.add(key)
        actual_by_key[key] = entry
        if key not in allow_by_key:
            collector.add("SOURCE_ALLOWLIST", f"/source_access/actual_open/{index}", "actual-open file lies outside frozen allowlist")
        elif allow_by_key[key].get("role") != entry.get("role"):
            collector.add(
                "SOURCE_ALLOWLIST",
                f"/source_access/actual_open/{index}/role",
                "actual-open role does not match the frozen allowlist role",
            )
        relative_path = entry.get("path")
        if isinstance(relative_path, str) and is_safe_relative_path(relative_path):
            file_path = source_root / relative_path
            if file_path.is_symlink():
                collector.add("SOURCE_FILE_INTEGRITY", f"/source_access/actual_open/{index}/path", "actual-open source cannot be a symlink")
            elif not file_path.is_file():
                collector.add("SOURCE_FILE_INTEGRITY", f"/source_access/actual_open/{index}/path", "actual-open path is not a real file under source root")
            else:
                try:
                    file_path.resolve().relative_to(source_root.resolve())
                except ValueError:
                    collector.add("SOURCE_FILE_INTEGRITY", f"/source_access/actual_open/{index}/path", "actual-open source resolves outside source root")
                actual_hash = sha256_bytes(file_path.read_bytes())
                if entry.get("sha256") != actual_hash:
                    collector.add("SOURCE_FILE_INTEGRITY", f"/source_access/actual_open/{index}/sha256", "declared SHA-256 does not match file bytes")
                if entry.get("namespace") in COURSE_NAMESPACES and course_manifest.get(relative_path) != actual_hash:
                    collector.add("SOURCE_FILE_INTEGRITY", f"/source_access/actual_open/{index}", "course source is absent from SOURCE-MANIFEST.json or its manifest hash differs")

    for route_id, route_item in routes.items():
        source = route_item.get("source", {})
        key = (source.get("namespace"), source.get("path"))
        requirement = route_item.get("requirement")
        verdict = route_item.get("verdict")
        allowed = allow_by_key.get(key)
        opened = actual_by_key.get(key)
        if requirement == "mandatory" and verdict != "incorporated":
            collector.add(
                "SOURCE_ALLOWLIST",
                f"/routes/{route_id}",
                "mandatory route must be incorporated; conditional, forbidden and check-only candidates are optional until selected",
            )
        if verdict == "incorporated" and requirement != "mandatory":
            collector.add(
                "SOURCE_ALLOWLIST",
                f"/routes/{route_id}/requirement",
                "incorporated route must be marked mandatory after the relevance gate",
            )
        if verdict == "incorporated":
            if allowed is None or allowed.get("role") != "incorporated":
                collector.add(
                    "SOURCE_ALLOWLIST",
                    f"/routes/{route_id}/source",
                    "incorporated route must be frozen in the allowlist with incorporated role",
                )
            if opened is None or opened.get("role") != "incorporated":
                collector.add(
                    "SOURCE_ALLOWLIST",
                    f"/routes/{route_id}/source",
                    "incorporated route source is missing from the actual-open ledger",
                )
            trigger_ids = route_item.get("triggering_fact_ids", [])
            if not trigger_ids or not any(facts.get(fact_id, {}).get("disposition") in SUCCESS_DISPOSITIONS for fact_id in trigger_ids):
                collector.add("SOURCE_ALLOWLIST", f"/routes/{route_id}/triggering_fact_ids", "incorporated route requires a supporting trigger fact")
        elif verdict == "conditional" and allowed is None:
            collector.add(
                "SOURCE_ALLOWLIST",
                f"/routes/{route_id}/source",
                "conditional route must be represented in the frozen allowlist",
            )
        elif verdict == "checked_not_relevant":
            if allowed is None or opened is None or allowed.get("role") != "check_only" or opened.get("role") != "check_only":
                collector.add("SOURCE_ALLOWLIST", f"/routes/{route_id}/source", "checked-not-relevant route requires a real check-only open")

    prohibited = set(access.get("forbidden_paths", [])) | set(access.get("prior_answer_paths", []))
    forbidden_route_paths = {
        route.get("source", {}).get("path")
        for route in routes.values()
        if route.get("verdict") == "forbidden"
    }
    prohibited |= {item for item in forbidden_route_paths if isinstance(item, str)}
    for list_name, entries in (("allowlist", allowlist), ("actual_open", actual_open)):
        for index, entry in enumerate(entries):
            if entry.get("path") in prohibited:
                collector.add(
                    "FORBIDDEN_SOURCE_ACCESS",
                    f"/source_access/{list_name}/{index}",
                    "forbidden or prior-answer file cannot be opened or converted to check-only access",
                )

    # A route may participate in several independent relationship sets.  Its
    # verdict is derived from the union of selected memberships, so an unresolved
    # set cannot contradict a separate selected prerequisite/sequence membership.
    route_memberships: dict[str, set[str]] = {route_id: set() for route_id in routes}
    selected_routes: set[str] = set()
    unresolved_routes: set[str] = set()
    seen_set_ids: set[str] = set()
    for index, relationship_set in enumerate(plan.get("route_relationship_sets", [])):
        set_id = relationship_set.get("id")
        path = f"/route_relationship_sets/{index}"
        kind = relationship_set.get("kind")
        route_ids = relationship_set.get("route_ids", [])
        selected = relationship_set.get("selected_route_ids", [])
        deciding = relationship_set.get("deciding_fact_ids", [])
        if set_id in seen_set_ids:
            collector.add("RELATIONSHIP_SELECTION", f"{path}/id", f"duplicate relationship-set id {set_id!r}")
        seen_set_ids.add(set_id)
        reference_ids(route_ids, routes, "RELATIONSHIP_SELECTION", f"{path}/route_ids", collector)
        reference_ids(selected, routes, "RELATIONSHIP_SELECTION", f"{path}/selected_route_ids", collector)
        reference_ids(deciding, facts, "BRANCH_DECIDING_FACT", f"{path}/deciding_fact_ids", collector)
        if not route_ids:
            collector.add("RELATIONSHIP_SELECTION", f"{path}/route_ids", "relationship set cannot be empty")
        for route_id in route_ids:
            route_memberships.setdefault(route_id, set()).add(set_id)
        if not set(selected).issubset(route_ids):
            collector.add("RELATIONSHIP_SELECTION", f"{path}/selected_route_ids", "selected route is outside relationship set")
        state = relationship_set.get("selection_state")
        if state == "selected":
            valid_shape = (
                (kind == "XOR" and len(selected) == 1)
                or (kind == "AND prerequisite" and set(selected) == set(route_ids))
                or (kind == "SEQUENCE" and selected == route_ids)
                or (kind == "OPTIONAL overlay" and bool(selected) and set(selected).issubset(route_ids))
            )
            if not valid_shape:
                collector.add("RELATIONSHIP_SELECTION", f"{path}/selected_route_ids", f"selected routes do not satisfy {kind} semantics")
            if not deciding:
                collector.add("BRANCH_DECIDING_FACT", f"{path}/deciding_fact_ids", "selected relationship set lacks a deciding fact")
            for fact_id in deciding:
                if fact_id in facts and facts[fact_id].get("disposition") not in SUCCESS_DISPOSITIONS:
                    collector.add("BRANCH_DECIDING_FACT", path, f"relationship set relies on non-deciding fact {fact_id!r}")
            selected_routes.update(selected)
        elif state == "unresolved":
            if selected:
                collector.add("RELATIONSHIP_SELECTION", f"{path}/selected_route_ids", "unresolved relationship set cannot select routes")
            unresolved_routes.update(route_ids)
        elif state == "not_applicable" and selected:
            collector.add("RELATIONSHIP_SELECTION", f"{path}/selected_route_ids", "not-applicable relationship set cannot select routes")

    for route_id, route in routes.items():
        declared = set(route.get("relationship_set_ids", []))
        actual = route_memberships.get(route_id, set())
        if declared != actual:
            collector.add(
                "RELATIONSHIP_SELECTION",
                f"/routes/{route_id}/relationship_set_ids",
                f"route/set membership mismatch: declared={sorted(declared)}, actual={sorted(actual)}",
            )
        verdict = route.get("verdict")
        if route_id in selected_routes and verdict != "incorporated":
            collector.add("RELATIONSHIP_SELECTION", f"/routes/{route_id}/verdict", "route selected by a relationship set must be incorporated")
        if route_id in unresolved_routes and route_id not in selected_routes and verdict != "conditional":
            collector.add("RELATIONSHIP_SELECTION", f"/routes/{route_id}/verdict", "route found only in unresolved sets must remain conditional")
        if declared and verdict == "incorporated" and route_id not in selected_routes:
            collector.add("RELATIONSHIP_SELECTION", f"/routes/{route_id}/verdict", "incorporated route needs at least one selected relationship-set basis")

    # Document chain: actor authority, counts, embedded notice business and
    # complex trust/foundation bundles.
    chain = plan.get("requested_document_chain", {})
    instruments = index_unique(chain.get("instruments", []), "/requested_document_chain/instruments", collector)
    sequence_seen: set[int] = set()
    component_ids: set[str] = set()
    attachment_ids: set[str] = set()
    record_ids: set[str] = set()
    execution_ids: set[str] = set()
    for instrument_id, instrument in instruments.items():
        sequence = instrument.get("sequence")
        if sequence in sequence_seen:
            collector.add("DOCUMENT_COUNT_RECONCILIATION", f"/requested_document_chain/instruments/{instrument_id}/sequence", "instrument sequence must be unique")
        sequence_seen.add(sequence)
        actor_id = instrument.get("actor_id")
        if actor_id not in entities:
            collector.add("CORPORATE_ACTOR_AUTHORITY", f"/requested_document_chain/instruments/{instrument_id}/actor_id", f"unknown actor {actor_id!r}")
        actor = entities.get(actor_id, {})
        if actor.get("entity_type") in {"trust", "purpose_trust"} or bool(set(actor.get("capacities", [])) & {"trust", "purpose_trust"}):
            collector.add("ENTITY_CAPACITY", f"/requested_document_chain/instruments/{instrument_id}/actor_id", "a trust or purpose trust is not a legal instrument actor; identify its trustee")
        signatories = instrument.get("signatories", [])
        if not signatories or any(signatory.get("human") is not True for signatory in signatories):
            collector.add("CORPORATE_ACTOR_AUTHORITY", f"/requested_document_chain/instruments/{instrument_id}/signatories", "operative instrument requires one or more human signatories")
        upstream_id = instrument.get("upstream_authority_instrument_id")
        authority_refs = [("upstream_authority_instrument_id", upstream_id)] + [
            (f"signatories/{index}/authority_instrument_id", signatory.get("authority_instrument_id"))
            for index, signatory in enumerate(signatories)
        ]
        for field_name, authority_id in authority_refs:
            if authority_id is None:
                continue
            authority_path = f"/requested_document_chain/instruments/{instrument_id}/{field_name}"
            if authority_id == instrument_id:
                collector.add("CORPORATE_ACTOR_AUTHORITY", authority_path, "authority reference cannot point to the instrument itself")
            elif authority_id not in instruments:
                collector.add("CORPORATE_ACTOR_AUTHORITY", authority_path, f"authority reference points to unknown instrument {authority_id!r}")
            elif instruments[authority_id].get("sequence", 0) >= instrument.get("sequence", 0):
                collector.add("CORPORATE_ACTOR_AUTHORITY", authority_path, "authority instrument must precede the instrument that relies on it")
        corporate_target_actor = actor.get("entity_type") == "corporate" and bool(
            CORPORATE_UPSTREAM_CAPACITIES & set(actor.get("capacities", []))
        ) and instrument.get("target_act") is True
        if corporate_target_actor:
            if not upstream_id or upstream_id == instrument_id or upstream_id not in instruments:
                collector.add("CORPORATE_ACTOR_AUTHORITY", f"/requested_document_chain/instruments/{instrument_id}/upstream_authority_instrument_id", "corporate member/director needs a distinct upstream authority instrument")
            else:
                upstream = instruments[upstream_id]
                if upstream.get("kind") != "upstream_authority" or upstream.get("actor_id") != actor_id or upstream.get("target_act"):
                    collector.add("CORPORATE_ACTOR_AUTHORITY", f"/requested_document_chain/instruments/{upstream_id}", "upstream authority must belong to the same corporate actor and precede the target act")
                if upstream.get("sequence", 0) >= instrument.get("sequence", 0):
                    collector.add("CORPORATE_ACTOR_AUTHORITY", f"/requested_document_chain/instruments/{instrument_id}/sequence", "upstream authority must precede the target instrument")
                if any(signatory.get("authority_instrument_id") != upstream_id for signatory in signatories):
                    collector.add("CORPORATE_ACTOR_AUTHORITY", f"/requested_document_chain/instruments/{instrument_id}/signatories", "each human signatory must derive authority from the distinct upstream instrument")

        for component in instrument.get("operative_components", []):
            component_id = component.get("id")
            if component_id in component_ids:
                collector.add("DOCUMENT_COUNT_RECONCILIATION", f"/requested_document_chain/instruments/{instrument_id}/operative_components", f"duplicate component id {component_id!r}")
            component_ids.add(component_id)
            validate_gap_backing(component, f"/requested_document_chain/instruments/{instrument_id}/operative_components/{component_id}", gaps, collector)
        for attachment in instrument.get("attachments", []):
            attachment_id = attachment.get("id")
            if attachment_id in attachment_ids:
                collector.add("DOCUMENT_COUNT_RECONCILIATION", f"/requested_document_chain/instruments/{instrument_id}/attachments", f"duplicate attachment id {attachment_id!r}")
            attachment_ids.add(attachment_id)
            validate_gap_backing(attachment, f"/requested_document_chain/instruments/{instrument_id}/attachments/{attachment_id}", gaps, collector)
        for record in instrument.get("records_filings", []):
            record_id = record.get("id")
            if record_id in record_ids:
                collector.add("DOCUMENT_COUNT_RECONCILIATION", f"/requested_document_chain/instruments/{instrument_id}/records_filings", f"duplicate record/filing id {record_id!r}")
            record_ids.add(record_id)
            validate_gap_backing(record, f"/requested_document_chain/instruments/{instrument_id}/records_filings/{record_id}", gaps, collector)
        execution = instrument.get("execution", {})
        execution_id = execution.get("id")
        if execution_id in execution_ids:
            collector.add("DOCUMENT_COUNT_RECONCILIATION", f"/requested_document_chain/instruments/{instrument_id}/execution", f"duplicate execution id {execution_id!r}")
        execution_ids.add(execution_id)
        validate_gap_backing(execution, f"/requested_document_chain/instruments/{instrument_id}/execution", gaps, collector)

        if chain.get("required"):
            has_content = (
                any(item.get("status") in INCLUDED_STATUSES for item in instrument.get("operative_components", []))
                or any(item.get("status") in INCLUDED_STATUSES for item in instrument.get("attachments", []))
                or any(item.get("status") in INCLUDED_STATUSES for item in instrument.get("records_filings", []))
            )
            if not has_content:
                collector.add("DOCUMENT_COUNT_RECONCILIATION", f"/requested_document_chain/instruments/{instrument_id}", "requested instrument has no produced or placeholder-backed content")

        if instrument.get("kind") == "notice" and instrument.get("action_business"):
            selected_components = set(instrument.get("selected_action_component_ids", []))
            included_sources = {
                item.get("source_component_id")
                for item in instrument.get("operative_components", [])
                if item.get("status") in INCLUDED_STATUSES
            }
            missing = sorted(selected_components - included_sources)
            if not selected_components:
                collector.add("ACTION_NOTICE_COMPONENTS", f"/requested_document_chain/instruments/{instrument_id}/selected_action_component_ids", "action notice must identify selected action-precedent operatives")
            if missing:
                collector.add("ACTION_NOTICE_COMPONENTS", f"/requested_document_chain/instruments/{instrument_id}/operative_components", f"notice omits selected action-precedent operatives: {missing}")

    computed = {
        "instruments": len(instruments),
        "operative_components": sum(
            1
            for instrument in instruments.values()
            for item in instrument.get("operative_components", [])
            if item.get("status") in INCLUDED_STATUSES
        ),
        "attachments": sum(
            1
            for instrument in instruments.values()
            for item in instrument.get("attachments", [])
            if item.get("status") in INCLUDED_STATUSES
        ),
        "execution_blocks": sum(
            1 for instrument in instruments.values() if instrument.get("execution", {}).get("status") in INCLUDED_STATUSES
        ),
        "records_filings": sum(
            1
            for instrument in instruments.values()
            for item in instrument.get("records_filings", [])
            if item.get("status") in INCLUDED_STATUSES
        ),
    }
    expected = chain.get("expected_counts", {})
    actual = chain.get("actual_counts", {})
    if expected != actual:
        collector.add("DOCUMENT_COUNT_RECONCILIATION", "/requested_document_chain", f"expected and actual counts differ: expected={expected}, actual={actual}")
    if actual != computed:
        collector.add("DOCUMENT_COUNT_RECONCILIATION", "/requested_document_chain/actual_counts", f"declared actual counts do not match included document components: declared={actual}, computed={computed}")
    if chain.get("required") and not instruments:
        collector.add("DOCUMENT_COUNT_RECONCILIATION", "/requested_document_chain/instruments", "requested document chain is empty")

    if chain.get("complex_transaction"):
        # Trust and foundation matters do not share a fixed
        # conveyance/facility/security/register-of-charges bundle.  A complex
        # chain is therefore checked generically: it must retain more than one
        # distinct included document component and, where the route declares a
        # records/filings stage, that stage must contain an actual produced entry.
        included_component_ids = {
            item.get("id")
            for instrument in instruments.values()
            for item in instrument.get("operative_components", [])
            if item.get("status") in INCLUDED_STATUSES
        }
        included_attachment_ids = {
            item.get("id")
            for instrument in instruments.values()
            for item in instrument.get("attachments", [])
            if item.get("status") in INCLUDED_STATUSES
        }
        included_record_ids = {
            item.get("id")
            for instrument in instruments.values()
            for item in instrument.get("records_filings", [])
            if item.get("status") in INCLUDED_STATUSES
        }
        included_document_ids = included_component_ids | included_attachment_ids | included_record_ids
        if len(included_document_ids) < 2 and len(instruments) < 2:
            collector.add(
                "COMPLEX_TRANSACTION_DOCUMENTS",
                "/requested_document_chain/instruments",
                "complex trust/foundation transaction must retain at least two distinct included documents or instruments",
            )
        declared_records = any(instrument.get("records_filings") for instrument in instruments.values())
        produced_records = any(
            item.get("status") == "produced"
            for instrument in instruments.values()
            for item in instrument.get("records_filings", [])
        )
        if declared_records and not produced_records:
            collector.add(
                "COMPLEX_TRANSACTION_DOCUMENTS",
                "/requested_document_chain/instruments",
                "complex trust/foundation transaction declares records or filings but has no actual produced entry",
            )

    # Every unresolved route/form point stays conditional or is represented by a placeholder.
    for route_id, route in routes.items():
        if route.get("unresolved"):
            if route.get("verdict") != "conditional" or not route.get("gap_ids"):
                collector.add("MATERIALS_GAP_PRESERVATION", f"/routes/{route_id}", "unresolved route must remain conditional and cite a materials gap")
    affected_known = set(routes) | component_ids | attachment_ids | record_ids | execution_ids | set(instruments)
    for gap_id, gap in gaps.items():
        if not gap.get("affected_ids"):
            collector.add("MATERIALS_GAP_PRESERVATION", f"/materials_gaps/{gap_id}/affected_ids", "materials gap must identify affected route or document fields")
        for affected_id in gap.get("affected_ids", []):
            if affected_id not in affected_known:
                collector.add("MATERIALS_GAP_PRESERVATION", f"/materials_gaps/{gap_id}/affected_ids", f"gap points to unknown affected id {affected_id!r}")

    # Every mandatory incorporated route contributes a specific final assertion.
    traces_by_route: dict[str, list[dict[str, Any]]] = {}
    for trace_id, entry in trace.items():
        route_id = entry.get("route_id")
        if route_id not in routes:
            collector.add("FINAL_ROUTE_TRACE", f"/final_trace/{trace_id}/route_id", f"unknown route {route_id!r}")
        traces_by_route.setdefault(str(route_id), []).append(entry)
    for route_id, route_item in routes.items():
        entries = traces_by_route.get(route_id, [])
        if len(entries) != 1:
            collector.add(
                "FINAL_ROUTE_TRACE",
                f"/routes/{route_id}",
                f"every incorporated, conditional, forbidden or checked route must have exactly one trace; found {len(entries)}",
            )
        elif entries[0].get("contribution") != route_item.get("unique_contribution"):
            collector.add("FINAL_ROUTE_TRACE", f"/final_trace/{entries[0].get('id')}/contribution", "trace must retain the route's unique contribution verbatim")

    authorization = plan.get("render_authorization", {})
    decision = authorization.get("decision")
    input_complete = authorization.get("input_complete")
    outcome = authorization.get("materials_outcome")
    has_input_gap = any(fact.get("disposition") == "input gap" for fact in facts.values())
    has_placeholders = bool(gaps) or any(
        item.get("status") in {"placeholder", "conditional"}
        for instrument in instruments.values()
        for collection in ("operative_components", "attachments", "records_filings")
        for item in instrument.get(collection, [])
    )
    if input_complete is False and decision != "do_not_render":
        collector.add("RENDER_GATE", "/render_authorization/decision", "incomplete input cannot authorize rendering")
    if input_complete is False and not has_input_gap:
        collector.add("RENDER_GATE", "/render_authorization/input_complete", "incomplete input must be represented by an input-gap fact")
    if has_input_gap and (input_complete is not False or decision != "do_not_render"):
        collector.add("RENDER_GATE", "/render_authorization", "input-gap disposition requires incomplete input and do-not-render")
    if outcome == "materials do not resolve" and decision != "do_not_render":
        collector.add("RENDER_GATE", "/render_authorization/decision", "unresolved materials cannot authorize rendering")
    if decision == "render" and (not input_complete or has_placeholders or outcome != "answerable"):
        collector.add("RENDER_GATE", "/render_authorization", "render requires complete input, answerable materials and no gaps/placeholders")
    if decision == "render_with_placeholders" and (
        not input_complete or not has_placeholders or outcome not in {"answerable with placeholders", "conditional answer", "partial course coverage"}
    ):
        collector.add("RENDER_GATE", "/render_authorization", "placeholder rendering requires complete input and an identified placeholder/conditional materials gap")
    if decision == "do_not_render" and input_complete and not has_input_gap and outcome != "materials do not resolve":
        collector.add("RENDER_GATE", "/render_authorization", "do-not-render requires an input gap or materials-do-not-resolve outcome")

    render_gate = plan.get("render_gate", {})
    if render_gate != {"status": "not_rendered", "validation_report": None}:
        collector.add("RENDER_GATE", "/render_gate", "RoutePlan must be validated before any answer is rendered")


def validate_gap_backing(
    item: dict[str, Any],
    path: str,
    gaps: dict[str, dict[str, Any]],
    collector: Collector,
) -> None:
    gap_ids = item.get("gap_ids", [])
    reference_ids(gap_ids, gaps, "MATERIALS_GAP_PRESERVATION", f"{path}/gap_ids", collector)
    if item.get("unresolved"):
        if item.get("status") not in {"placeholder", "conditional"} or not gap_ids:
            collector.add("MATERIALS_GAP_PRESERVATION", path, "unresolved document/form point must be conditional or placeholder-backed")


def build_report(
    plan: dict[str, Any] | None,
    schema: dict[str, Any] | None,
    collector: Collector,
    exit_code: int,
    error: str | None = None,
) -> dict[str, Any]:
    issues = sorted(set(collector.issues))
    status = "ERROR" if exit_code == 2 else ("VALID" if exit_code == 0 else "INVALID")
    invariants = [
        {"code": code, "status": "FAIL" if code in collector.failed_invariants else "PASS"}
        for code in INVARIANT_CODES
    ]
    report: dict[str, Any] = {
        "report_version": REPORT_VERSION,
        "plan_id": plan.get("plan_id") if isinstance(plan, dict) else None,
        "status": status,
        "exit_code": exit_code,
        "schema_sha256": canonical_sha256(schema) if schema is not None else None,
        "plan_sha256": canonical_sha256(plan) if plan is not None else None,
        "render_authorization": plan.get("render_authorization") if isinstance(plan, dict) else None,
        "summary": {
            "critical_count": len(issues),
            "warning_count": 0,
        },
        "invariants": invariants,
        "issues": [issue.as_dict() for issue in issues],
    }
    if error is not None:
        report["error"] = error
    return report


def validate(plan: dict[str, Any], schema: dict[str, Any], source_root: Path = ROOT) -> tuple[dict[str, Any], int]:
    collector = Collector()
    schema_walk(plan, schema, schema, "", collector)
    if not collector.issues:
        validate_invariants(plan, collector, source_root)
    exit_code = 0 if not collector.issues else 1
    return build_report(plan, schema, collector, exit_code), exit_code


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path, help="RoutePlan JSON to validate")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--source-root", type=Path, default=ROOT, help="root containing opened sources and SOURCE-MANIFEST.json")
    parser.add_argument("--output", type=Path, help="also write the deterministic report to this path")
    parser.add_argument("--compact", action="store_true", help="emit one-line JSON")
    args = parser.parse_args()

    plan: dict[str, Any] | None = None
    schema: dict[str, Any] | None = None
    collector = Collector()
    try:
        schema = json.loads(args.schema.read_text(encoding="utf-8"))
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
        if not isinstance(schema, dict) or not isinstance(plan, dict):
            raise ValueError("schema and RoutePlan roots must be JSON objects")
        report, exit_code = validate(plan, schema, args.source_root.resolve())
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, ValueError) as error:
        exit_code = 2
        report = build_report(plan, schema, collector, exit_code, f"{type(error).__name__}: {error}")

    rendered = json.dumps(
        report,
        indent=None if args.compact else 2,
        sort_keys=True,
        ensure_ascii=True,
        separators=(",", ":") if args.compact else None,
    ) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
