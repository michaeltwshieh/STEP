"""Generic RoutePlan fixtures for deterministic validator regression tests.

The fixtures reference frozen case IDs only.  They deliberately avoid copying names,
amounts or other specimen facts into production validation rules.
"""

from __future__ import annotations

import copy
import hashlib
import json
from typing import Any, Callable


def digest(label: str) -> str:
    return hashlib.sha256(label.encode("utf-8")).hexdigest()


def component(component_id: str, source_id: str | None = None) -> dict[str, Any]:
    return {
        "id": component_id,
        "source_component_id": source_id or component_id,
        "status": "produced",
        "unresolved": False,
        "gap_ids": [],
    }


def attachment(attachment_id: str, kind: str) -> dict[str, Any]:
    return {
        "id": attachment_id,
        "kind": kind,
        "status": "produced",
        "unresolved": False,
        "gap_ids": [],
    }


def record(record_id: str, kind: str) -> dict[str, Any]:
    return {
        "id": record_id,
        "kind": kind,
        "status": "produced",
        "unresolved": False,
        "gap_ids": [],
    }


def instrument(
    instrument_id: str,
    sequence: int,
    kind: str,
    actor_id: str,
    *,
    target_company_act: bool = False,
    upstream_id: str | None = None,
    action_business: bool = False,
    selected_action_ids: list[str] | None = None,
    components: list[dict[str, Any]] | None = None,
    attachments: list[dict[str, Any]] | None = None,
    records: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    return {
        "id": instrument_id,
        "sequence": sequence,
        "kind": kind,
        "actor_id": actor_id,
        "target_company_act": target_company_act,
        "upstream_authority_instrument_id": upstream_id,
        "target_instrument": f"Generic {kind} instrument",
        "signatory": {
            "human": True,
            "name_or_placeholder": "[authorised human signatory]",
            "authority_instrument_id": upstream_id,
        },
        "action_business": action_business,
        "selected_action_component_ids": selected_action_ids or [],
        "operative_components": components or [],
        "attachments": attachments or [],
        "execution": {
            "id": f"X_{instrument_id}",
            "status": "produced",
            "unresolved": False,
            "gap_ids": [],
        },
        "records_filings": records or [],
    }


def entity(
    entity_id: str,
    entity_type: str,
    capacities: list[str],
    *,
    director_count: int | None = None,
    director_count_fact_ids: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "id": entity_id,
        "entity_type": entity_type,
        "capacities": capacities,
        "director_count": director_count,
        "director_count_fact_ids": director_count_fact_ids or [],
    }


def route(
    route_id: str,
    namespace: str,
    path: str,
    *,
    requirement: str = "mandatory",
    verdict: str = "incorporated",
    xor_set_id: str | None = None,
    deciding_fact_ids: list[str] | None = None,
    unresolved: bool = False,
    gap_ids: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "id": route_id,
        "source": {
            "namespace": namespace,
            "path": path,
            "pinpoint": "generic fixture passage",
        },
        "requirement": requirement,
        "verdict": verdict,
        "triggering_fact_ids": ["F_base"],
        "deciding_fact_ids": deciding_fact_ids or [],
        "unique_contribution": f"Unique contribution from {route_id}",
        "xor_set_id": xor_set_id,
        "unresolved": unresolved,
        "gap_ids": gap_ids or [],
    }


def recalculate_counts(plan: dict[str, Any]) -> None:
    instruments = plan["requested_document_chain"]["instruments"]
    included = {"produced", "placeholder"}
    counts = {
        "instruments": len(instruments),
        "operative_components": sum(
            item["status"] in included
            for doc in instruments
            for item in doc["operative_components"]
        ),
        "attachments": sum(
            item["status"] in included
            for doc in instruments
            for item in doc["attachments"]
        ),
        "execution_blocks": sum(doc["execution"]["status"] in included for doc in instruments),
        "records_filings": sum(
            item["status"] in included
            for doc in instruments
            for item in doc["records_filings"]
        ),
    }
    plan["requested_document_chain"]["expected_counts"] = counts
    plan["requested_document_chain"]["actual_counts"] = copy.deepcopy(counts)


def rebuild_indexes(plan: dict[str, Any]) -> None:
    namespace_paths = {
        "exam_question": set(),
        "exam_attachment": set(),
        "course_manual": set(),
        "course_appendix": set(),
    }
    allowlist: list[dict[str, str]] = []
    actual_open: list[dict[str, str]] = []
    forbidden: list[str] = []
    traces: list[dict[str, str]] = []
    for item in plan["routes"]:
        source = item["source"]
        namespace_paths[source["namespace"]].add(source["path"])
        if item["verdict"] == "forbidden":
            forbidden.append(source["path"])
        elif item["verdict"] in {"incorporated", "conditional"}:
            role = item["verdict"]
            allowlist.append({
                "path": source["path"],
                "namespace": source["namespace"],
                "role": role,
            })
            if item["verdict"] == "incorporated":
                actual_open.append({
                    "path": source["path"],
                    "namespace": source["namespace"],
                    "role": "incorporated",
                    "sha256": digest(source["path"]),
                })
        traces.append({
            "id": f"T_{item['id']}",
            "route_id": item["id"],
            "contribution": item["unique_contribution"],
            "answer_location": f"planned answer or private trace location for {item['id']}",
        })
    plan["namespaces"] = {
        key: sorted(value)
        for key, value in namespace_paths.items()
    }
    plan["source_access"]["allowlist"] = allowlist
    plan["source_access"]["allowlist_sha256"] = hashlib.sha256(
        json_bytes(allowlist)
    ).hexdigest()
    plan["source_access"]["actual_open"] = actual_open
    plan["source_access"]["forbidden_paths"] = sorted(set(forbidden))
    plan["final_trace"] = traces


def base_plan(plan_id: str, case_ref: str, mode: str = "DRAFTING") -> dict[str, Any]:
    plan: dict[str, Any] = {
        "schema_version": "route-plan-v1",
        "plan_id": plan_id,
        "case_refs": [case_ref],
        "answer_unit": {
            "id": "Unit_main",
            "mode": mode,
            "question_ref": "inputs/question.json",
            "mcq_options": [],
        },
        "namespaces": {},
        "locks": {},
        "facts": [
            {
                "id": "F_base",
                "kind": "general",
                "subject_id": None,
                "value": True,
                "text": "The supplied question fixes the generic requested outcome.",
                "material": True,
                "disposition": "used - outcome",
            }
        ],
        "claims": [],
        "entities": [entity("E_human", "human", ["signatory"])],
        "routes": [
            route("R_question", "exam_question", "inputs/question.json"),
            route("R_rule", "course_manual", "course/generic-rule.md"),
        ],
        "source_access": {
            "allowlist_frozen": True,
            "allowlist_sha256": "0" * 64,
            "allowlist": [],
            "actual_open": [],
            "forbidden_paths": [],
            "prior_answer_paths": ["forbidden/prior-answer.md"],
        },
        "xor_branch_sets": [],
        "requested_document_chain": {
            "required": mode == "DRAFTING",
            "complex_transaction": False,
            "instruments": [],
            "expected_counts": {},
            "actual_counts": {},
        },
        "materials_gaps": [],
        "final_trace": [],
        "render_gate": {"status": "not_rendered", "validation_report": None},
    }
    for name in (
        "jurisdiction",
        "regime_entity",
        "legal_actor_capacity",
        "transaction_relationship",
        "lifecycle_stage",
        "governing_instruments",
    ):
        plan["locks"][name] = {
            "state": "supplied",
            "value": f"generic supplied {name}",
            "deciding_fact_ids": ["F_base"],
            "alternatives": [],
        }
    rebuild_indexes(plan)
    recalculate_counts(plan)
    return plan


def json_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def action_notice_clean() -> dict[str, Any]:
    plan = base_plan("Fixture_action_notice_clean", "S01")
    plan["routes"].append(route("R_action", "course_appendix", "course/action-precedent.md"))
    selected = ["Action_commence", "Action_appoint", "Action_audit"]
    plan["requested_document_chain"]["instruments"] = [
        instrument(
            "I_notice",
            1,
            "notice",
            "E_human",
            action_business=True,
            selected_action_ids=selected,
            components=[component(f"C_{name}", name) for name in selected],
        )
    ]
    rebuild_indexes(plan)
    recalculate_counts(plan)
    return plan


def managed_borrowing_clean() -> dict[str, Any]:
    plan = base_plan("Fixture_managed_borrowing_clean", "S02")
    plan["entities"] = [
        entity("E_owner", "human", ["beneficial_owner", "signatory"]),
        entity("E_member", "corporate", ["corporate_member"]),
        entity("E_director", "corporate", ["corporate_director"]),
    ]
    plan["requested_document_chain"]["complex_transaction"] = True
    plan["requested_document_chain"]["instruments"] = [
        instrument("I_instruction", 1, "agreement", "E_owner", components=[component("C_instruction")]),
        instrument("I_member_authority", 2, "upstream_authority", "E_member", components=[component("C_member_authority")]),
        instrument(
            "I_member_resolution",
            3,
            "resolution",
            "E_member",
            target_company_act=True,
            upstream_id="I_member_authority",
            components=[component("C_member_approval")],
        ),
        instrument("I_director_authority", 4, "upstream_authority", "E_director", components=[component("C_director_authority")]),
        instrument(
            "I_complex_resolution",
            5,
            "resolution",
            "E_director",
            target_company_act=True,
            upstream_id="I_director_authority",
            components=[component("C_complex_approval")],
            attachments=[
                attachment("A_conveyance", "conveyance_bill_of_sale"),
                attachment("A_facility", "facility"),
                attachment("A_security", "security"),
                attachment("A_registry", "registry"),
            ],
            records=[record("RF_charge_register", "register_of_charges")],
        ),
    ]
    recalculate_counts(plan)
    return plan


def transfer_unresolved_clean() -> dict[str, Any]:
    plan = base_plan("Fixture_transfer_unresolved_clean", "P05B", mode="PROSE")
    plan["routes"].extend([
        route(
            "R_approval",
            "course_appendix",
            "course/approval.md",
            requirement="optional",
            verdict="conditional",
            xor_set_id="X_transfer_decision",
        ),
        route(
            "R_refusal",
            "course_appendix",
            "course/refusal.md",
            requirement="optional",
            verdict="conditional",
            xor_set_id="X_transfer_decision",
        ),
    ])
    plan["xor_branch_sets"] = [{
        "id": "X_transfer_decision",
        "route_ids": ["R_approval", "R_refusal"],
        "selection_state": "unresolved",
        "selected_route_ids": [],
        "deciding_fact_ids": [],
    }]
    rebuild_indexes(plan)
    recalculate_counts(plan)
    return plan


def final_completion_clean() -> dict[str, Any]:
    plan = base_plan("Fixture_final_completion_clean", "P08A", mode="PROSE")
    plan["facts"].append({
        "id": "F_completion_method",
        "kind": "branch_decision",
        "subject_id": None,
        "value": "final meeting",
        "text": "The supplied procedure selects one completion method.",
        "material": True,
        "disposition": "used - outcome",
    })
    plan["routes"].extend([
        route(
            "R_final_meeting",
            "course_appendix",
            "course/final-meeting.md",
            requirement="optional",
            verdict="incorporated",
            xor_set_id="X_completion",
            deciding_fact_ids=["F_completion_method"],
        ),
        route(
            "R_written_approval",
            "course_appendix",
            "course/written-approval.md",
            requirement="optional",
            verdict="conditional",
            xor_set_id="X_completion",
        ),
    ])
    plan["xor_branch_sets"] = [{
        "id": "X_completion",
        "route_ids": ["R_final_meeting", "R_written_approval"],
        "selection_state": "selected",
        "selected_route_ids": ["R_final_meeting"],
        "deciding_fact_ids": ["F_completion_method"],
    }]
    rebuild_indexes(plan)
    recalculate_counts(plan)
    return plan


def source_access_clean() -> dict[str, Any]:
    plan = base_plan("Fixture_source_access_clean", "MCQ17", mode="MCQ")
    plan["answer_unit"]["mcq_options"] = ["A", "B", "C", "D"]
    plan["claims"] = [
        {
            "id": f"Claim_{letter}",
            "kind": "mcq_option",
            "option": letter,
            "text": f"Generic option {letter}",
            "disposition": "supported" if letter == "C" else "refuted",
        }
        for letter in "ABCD"
    ]
    plan["routes"].append(
        route(
            "R_forbidden",
            "course_appendix",
            "course/forbidden-comparator.md",
            requirement="optional",
            verdict="forbidden",
        )
    )
    plan["requested_document_chain"]["required"] = False
    rebuild_indexes(plan)
    recalculate_counts(plan)
    return plan


def entity_count_clean() -> dict[str, Any]:
    plan = base_plan("Fixture_entity_count_clean", "S02")
    plan["facts"].append({
        "id": "F_director_count",
        "kind": "director_count",
        "subject_id": "E_provider",
        "value": 1,
        "text": "The question expressly supplies the director count.",
        "material": True,
        "disposition": "supported",
    })
    plan["entities"] = [
        entity(
            "E_provider",
            "corporate",
            ["corporate_director"],
            director_count=1,
            director_count_fact_ids=["F_director_count"],
        )
    ]
    plan["requested_document_chain"]["instruments"] = [
        instrument("I_provider_authority", 1, "upstream_authority", "E_provider", components=[component("C_provider_authority")])
    ]
    recalculate_counts(plan)
    return plan


def gap_clean() -> dict[str, Any]:
    plan = base_plan("Fixture_gap_clean", "P08B", mode="PROSE")
    plan["materials_gaps"] = [{
        "id": "G_form",
        "description": "The course does not supply the exact generic form.",
        "resolution": "conditional",
        "affected_ids": ["R_gap"],
    }]
    plan["routes"].append(
        route(
            "R_gap",
            "course_appendix",
            "course/incomplete-form.md",
            requirement="optional",
            verdict="conditional",
            unresolved=True,
            gap_ids=["G_form"],
        )
    )
    rebuild_indexes(plan)
    recalculate_counts(plan)
    return plan


def mutate(plan: dict[str, Any], plan_id: str, operation: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    result = copy.deepcopy(plan)
    result["plan_id"] = plan_id
    operation(result)
    return result


def all_fixtures() -> dict[str, dict[str, Any]]:
    action = action_notice_clean()
    managed = managed_borrowing_clean()
    transfer = transfer_unresolved_clean()
    completion = final_completion_clean()
    sources = source_access_clean()
    counts = entity_count_clean()
    gaps = gap_clean()

    def action_missing(plan: dict[str, Any]) -> None:
        notice = plan["requested_document_chain"]["instruments"][0]
        notice["operative_components"] = notice["operative_components"][:1]
        recalculate_counts(plan)

    def missing_upstream(plan: dict[str, Any]) -> None:
        plan["requested_document_chain"]["instruments"] = [
            item for item in plan["requested_document_chain"]["instruments"]
            if item["id"] != "I_member_authority"
        ]
        member = next(item for item in plan["requested_document_chain"]["instruments"] if item["id"] == "I_member_resolution")
        member["upstream_authority_instrument_id"] = None
        member["signatory"]["authority_instrument_id"] = None
        recalculate_counts(plan)

    def missing_attachment(kind: str) -> Callable[[dict[str, Any]], None]:
        def operation(plan: dict[str, Any]) -> None:
            resolution = next(item for item in plan["requested_document_chain"]["instruments"] if item["id"] == "I_complex_resolution")
            resolution["attachments"] = [item for item in resolution["attachments"] if item["kind"] != kind]
            recalculate_counts(plan)
        return operation

    def missing_charge_register(plan: dict[str, Any]) -> None:
        resolution = next(item for item in plan["requested_document_chain"]["instruments"] if item["id"] == "I_complex_resolution")
        resolution["records_filings"] = []
        recalculate_counts(plan)

    def hard_approval(plan: dict[str, Any]) -> None:
        plan["xor_branch_sets"][0]["selection_state"] = "selected"
        plan["xor_branch_sets"][0]["selected_route_ids"] = ["R_approval"]
        next(item for item in plan["routes"] if item["id"] == "R_approval")["verdict"] = "incorporated"
        rebuild_indexes(plan)

    def cumulative_completion(plan: dict[str, Any]) -> None:
        branch = plan["xor_branch_sets"][0]
        branch["selected_route_ids"] = ["R_final_meeting", "R_written_approval"]
        next(item for item in plan["routes"] if item["id"] == "R_written_approval")["verdict"] = "incorporated"
        rebuild_indexes(plan)

    def unselected_incorporated_completion(plan: dict[str, Any]) -> None:
        next(item for item in plan["routes"] if item["id"] == "R_written_approval")["verdict"] = "incorporated"
        rebuild_indexes(plan)

    def forbidden_open(plan: dict[str, Any]) -> None:
        path = "course/forbidden-comparator.md"
        entry = {"path": path, "namespace": "course_appendix", "role": "check_only"}
        plan["source_access"]["allowlist"].append(entry)
        plan["source_access"]["actual_open"].append({**entry, "sha256": digest(path)})

    def prior_open(plan: dict[str, Any]) -> None:
        path = "forbidden/prior-answer.md"
        plan["namespaces"]["exam_question"].append(path)
        entry = {"path": path, "namespace": "exam_question", "role": "check_only"}
        plan["source_access"]["allowlist"].append(entry)
        plan["source_access"]["actual_open"].append({**entry, "sha256": digest(path)})

    def incorporated_not_opened(plan: dict[str, Any]) -> None:
        plan["source_access"]["actual_open"] = [
            item for item in plan["source_access"]["actual_open"]
            if item["path"] != "course/generic-rule.md"
        ]

    def access_role_mismatch(plan: dict[str, Any]) -> None:
        target = next(
            item for item in plan["source_access"]["actual_open"]
            if item["path"] == "course/generic-rule.md"
        )
        target["role"] = "check_only"

    def unsupported_count(plan: dict[str, Any]) -> None:
        provider = plan["entities"][0]
        provider["director_count_fact_ids"] = []

    def unresolved_gap_removed(plan: dict[str, Any]) -> None:
        gap_route = next(item for item in plan["routes"] if item["id"] == "R_gap")
        gap_route["verdict"] = "incorporated"
        gap_route["gap_ids"] = []
        rebuild_indexes(plan)

    return {
        "action-notice.clean.json": action,
        "action-notice.missing-operatives.fail.json": mutate(action, "Fixture_action_notice_missing_operatives", action_missing),
        "managed-borrowing.clean.json": managed,
        "managed-borrowing.missing-upstream.fail.json": mutate(managed, "Fixture_managed_missing_upstream", missing_upstream),
        "managed-borrowing.missing-bill-of-sale.fail.json": mutate(managed, "Fixture_managed_missing_bill", missing_attachment("conveyance_bill_of_sale")),
        "managed-borrowing.missing-complex-attachment.fail.json": mutate(managed, "Fixture_managed_missing_attachment", missing_attachment("facility")),
        "managed-borrowing.missing-charge-register.fail.json": mutate(managed, "Fixture_managed_missing_charge_register", missing_charge_register),
        "transfer-unresolved.clean.json": transfer,
        "transfer-unresolved.hard-approval.fail.json": mutate(transfer, "Fixture_transfer_hard_approval", hard_approval),
        "final-completion.clean.json": completion,
        "final-completion.cumulative.fail.json": mutate(completion, "Fixture_completion_cumulative", cumulative_completion),
        "final-completion.unselected-incorporated.fail.json": mutate(completion, "Fixture_completion_unselected_incorporated", unselected_incorporated_completion),
        "source-access.clean.json": sources,
        "source-access.forbidden-open.fail.json": mutate(sources, "Fixture_source_forbidden_open", forbidden_open),
        "source-access.incorporated-not-opened.fail.json": mutate(sources, "Fixture_source_incorporated_not_opened", incorporated_not_opened),
        "source-access.prior-answer-open.fail.json": mutate(sources, "Fixture_source_prior_open", prior_open),
        "source-access.role-mismatch.fail.json": mutate(sources, "Fixture_source_role_mismatch", access_role_mismatch),
        "entity-count.clean.json": counts,
        "entity-count.unsupported.fail.json": mutate(counts, "Fixture_entity_count_unsupported", unsupported_count),
        "materials-gap.clean.json": gaps,
        "materials-gap.unconditional.fail.json": mutate(gaps, "Fixture_gap_unconditional", unresolved_gap_removed),
    }
