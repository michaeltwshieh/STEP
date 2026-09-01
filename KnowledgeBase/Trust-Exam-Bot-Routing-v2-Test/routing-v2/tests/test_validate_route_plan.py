#!/usr/bin/env python3
"""Focused regression tests for the Trust-native RoutePlan contract."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = PACKAGE_ROOT / "routing-v2/schema/route-plan.schema.json"
VALIDATOR_PATH = PACKAGE_ROOT / "routing-v2/scripts/validate_route_plan.py"

SPEC = importlib.util.spec_from_file_location("trust_route_validator", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


def allowlist_hash(entries: list[dict[str, str]]) -> str:
    encoded = json.dumps(entries, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


class RoutePlanValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.source_root = Path(self.temporary.name)
        self.question_path = self.source_root / "question.md"
        self.question_path.write_text("Advise the beneficiary under the supplied facts.\n", encoding="utf-8")
        (self.source_root / "SOURCE-MANIFEST.json").write_text(
            json.dumps({"files": {}, "bundle_sha256": hashlib.sha256(b"{}").hexdigest()}),
            encoding="utf-8",
        )
        self.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def classification(self, identifier: str, value: str) -> dict[str, object]:
        return {
            "id": identifier,
            "state": "supplied",
            "value": value,
            "deciding_fact_ids": ["fact1"],
            "alternatives": [],
        }

    def base_plan(self) -> dict[str, object]:
        source_hash = hashlib.sha256(self.question_path.read_bytes()).hexdigest()
        allowlist = [{"path": "question.md", "namespace": "exam_question", "role": "incorporated"}]
        zero_counts = {
            "instruments": 0,
            "operative_components": 0,
            "attachments": 0,
            "execution_blocks": 0,
            "records_filings": 0,
        }
        return {
            "schema_version": "route-plan-v2",
            "plan_id": "plan1",
            "case_refs": [],
            "answer_unit": {
                "id": "unit1",
                "mode": "PROSE",
                "question_ref": "Question 1",
                "subpart_ref": "whole",
                "command_word": "advise",
                "marks": 10,
                "requested_deliverables": ["advice"],
                "polarity": None,
                "mcq_options": [],
                "selected_option": None,
                "closest_options": [],
            },
            "namespaces": {
                "exam_question": ["question.md"],
                "exam_attachment": [],
                "course_manual": [],
                "course_appendix": [],
            },
            "jurisdiction_factors": [
                {
                    **self.classification("jur1", "Cayman Islands"),
                    "kind": "proper_law",
                }
            ],
            "trust_architecture": [self.classification("arch1", "conventional trust")],
            "actor_capacities": [self.classification("actor1", "beneficiary")],
            "power_characteristics": [self.classification("power1", "dispositive discretion")],
            "relationships": [self.classification("relation1", "trustee-beneficiary")],
            "lifecycle_stages": [self.classification("stage1", "administration")],
            "governing_instruments": [self.classification("instrument1", "question facts")],
            "standing": [self.classification("standing1", "beneficiary may request advice")],
            "facts": [
                {
                    "id": "fact1",
                    "kind": "general",
                    "subject_id": "person1",
                    "value": "Cayman Islands",
                    "text": "The supplied facts identify the relevant parties and law.",
                    "material": True,
                    "disposition": "supported",
                }
            ],
            "claims": [
                {
                    "id": "claim1",
                    "kind": "answer_assertion",
                    "option": None,
                    "text": "The requested advice is source-bound.",
                    "disposition": "supported",
                }
            ],
            "entities": [
                {
                    "id": "person1",
                    "entity_type": "human",
                    "capacities": ["beneficiary"],
                    "cardinalities": [],
                }
            ],
            "routes": [
                {
                    "id": "route1",
                    "source": {"namespace": "exam_question", "path": "question.md", "pinpoint": "complete stem"},
                    "requirement": "mandatory",
                    "verdict": "incorporated",
                    "triggering_fact_ids": ["fact1"],
                    "deciding_fact_ids": [],
                    "unique_contribution": "Supplies the facts and requested output.",
                    "deliverable_scope": "requested output",
                    "relationship_set_ids": [],
                    "unresolved": False,
                    "gap_ids": [],
                }
            ],
            "source_access": {
                "allowlist_frozen": True,
                "allowlist_sha256": allowlist_hash(allowlist),
                "allowlist": allowlist,
                "actual_open": [
                    {
                        "path": "question.md",
                        "namespace": "exam_question",
                        "role": "incorporated",
                        "sha256": source_hash,
                    }
                ],
                "forbidden_paths": [],
                "prior_answer_paths": [],
            },
            "route_relationship_sets": [],
            "requested_document_chain": {
                "required": False,
                "complex_transaction": False,
                "instruments": [],
                "expected_counts": copy.deepcopy(zero_counts),
                "actual_counts": copy.deepcopy(zero_counts),
            },
            "materials_gaps": [],
            "final_trace": [
                {
                    "id": "trace1",
                    "route_id": "route1",
                    "contribution": "Supplies the facts and requested output.",
                    "answer_location": "opening analysis",
                }
            ],
            "render_authorization": {
                "decision": "render",
                "input_complete": True,
                "materials_outcome": "answerable",
            },
            "render_gate": {"status": "not_rendered", "validation_report": None},
        }

    def validate(self, plan: dict[str, object]) -> tuple[dict[str, object], int]:
        return VALIDATOR.validate(plan, self.schema, self.source_root)

    def as_mcq(self, plan: dict[str, object], selected: str | None, closest: list[str]) -> None:
        plan["answer_unit"].update(
            {
                "mode": "MCQ",
                "command_word": "best",
                "polarity": "best",
                "mcq_options": ["A", "B"],
                "selected_option": selected,
                "closest_options": closest,
            }
        )
        plan["claims"] = [
            {"id": "a1", "kind": "mcq_subclaim", "option": "A", "text": "A proposition", "disposition": "supported"},
            {"id": "ac", "kind": "mcq_option_conclusion", "option": "A", "text": "A conclusion", "disposition": "supported"},
            {"id": "b1", "kind": "mcq_subclaim", "option": "B", "text": "B proposition", "disposition": "refuted"},
            {"id": "bc", "kind": "mcq_option_conclusion", "option": "B", "text": "B conclusion", "disposition": "refuted"},
        ]

    def failed_codes(self, report: dict[str, object]) -> set[str]:
        return {
            item["code"]
            for item in report["invariants"]
            if item["status"] == "FAIL"
        }

    def test_clean_source_bound_plan_is_valid(self) -> None:
        report, exit_code = self.validate(self.base_plan())
        self.assertEqual(0, exit_code, report["issues"])
        self.assertEqual("VALID", report["status"])

    def test_empty_plan_is_rejected(self) -> None:
        plan = self.base_plan()
        for key in ("facts", "claims", "entities", "routes"):
            plan[key] = []
        report, exit_code = self.validate(plan)
        self.assertEqual(1, exit_code)
        self.assertIn("SCHEMA", {issue["code"] for issue in report["issues"]})

    def test_nonexistent_or_fake_actual_open_is_rejected(self) -> None:
        plan = self.base_plan()
        plan["namespaces"]["exam_question"] = ["ghost.md"]
        plan["routes"][0]["source"]["path"] = "ghost.md"
        plan["source_access"]["allowlist"] = [
            {"path": "ghost.md", "namespace": "exam_question", "role": "incorporated"}
        ]
        plan["source_access"]["allowlist_sha256"] = allowlist_hash(plan["source_access"]["allowlist"])
        plan["source_access"]["actual_open"] = [
            {"path": "ghost.md", "namespace": "exam_question", "role": "incorporated", "sha256": "0" * 64}
        ]
        report, exit_code = self.validate(plan)
        self.assertEqual(1, exit_code)
        self.assertIn("SOURCE_FILE_INTEGRITY", self.failed_codes(report))

    def test_compound_mcq_requires_one_conclusion_per_option(self) -> None:
        plan = self.base_plan()
        plan["answer_unit"].update(
            {
                "mode": "MCQ",
                "command_word": "best",
                "polarity": "best",
                "mcq_options": ["A", "B"],
                "selected_option": "A",
                "closest_options": ["A", "B"],
            }
        )
        plan["claims"] = [
            {"id": "a1", "kind": "mcq_subclaim", "option": "A", "text": "A first proposition", "disposition": "supported"},
            {"id": "ac", "kind": "mcq_option_conclusion", "option": "A", "text": "A conclusion", "disposition": "supported"},
            {"id": "b1", "kind": "mcq_subclaim", "option": "B", "text": "B first proposition", "disposition": "refuted"},
        ]
        report, exit_code = self.validate(plan)
        self.assertEqual(1, exit_code)
        self.assertIn("FACT_CLAIM_DISPOSITIONS", self.failed_codes(report))

    def test_relationship_set_selection_is_enforced(self) -> None:
        plan = self.base_plan()
        plan["routes"][0]["relationship_set_ids"] = ["set1"]
        plan["route_relationship_sets"] = [
            {
                "id": "set1",
                "kind": "AND prerequisite",
                "route_ids": ["route1"],
                "selection_state": "selected",
                "selected_route_ids": [],
                "deciding_fact_ids": ["fact1"],
            }
        ]
        report, exit_code = self.validate(plan)
        self.assertEqual(1, exit_code)
        self.assertIn("RELATIONSHIP_SELECTION", self.failed_codes(report))

    def test_route_can_participate_in_selected_xor_and_sequence_sets(self) -> None:
        plan = self.base_plan()
        route2 = copy.deepcopy(plan["routes"][0])
        route2.update(
            {
                "id": "route2",
                "requirement": "optional",
                "verdict": "conditional",
                "unique_contribution": "Preserves the rejected alternative.",
                "relationship_set_ids": ["choice1"],
            }
        )
        plan["routes"][0]["relationship_set_ids"] = ["choice1", "sequence1"]
        plan["routes"].append(route2)
        plan["route_relationship_sets"] = [
            {
                "id": "choice1",
                "kind": "XOR",
                "route_ids": ["route1", "route2"],
                "selection_state": "selected",
                "selected_route_ids": ["route1"],
                "deciding_fact_ids": ["fact1"],
            },
            {
                "id": "sequence1",
                "kind": "SEQUENCE",
                "route_ids": ["route1"],
                "selection_state": "selected",
                "selected_route_ids": ["route1"],
                "deciding_fact_ids": ["fact1"],
            },
        ]
        plan["final_trace"].append(
            {
                "id": "trace2",
                "route_id": "route2",
                "contribution": "Preserves the rejected alternative.",
                "answer_location": "conditional branch",
            }
        )
        report, exit_code = self.validate(plan)
        self.assertEqual(0, exit_code, report["issues"])

    def test_and_is_unordered_but_sequence_is_ordered(self) -> None:
        plan = self.base_plan()
        route2 = copy.deepcopy(plan["routes"][0])
        route2.update(
            {
                "id": "route2",
                "unique_contribution": "Supplies the prerequisite authority.",
                "relationship_set_ids": ["set1"],
            }
        )
        plan["routes"][0]["relationship_set_ids"] = ["set1"]
        plan["routes"].append(route2)
        plan["final_trace"].append(
            {
                "id": "trace2",
                "route_id": "route2",
                "contribution": "Supplies the prerequisite authority.",
                "answer_location": "authority analysis",
            }
        )
        relationship_set = {
            "id": "set1",
            "kind": "AND prerequisite",
            "route_ids": ["route1", "route2"],
            "selection_state": "selected",
            "selected_route_ids": ["route2", "route1"],
            "deciding_fact_ids": ["fact1"],
        }
        plan["route_relationship_sets"] = [relationship_set]

        report, exit_code = self.validate(plan)
        self.assertEqual(0, exit_code, report["issues"])

        relationship_set["kind"] = "SEQUENCE"
        report, exit_code = self.validate(plan)
        self.assertEqual(1, exit_code)
        self.assertIn("RELATIONSHIP_SELECTION", self.failed_codes(report))

    def test_unresolved_mcq_may_omit_selection_and_closest_options(self) -> None:
        plan = self.base_plan()
        self.as_mcq(plan, None, [])
        plan["render_authorization"] = {
            "decision": "do_not_render",
            "input_complete": True,
            "materials_outcome": "materials do not resolve",
        }
        report, exit_code = self.validate(plan)
        self.assertEqual(0, exit_code, report["issues"])

    def test_null_mcq_selection_is_invalid_when_rendering_is_authorized(self) -> None:
        plan = self.base_plan()
        self.as_mcq(plan, None, [])
        report, exit_code = self.validate(plan)
        self.assertEqual(1, exit_code)
        self.assertIn("FACT_CLAIM_DISPOSITIONS", self.failed_codes(report))

    def test_impossible_entity_capacity_is_rejected(self) -> None:
        plan = self.base_plan()
        plan["entities"][0]["capacities"] = ["corporate_trustee"]
        report, exit_code = self.validate(plan)
        self.assertEqual(1, exit_code)
        self.assertIn("ENTITY_CAPACITY", self.failed_codes(report))

    def test_foundation_allows_additional_valid_capacity(self) -> None:
        plan = self.base_plan()
        plan["entities"][0]["entity_type"] = "foundation"
        plan["entities"][0]["capacities"] = ["foundation", "beneficiary"]
        report, exit_code = self.validate(plan)
        self.assertEqual(0, exit_code, report["issues"])

    def test_checked_route_requires_real_check_only_open(self) -> None:
        plan = self.base_plan()
        plan["routes"][0]["requirement"] = "optional"
        plan["routes"][0]["verdict"] = "checked_not_relevant"
        report, exit_code = self.validate(plan)
        self.assertEqual(1, exit_code)
        self.assertIn("SOURCE_ALLOWLIST", self.failed_codes(report))

    def test_requested_instrument_needs_substantive_content(self) -> None:
        for complex_transaction, execution_status, execution_count in (
            (True, "omitted", 0),
            (False, "produced", 1),
        ):
            with self.subTest(
                complex_transaction=complex_transaction,
                execution_status=execution_status,
            ):
                plan = self.base_plan()
                plan["answer_unit"]["mode"] = "DRAFTING"
                plan["answer_unit"]["command_word"] = "draft"
                plan["requested_document_chain"] = {
                    "required": True,
                    "complex_transaction": complex_transaction,
                    "instruments": [
                        {
                            "id": "draft1",
                            "sequence": 1,
                            "kind": "deed",
                            "actor_id": "person1",
                            "target_act": True,
                            "upstream_authority_instrument_id": None,
                            "target_instrument": "empty deed",
                            "signatories": [{"human": True, "name_or_placeholder": "[name]", "authority_instrument_id": None}],
                            "action_business": False,
                            "selected_action_component_ids": [],
                            "operative_components": [],
                            "attachments": [],
                            "execution": {"id": "execution1", "status": execution_status, "unresolved": False, "gap_ids": []},
                            "records_filings": [],
                        }
                    ],
                    "expected_counts": {"instruments": 1, "operative_components": 0, "attachments": 0, "execution_blocks": execution_count, "records_filings": 0},
                    "actual_counts": {"instruments": 1, "operative_components": 0, "attachments": 0, "execution_blocks": execution_count, "records_filings": 0},
                }
                report, exit_code = self.validate(plan)
                self.assertEqual(1, exit_code)
                self.assertIn("DOCUMENT_COUNT_RECONCILIATION", self.failed_codes(report))

    def test_render_authorization_must_match_gaps(self) -> None:
        plan = self.base_plan()
        plan["render_authorization"]["decision"] = "do_not_render"
        report, exit_code = self.validate(plan)
        self.assertEqual(1, exit_code)
        self.assertIn("RENDER_GATE", self.failed_codes(report))


if __name__ == "__main__":
    unittest.main()
