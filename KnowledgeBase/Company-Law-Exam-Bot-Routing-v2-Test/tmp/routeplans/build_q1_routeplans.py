#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXAM = "exam-inputs/Specimen-Paper-1.pdf"
M10 = "Course-Manual-Module-10-Company-Decision-making-Procedures.md"
M12 = "Course-Manual-Module-12-Termination-of-Companies.md"
A25D = "Appendix-25D-Notice-of-AGM.md"
A25E = "Appendix-25E-Notice-of-general-meeting-to-pass-a-specific.md"
A30A = "Appendix-30A-Directors-declaration-of-solvency.md"
A30B = "Appendix-30B-Members-resolution-to-voluntarily-wind-up-the-company.md"
A30C = "Appendix-30C-Notice-of-winding-up-for-publication-in-press-and-Gazette.md"
SOURCE_SHA = {
    EXAM: "06dc9ab27f0bad1ffad543f84ee645a0af07aa0095075ff43b5cba90d7c11f66",
    M10: "99613860d1e48fb2230a549ac577b2884d9073aa580ede3c2298ba32026ae4dc",
    M12: "1246d3259c6aac6149ed68e0f87a44c002871d246fddd147cb90be92adaa603c",
    A25E: "c1eed42e361819d8173cc313c4b93c5e0214117c49c1f3d94b4a926a3054a85d",
    A30A: "22620cc72d2774905249b0f1b6cf55a8d654c738005dec4dcd64727adce22bb0",
    A30B: "9b6f085d5f7a68b3d4f6488e612fc50dfa47bd47e1ce7fe6adfb011dcb58c9f4",
}


def h(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def lock(state, value, facts=(), alternatives=()):
    return {"state": state, "value": value, "deciding_fact_ids": list(facts), "alternatives": list(alternatives)}


def fact(fid, kind, text, value, disposition="used - content", subject=None, material=True):
    return {"id": fid, "kind": kind, "subject_id": subject, "value": value, "text": text,
            "material": material, "disposition": disposition}


def route(rid, namespace, path, pinpoint, verdict, contribution, triggers, requirement="mandatory",
          deciding=(), xor=None, unresolved=False, gaps=()):
    return {"id": rid, "source": {"namespace": namespace, "path": path, "pinpoint": pinpoint},
            "requirement": requirement, "verdict": verdict, "triggering_fact_ids": list(triggers),
            "deciding_fact_ids": list(deciding), "unique_contribution": contribution,
            "xor_set_id": xor, "unresolved": unresolved, "gap_ids": list(gaps)}


def empty_chain():
    counts = {"instruments": 0, "operative_components": 0, "attachments": 0,
              "execution_blocks": 0, "records_filings": 0}
    return {"required": False, "complex_transaction": False, "instruments": [],
            "expected_counts": counts, "actual_counts": counts}


def entity(eid, entity_type, capacities):
    return {"id": eid, "entity_type": entity_type, "capacities": capacities,
            "director_count": None, "director_count_fact_ids": []}


def build(unit, mode, facts, claims, routes, allowlist, extra_appendices=(), chain=None, gaps=(), xor=()):
    namespaces = {
        "exam_question": [EXAM],
        "exam_attachment": [EXAM],
        "course_manual": sorted({r["source"]["path"] for r in routes if r["source"]["namespace"] == "course_manual"}),
        "course_appendix": sorted(set(extra_appendices) | {r["source"]["path"] for r in routes if r["source"]["namespace"] == "course_appendix"}),
    }
    plan = {
        "schema_version": "route-plan-v1",
        "plan_id": f"specimen1.q1.{unit}.v1",
        "case_refs": [],
        "answer_unit": {"id": f"q1.{unit}", "mode": mode, "question_ref": f"Specimen Paper 1 Question 1.{unit}", "mcq_options": []},
        "namespaces": namespaces,
        "locks": {
            "jurisdiction": lock("genuinely_unknown", None, alternatives=["Unidentified jurisdiction; use supplied legislation threshold and actual articles only"]),
            "regime_entity": lock("supplied", "Company Ltd governed procedurally by supplied articles", ["f.entity"]),
            "legal_actor_capacity": lock("supplied", facts[1]["text"], ["f.actor"]),
            "transaction_relationship": lock("supplied", facts[2]["text"], ["f.relationship"]),
            "lifecycle_stage": lock("supplied", facts[3]["text"], ["f.lifecycle"]),
            "governing_instruments": lock("supplied", "Applicable companies legislation threshold plus examination Appendix 1 articles", ["f.governing"]),
        },
        "facts": facts,
        "claims": claims,
        "entities": [
            entity("company", "corporate", ["other"]),
            entity("secretary", "human", ["officer", "signatory"]),
            entity("A", "human", ["director"]), entity("B", "human", ["director"]),
            entity("C", "human", ["member"]), entity("D", "human", ["member"]), entity("E", "human", ["member"]),
        ],
        "routes": routes,
        "source_access": {
            "allowlist_frozen": True,
            "allowlist_sha256": h(allowlist),
            "allowlist": allowlist,
            "actual_open": [dict(entry, sha256=SOURCE_SHA[entry["path"]]) for entry in allowlist],
            "forbidden_paths": sorted({r["source"]["path"] for r in routes if r["verdict"] == "forbidden"}),
            "prior_answer_paths": [],
        },
        "xor_branch_sets": list(xor),
        "requested_document_chain": chain or empty_chain(),
        "materials_gaps": list(gaps),
        "final_trace": [
            {"id": f"trace.{r['id']}", "route_id": r["id"], "contribution": r["unique_contribution"],
             "answer_location": f"Question 1.{unit} answer/check trace"}
            for r in routes
        ],
        "render_gate": {"status": "not_rendered", "validation_report": None},
    }
    return plan


common_allow = [
    {"path": EXAM, "namespace": "exam_question", "role": "incorporated"},
    {"path": EXAM, "namespace": "exam_attachment", "role": "incorporated"},
    {"path": M10, "namespace": "course_manual", "role": "incorporated"},
]


def facts_for(unit, actor, relationship, lifecycle, extras):
    rows = [
        fact("f.entity", "regime_entity", "Company Ltd is the company in question", "Company Ltd"),
        fact("f.actor", "actor_capacity", actor, actor),
        fact("f.relationship", "transaction_relationship", relationship, relationship),
        fact("f.lifecycle", "lifecycle_stage", lifecycle, lifecycle),
        fact("f.governing", "governing_instrument", "Applicable legislation supplies a three-quarter threshold unless the articles define a lesser super-majority; examination Appendix 1 is supplied", "legislation and exam Appendix 1"),
        fact("f.holdings", "general", "C, D and E hold 70%, 20% and 10% respectively", "70/20/10"),
        fact("f.date", "general", "The original general meeting is to take place on 28 August", "28 August"),
    ]
    rows.extend(extras)
    return rows


plans = {}

facts11 = facts_for("1", "Company secretary or administrator drafting the Company's meeting notice",
                    "Company convening members to decide voluntary liquidation",
                    "Pre-meeting notice for an extraordinary special general meeting",
                    [fact("f.command", "general", "Draft a notice for the meeting", "draft notice"),
                     fact("f.threshold", "branch_decision", "The supplied articles define a special resolution as two-thirds of votes", "two-thirds"),
                     fact("f.missing", "general", "The question omits the year, time, place and proposed liquidator particulars", "placeholders", "input gap")])
routes11 = [
    route("r.question", "exam_question", EXAM, "Question 1.1, page 2", "incorporated", "Supplies the requested notice, date, parties, holdings, transaction and marks.", ["f.command", "f.date", "f.holdings"]),
    route("r.articles", "exam_attachment", EXAM, "Appendix 1 arts 1, 10.3-10.4, 11.1-11.3, 12.1, 13.7-13.8 and 27.1-27.5", "incorporated", "Controls the meeting type, two-thirds special-resolution threshold, notice content, service period, recipients and proxy mechanics.", ["f.governing", "f.threshold"]),
    route("r.m10", "course_manual", M10, "Sections 2.1-2.4 and 2.8", "incorporated", "Supplies the general-meeting notice and proxy procedure needed to complete the notice.", ["f.command", "f.lifecycle"]),
    route("r.m12", "course_manual", M12, "Section 3.1", "incorporated", "Supplies the members' voluntary winding-up decision sequence and the liquidator-appointment business.", ["f.command", "f.relationship"]),
    route("r.a25e", "course_appendix", A25E, "Complete precedent", "incorporated", "Supplies the exact structure, addressing, special-resolution block, proxy note, board-order line and execution placeholders for the notice.", ["f.command"]),
    route("r.a30a", "course_appendix", A30A, "Complete precedent", "checked_not_relevant", "Confirms the pre-resolution solvency declaration and statement but adds no requested component to the notice on the supplied facts.", ["f.relationship"], requirement="optional"),
    route("r.a30b", "course_appendix", A30B, "Complete precedent", "incorporated", "Supplies every action-specific operative resolution that the meeting notice must set out for the members' voluntary winding-up business.", ["f.command", "f.relationship"]),
    route("r.a25d", "course_appendix", A25D, "Complete precedent", "forbidden", "AGM notice is the wrong meeting and transaction stage.", ["f.lifecycle"], requirement="optional"),
    route("r.a30c", "course_appendix", A30C, "Complete precedent", "forbidden", "Publication notice follows commencement of winding-up and is not the requested meeting notice.", ["f.lifecycle"], requirement="optional"),
]
gap11 = {"id": "gap.notice_particulars", "description": "The paper gives 28 August but no year, time, place, notice date or proposed liquidator particulars.", "resolution": "placeholder", "affected_ids": ["notice.time_place", "notice.resolution2", "notice.execution"]}
chain11 = {
    "required": True, "complex_transaction": False,
    "instruments": [{
        "id": "notice", "sequence": 1, "kind": "notice", "actor_id": "company", "target_company_act": True,
        "upstream_authority_instrument_id": None, "target_instrument": "Notice of extraordinary special general meeting",
        "signatory": {"human": True, "name_or_placeholder": "[Secretary/administrator]", "authority_instrument_id": None},
        "action_business": True, "selected_action_component_ids": [
            "a30b.resolution1", "a30b.resolution2", "a30b.resolution3", "a30b.resolution4", "a30b.resolution5"
        ],
        "operative_components": [
            {"id": "notice.time_place", "source_component_id": "a25e.time_place", "status": "placeholder", "unresolved": True, "gap_ids": ["gap.notice_particulars"]},
            {"id": "notice.resolution1", "source_component_id": "a30b.resolution1", "status": "produced", "unresolved": False, "gap_ids": []},
            {"id": "notice.resolution2", "source_component_id": "a30b.resolution2", "status": "placeholder", "unresolved": True, "gap_ids": ["gap.notice_particulars"]},
            {"id": "notice.resolution3", "source_component_id": "a30b.resolution3", "status": "produced", "unresolved": False, "gap_ids": []},
            {"id": "notice.resolution4", "source_component_id": "a30b.resolution4", "status": "produced", "unresolved": False, "gap_ids": []},
            {"id": "notice.resolution5", "source_component_id": "a30b.resolution5", "status": "produced", "unresolved": False, "gap_ids": []},
            {"id": "notice.proxy", "source_component_id": "a25e.proxy_note", "status": "produced", "unresolved": False, "gap_ids": []},
        ],
        "attachments": [],
        "execution": {"id": "notice.execution", "status": "placeholder", "unresolved": True, "gap_ids": ["gap.notice_particulars"]},
        "records_filings": [],
    }],
    "expected_counts": {"instruments": 1, "operative_components": 7, "attachments": 0, "execution_blocks": 1, "records_filings": 0},
    "actual_counts": {"instruments": 1, "operative_components": 7, "attachments": 0, "execution_blocks": 1, "records_filings": 0},
}
allow11 = common_allow + [
    {"path": M12, "namespace": "course_manual", "role": "incorporated"},
    {"path": A25E, "namespace": "course_appendix", "role": "incorporated"},
    {"path": A30A, "namespace": "course_appendix", "role": "check_only"},
    {"path": A30B, "namespace": "course_appendix", "role": "incorporated"},
]
plans["1"] = build("1", "DRAFTING", facts11,
                   [{"id": "c.notice", "kind": "document_assertion", "option": None, "text": "The notice must reproduce all applicable action business and its execution/proxy structure.", "disposition": "used - content"}],
                   routes11, allow11, [A25D, A25E, A30A, A30B, A30C], chain11, [gap11])


def prose_plan(unit, actor, relationship, lifecycle, extras, claims, route_specs, forbidden):
    fs = facts_for(unit, actor, relationship, lifecycle, extras)
    rs = [
        route("r.question", "exam_question", EXAM, f"Question 1.{unit}, page 2", "incorporated", route_specs[0], ["f.command", "f.date", "f.holdings"]),
        route("r.articles", "exam_attachment", EXAM, route_specs[1], "incorporated", route_specs[2], route_specs[3]),
        route("r.m10", "course_manual", M10, route_specs[4], "incorporated", route_specs[5], route_specs[6]),
        route("r.forbidden", "course_appendix", forbidden, "Complete precedent", "forbidden", route_specs[7], ["f.lifecycle"], requirement="optional"),
    ]
    return build(unit, "PROSE", fs, claims, rs, common_allow, [forbidden])


plans["2"] = prose_plan("2", "Company serving notice through its secretary or administrator",
    "Company to members, directors and any successor entitled through death or bankruptcy",
    "Service before the 28 August meeting",
    [fact("f.command", "general", "State recipients, method and timing of service", "advise service")],
    [{"id": "c.service", "kind": "answer_assertion", "option": None, "text": "Serve the persons named by art 27.5 using an authorised art 27.1 method early enough to give 14 clear days under art 11.1.", "disposition": "used - outcome"}],
    ["Supplies the recipient, method and timing questions and four-mark scope.",
     "Appendix 1 arts 11.1-11.2 and 27.1-27.5", "Controls who receives notice, permitted delivery, deemed service and the 14-clear-day calculation.", ["f.governing", "f.command"],
     "Sections 2.2.2-2.2.6", "Supplies the general-meeting notice period, service and recipient procedure.", ["f.command", "f.lifecycle"],
     "An AGM notice precedent does not answer this prose service question or the special-meeting facts."], A25D)

plans["3"] = prose_plan("3", "Company and meeting participants affected by a notice defect",
    "Validity of proceedings following defective or omitted notice",
    "Validity consequence at and after the 28 August meeting",
    [fact("f.command", "general", "Explain the effect of a failure to give proper notice", "explain effect")],
    [{"id": "c.defect", "kind": "answer_assertion", "option": None, "text": "A non-accidental notice failure invalidates proceedings, while art 11.3 preserves proceedings after accidental omission or non-receipt.", "disposition": "used - outcome"}],
    ["Supplies the notice-defect question and three-mark scope.",
     "Appendix 1 arts 11.1-11.3", "Distinguishes a failure to comply with notice requirements from accidental omission or non-receipt.", ["f.governing", "f.command"],
     "Section 2.2.6", "Supplies the effect of failure to notify and the accidental-omission qualification.", ["f.command"],
     "A meeting-notice drafting precedent does not supply the legal consequence asked for."], A25E)

plans["4"] = prose_plan("4", "C as a 70% member attending alone",
    "Member attendance, original-meeting quorum and adjournment",
    "Original 28 August meeting before any adjournment",
    [fact("f.command", "general", "Decide whether C alone can pass the resolution on 28 August", "apply quorum"),
     fact("f.only_c", "branch_decision", "Only C attends at the appointed time on 28 August", "C alone")],
    [{"id": "c.quorum", "kind": "answer_assertion", "option": None, "text": "C cannot transact business at the original meeting because art 12.2 requires two shareholders personally present.", "disposition": "used - outcome"}],
    ["Supplies C's 70% holding, sole attendance and four-mark scope.",
     "Appendix 1 arts 12.2-12.3", "Controls the two-person original-meeting quorum and the consequence and quorum at the adjourned meeting.", ["f.governing", "f.only_c"],
     "Sections 2.5.1-2.5.3", "Supplies quorum and inquorate-meeting procedure.", ["f.command", "f.only_c"],
     "A winding-up resolution precedent cannot cure the missing quorum at the original meeting."], A30B)

plans["5"] = prose_plan("5", "C, D and E as members voting; C as potential poll demander",
    "Show-of-hands vote followed by a poll demand and share-weighted vote",
    "Voting at the quorate 28 August meeting",
    [fact("f.command", "general", "Determine the show-of-hands result and what C should do", "apply voting"),
     fact("f.attendance", "branch_decision", "C, D and E all attend; D and E vote against on a show of hands", "all attend; D and E against")],
    [{"id": "c.show", "kind": "answer_assertion", "option": None, "text": "The motion loses two votes to one on a show of hands.", "disposition": "used - outcome"},
     {"id": "c.poll", "kind": "answer_assertion", "option": None, "text": "C should demand a poll before or on declaration; C's 70% then exceeds the two-thirds special-resolution threshold.", "disposition": "used - outcome"}],
    ["Supplies the 70/20/10 holdings, attendance, votes and four-mark scope.",
     "Appendix 1 definition of special resolution and arts 12.6-12.10 and 13.1", "Controls one-member-one-vote on hands, the 15% poll-demand threshold, one-vote-per-share on poll and the two-thirds threshold.", ["f.governing", "f.attendance", "f.holdings"],
     "Sections 2.8-2.9", "Supplies motions, special resolutions, show-of-hands voting and polls.", ["f.command", "f.attendance"],
     "A specific proxy precedent is unnecessary because all three registered shareholders attend personally."], "Appendix-25G-Specific-proxy.md")


ROOT.mkdir(parents=True, exist_ok=True)
for unit, plan in plans.items():
    (ROOT / f"q1-{unit}-route-plan.json").write_text(json.dumps(plan, indent=2, ensure_ascii=True) + "\n")
