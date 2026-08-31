#!/usr/bin/env python3
"""Build and freeze the 20-item synthetic Section A regression corpus."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "routing-v2/corpus"


def verdict(verdict_: str, reason: str) -> dict[str, str]:
    return {"verdict": verdict_, "reason": reason}


def source(filename: str, pinpoint: str, rationale: str) -> dict[str, str]:
    return {"source": filename, "pinpoint": pinpoint, "rationale": rationale}


def question(
    id_: str,
    pair: str,
    change: str,
    stem: str,
    polarity: str,
    qualifiers: list[str],
    options: dict[str, str],
    answer: str,
    proposition: str,
    must_open: list[str],
    conditional: list[str],
    must_not_open: list[str],
    option_verdicts: dict[str, dict[str, str]],
    closest_two: list[str],
    distinction: str,
    rationale: list[dict[str, str]],
    confidence: str,
) -> dict:
    return {
        "id": id_,
        "pair_id": pair,
        "single_fact_change_from_pair": change,
        "stem": stem,
        "polarity": polarity,
        "qualifiers": qualifiers,
        "options": options,
        "gold": {
            "correct_letter": answer,
            "governing_proposition": proposition,
            "must_open": must_open,
            "conditional": conditional,
            "must_not_open": must_not_open,
            "option_by_option_verdict": option_verdicts,
            "closest_two": closest_two,
            "critical_distinction": distinction,
            "exact_course_source_rationale": rationale,
            "expected_confidence": confidence,
        },
    }


QUESTIONS = [
    question(
        "MCQ01", "MP01", "Traditional articles in MCQ01; BVI BC distribution regime in MCQ02.",
        "AB Ltd has traditional articles reproducing Appendix 1B article 23.1. It has distributable profits and proposes a final cash dividend. Which document route must be used?",
        "correct", ["must"],
        {
            "A": "Appendix 19A board recommendation followed by Appendix 19B members' declaration.",
            "B": "Appendix 19C board-only declaration.",
            "C": "Appendix 20E director-authorised solvency distribution.",
            "D": "Appendices 20B and 20D shareholder-loan repayment.",
        },
        "A", "Traditional article 23.1 requires board recommendation followed by members' declaration, which cannot exceed the recommendation.",
        ["Course-Manual-Module-06-Equity-Capital-and-Distributions.md §§6.1-6.2", "Course-Manual-Module-10-Company-Decision-making-Procedures.md §5.7", "Appendix-1B-Articles-of-Association-based-upon-Table-A-1948-Act-with.md art.23.1", "Appendix-19A-Directors-resolution-to-recommend-payment-of-a-dividend.md", "Appendix-19B-Members-resolution-to-declare-and-pay-a-dividend.md"],
        ["Appendix-19C-Directors-resolution-to-declare-and-pay-dividend.md only if the actual articles confer board-only power"],
        ["Appendix-20E-Directors-resolution-to-distribute-from-IBC-with-statement.md", "Appendix-20B-Demand-for-partial-repayment-of-beneficial-owner-loan.md", "Appendix-20D-Directors-resolution-to-repay-in-part-beneficial-owner-loan.md"],
        {
            "A": verdict("supported", "Supplies both required organs and stages."),
            "B": verdict("refuted", "Board-only power belongs to a different article route."),
            "C": verdict("refuted", "Uses the solvency-distribution regime, not traditional article 23.1."),
            "D": verdict("refuted", "Repayment of debt is not a dividend."),
        },
        ["A", "B"], "Whether the actual articles require two organs or confer board-only power.",
        [
            source("Course-Manual-Module-06-Equity-Capital-and-Distributions.md", "§6.1", "States that article 23.1 requires two resolutions and identifies Appendices 19A and 19B."),
            source("Course-Manual-Module-10-Company-Decision-making-Procedures.md", "§5.7", "Repeats the recommendation/declaration procedure."),
            source("Appendix-19A-Directors-resolution-to-recommend-payment-of-a-dividend.md and Appendix-19B-Members-resolution-to-declare-and-pay-a-dividend.md", "operative resolutions", "The first recommends; the second declares and pays."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ02", "MP01", "BVI BC distribution regime in MCQ02; traditional articles in MCQ01.",
        "AB Ltd is a BVI BC governed by the BVI Business Companies Act 2004. It has distributable funds and proposes the same final cash payment to its member. Which document route must be used?",
        "correct", ["must"],
        {
            "A": "Appendix 19A board recommendation followed by Appendix 19B members' declaration.",
            "B": "Appendix 19C board-only declaration.",
            "C": "Appendix 20E director-authorised solvency distribution.",
            "D": "Appendices 20B and 20D shareholder-loan repayment.",
        },
        "C", "A BVI BC distribution is authorised by directors subject to the statutory solvency test and a resolution stating their opinion.",
        ["Course-Manual-Module-06-Equity-Capital-and-Distributions.md §7.3", "Course-Manual-Module-10-Company-Decision-making-Procedures.md §5.8", "Appendix-20E-Directors-resolution-to-distribute-from-IBC-with-statement.md"],
        ["Actual memorandum/articles", "Course-Manual-Module-08-Directors-Part-II-Powers-and-Duties.md if care or improper payment is raised"],
        ["Appendix-19A-Directors-resolution-to-recommend-payment-of-a-dividend.md as governing route", "Appendix-19B-Members-resolution-to-declare-and-pay-a-dividend.md as governing route", "Appendix-20B-Demand-for-partial-repayment-of-beneficial-owner-loan.md absent a loan"],
        {
            "A": verdict("refuted", "Imports the traditional two-organ procedure."),
            "B": verdict("partly true but not best", "It is board-only but lacks the BVI distribution/solvency resolution route."),
            "C": verdict("supported", "Matches the BVI distribution and solvency requirements."),
            "D": verdict("refuted", "Presupposes an existing shareholder debt."),
        },
        ["B", "C"], "Both are board-only, but only Appendix 20E records the BVI solvency condition and authorises a distribution.",
        [
            source("Course-Manual-Module-06-Equity-Capital-and-Distributions.md", "§7.3", "Distinguishes BVI distributions and requires reasonable solvency grounds plus a statement in the resolution."),
            source("Course-Manual-Module-10-Company-Decision-making-Procedures.md", "§5.8", "Assigns the distribution decision to directors."),
            source("Appendix-20E-Directors-resolution-to-distribute-from-IBC-with-statement.md", "recitals and resolutions", "Contains financial review, solvency declaration and operative distribution."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ03", "MP02", "Voluntary sale by living holder in MCQ03; death and personal-representative election in MCQ04.",
        "A living registered shareholder voluntarily sells issued shares to a buyer, and the articles require board approval. Which route is correct?",
        "correct", [],
        {
            "A": "Appendix 26 plus a new Appendix 27A or 27B nominee instrument.",
            "B": "Appendix 18E with probate evidence.",
            "C": "Appendix 16C allotment and issue resolution.",
            "D": "Appendix 18A transfer form followed by Appendix 18B board approval and register/certificate updates.",
        },
        "D", "A voluntary inter vivos legal-title transfer uses a transfer instrument, required board approval, registration and certificate updates.",
        ["Course-Manual-Module-06-Equity-Capital-and-Distributions.md §5.1", "Course-Manual-Module-10-Company-Decision-making-Procedures.md §5.3", "Appendix-18A-Share-transfer-form.md", "Appendix-18B-Directors-resolution-authorising-share-transfer.md", "Actual transfer articles"],
        ["Appendix-18C-Directors-resolution-refusing-to-register-share-transfer.md and Appendix-18D-Notice-of-refusal-to-register-share-transfer.md if the board refuses", "Appendix-7A-Register-of-members.md and Appendix-16D-Share-certificate.md if the records are requested"],
        ["Appendix-18E-Request-of-personal-representative-to-be-registered-as.md", "Appendix-26-Irrevocable-instruction-to-transfer-beneficial-ownership.md", "Appendix-16C-Directors-resolution-to-allot-and-issue-new-shares.md"],
        {
            "A": verdict("refuted", "Changes beneficial ownership while leaving the nominee registered."),
            "B": verdict("refuted", "Is triggered by death and transmission."),
            "C": verdict("refuted", "Creates new shares rather than moving existing shares."),
            "D": verdict("supported", "Matches a voluntary legal-title transfer with board approval."),
        },
        ["B", "D"], "Voluntary disposition by a living holder versus transmission following death.",
        [
            source("Course-Manual-Module-06-Equity-Capital-and-Distributions.md", "§5.1", "Sets out the transfer form, board decision, registration and certificate stages."),
            source("Appendix-18A-Share-transfer-form.md and Appendix-18B-Directors-resolution-authorising-share-transfer.md", "operative provisions", "The transferor transfers and requests registration; the board approves and orders register/certificate changes."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ04", "MP02", "Death and personal-representative election in MCQ04; voluntary sale in MCQ03.",
        "The registered shareholder has died, and the personal representative elects to be registered in the deceased's place. Which route is correct?",
        "correct", [],
        {
            "A": "Appendix 26 plus a new Appendix 27A or 27B nominee instrument.",
            "B": "Appendix 18E with death and probate evidence.",
            "C": "Appendix 16C allotment and issue resolution.",
            "D": "Appendix 18A transfer form followed by Appendix 18B board approval and register/certificate updates.",
        },
        "B", "Death causes transmission by operation of law; a personal representative electing registration supplies death/probate evidence and the Appendix 18E request.",
        ["Course-Manual-Module-06-Equity-Capital-and-Distributions.md §5.2", "Appendix-1B-Articles-of-Association-based-upon-Table-A-1948-Act-with.md arts.8.6-8.8", "Appendix-18E-Request-of-personal-representative-to-be-registered-as.md"],
        ["Course-Manual-Module-10-Company-Decision-making-Procedures.md §5.3 for consequent records", "Appendix-18A-Share-transfer-form.md if the personal representative instead transfers directly to heirs"],
        ["Appendix-16C-Directors-resolution-to-allot-and-issue-new-shares.md", "Appendix-26-Irrevocable-instruction-to-transfer-beneficial-ownership.md", "Appendix-18B-Directors-resolution-authorising-share-transfer.md as the primary trigger"],
        {
            "A": verdict("refuted", "Is a beneficial-only nominee route."),
            "B": verdict("supported", "Matches transmission and the stated election for personal registration."),
            "C": verdict("refuted", "Is the wrong lifecycle stage."),
            "D": verdict("partly true but not best", "A personal representative may transfer to heirs, but that is not the election stated."),
        },
        ["B", "D"], "The personal representative's stated election determines registration versus direct transfer to heirs.",
        [
            source("Course-Manual-Module-06-Equity-Capital-and-Distributions.md", "§5.2", "Defines transmission by operation of law and gives the personal representative two elections."),
            source("Appendix-18E-Request-of-personal-representative-to-be-registered-as.md", "request and enclosures", "Requests personal registration and attaches the share certificate and grant of probate."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ05", "MP03", "Registered nominee stays in MCQ05; registered nominee is replaced in MCQ06.",
        "The beneficial owner transfers only the beneficial interest to a new client; the same nominee remains the registered shareholder. Which statement is incorrect?",
        "incorrect", ["only"],
        {
            "A": "The Appendix 26 and new Appendix 27A or 27B route is sufficient for the title change described.",
            "B": "The beneficial-owner register and FATCA/CRS records may require updating.",
            "C": "The register of members must be changed to replace the nominee.",
            "D": "A share transfer form is needed only if legal title also moves.",
        },
        "C", "If the nominee remains registered holder, legal title and the register of members do not change; beneficial-owner and nominee records do.",
        ["Course-Manual-Module-10-Company-Decision-making-Procedures.md §5.3", "Course-Manual-Module-11-Company-Management-Services-and-Beneficial-Owner-Control.md §2.5", "Appendix-26-Irrevocable-instruction-to-transfer-beneficial-ownership.md", "Appendix-27A-Nominee-shareholder-agreement.md or Appendix-27B-Nominee-shareholder-declaration.md"],
        ["Appendix-7D-Register-of-beneficial-owners.md"],
        ["Appendix-18A-Share-transfer-form.md as the operative route", "Appendix-18E-Request-of-personal-representative-to-be-registered-as.md"],
        {
            "A": verdict("supported", "Matches a beneficial-only transfer with continuing nominee title."),
            "B": verdict("supported", "The course instruction expressly calls for consequential BO/FATCA/CRS updates."),
            "C": verdict("refuted", "The registered nominee is unchanged, so the register of members does not replace it."),
            "D": verdict("supported", "The legal-title transfer route activates only if the registered holder changes."),
        },
        ["A", "C"], "Whether legal title and the register of members move.",
        [
            source("Course-Manual-Module-10-Company-Decision-making-Procedures.md", "§5.3", "Separates a beneficial-only change from the registered-share transfer route."),
            source("Appendix-26-Irrevocable-instruction-to-transfer-beneficial-ownership.md", "instruction and endorsement", "Leaves shares with the nominee while replacing the nominee instrument and updating BO/FATCA/CRS records."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ06", "MP03", "Registered nominee is replaced in MCQ06; nominee stays in MCQ05.",
        "The beneficial owner arranges for the nominee to cease being registered holder and for legal title to pass to the buyer. Which statement is incorrect?",
        "incorrect", ["only"],
        {
            "A": "The Appendix 26 and new Appendix 27A or 27B route is sufficient for the title change described.",
            "B": "The beneficial-owner register and FATCA/CRS records may require updating.",
            "C": "The register of members must be changed to replace the nominee.",
            "D": "A share transfer form is needed only if legal title also moves.",
        },
        "A", "Once legal title moves, the beneficial-only nominee route is insufficient; the legal transfer and register-of-members route is required.",
        ["Course-Manual-Module-06-Equity-Capital-and-Distributions.md §5.1", "Course-Manual-Module-10-Company-Decision-making-Procedures.md §5.3", "Appendix-18A-Share-transfer-form.md", "Appendix-18B-Directors-resolution-authorising-share-transfer.md"],
        ["Appendix-18C-Directors-resolution-refusing-to-register-share-transfer.md and Appendix-18D-Notice-of-refusal-to-register-share-transfer.md if approval is refused", "Beneficial-owner records"],
        ["Appendix-26-Irrevocable-instruction-to-transfer-beneficial-ownership.md as a standalone substitute"],
        {
            "A": verdict("refuted", "The registered holder changes, so a beneficial-only route is insufficient."),
            "B": verdict("supported", "Beneficial-owner records may also change."),
            "C": verdict("supported", "Legal ownership requires replacement in the register."),
            "D": verdict("supported", "The stated condition for a share transfer form is satisfied."),
        },
        ["A", "C"], "Whether the registered holder changes.",
        [
            source("Course-Manual-Module-06-Equity-Capital-and-Distributions.md", "§5.1", "Explains that legal ownership passes through the transfer/registration process."),
            source("Appendix-18A-Share-transfer-form.md and Appendix-18B-Directors-resolution-authorising-share-transfer.md", "operative provisions", "Request and order replacement in the register and certificate chain."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ07", "MP04", "Restrictive company objects are defective in MCQ07; director authority is defective in MCQ08.",
        "The directors were otherwise properly authorised, but the proposed transaction falls outside the company's restrictive objects. Which source route is not contradicted by the course materials?",
        "not contradicted", [],
        {
            "A": "Corporate capacity under Module 5 section 2.4 is primary; director authority under Module 8 is conditional.",
            "B": "Shareholder reserve power under Module 7 section 2 is primary.",
            "C": "Meeting procedure under Module 10 alone governs.",
            "D": "Director authority under Module 8 section 1.3 is primary; capacity is merely conditional.",
        },
        "A", "Capacity asks whether the company can undertake the transaction; authority asks whether a director or agent can bind it.",
        ["Course-Manual-Module-05-The-Companys-Constitution.md §2.4"],
        ["Course-Manual-Module-08-Directors-Part-II-Powers-and-Duties.md §§1.2-1.3 for external enforceability and internal director liability", "Actual statutory template"],
        ["Meeting appendices as a substitute for capacity analysis"],
        {
            "A": verdict("supported", "The stated defect is in the company's capacity."),
            "B": verdict("refuted", "Addresses a different allocation-of-power issue."),
            "C": verdict("refuted", "Procedure does not answer capacity."),
            "D": verdict("refuted", "Reverses the primary and conditional issues."),
        },
        ["A", "D"], "Which legal person or actor lacks power: the company itself or the director.",
        [
            source("Course-Manual-Module-05-The-Companys-Constitution.md", "§2.4", "Defines company capacity by reference to objects and separately discusses modern external effect and internal liability."),
        ],
        "high (9/10)",
    ),
    question(
        "MCQ08", "MP04", "Director authority is defective in MCQ08; company capacity is defective in MCQ07.",
        "The transaction is within the company's objects, but the individual director exceeded authority conferred by the articles. Which source route is not contradicted by the course materials?",
        "not contradicted", [],
        {
            "A": "Corporate capacity under Module 5 section 2.4 is primary; director authority under Module 8 is conditional.",
            "B": "Shareholder reserve power under Module 7 section 2 is primary.",
            "C": "Meeting procedure under Module 10 alone governs.",
            "D": "Director authority under Module 8 section 1.3 is primary; capacity is merely conditional.",
        },
        "D", "The primary question is the director's authority and outsider-protection rules; company capacity is not defective on the facts.",
        ["Course-Manual-Module-08-Directors-Part-II-Powers-and-Duties.md §§1.2-1.3"],
        ["Course-Manual-Module-05-The-Companys-Constitution.md §2.4 to confirm capacity", "Course-Manual-Module-10-Company-Decision-making-Procedures.md if a specific internal irregularity is alleged"],
        ["Constitutional-amendment appendices as the primary route"],
        {
            "A": verdict("refuted", "Reverses the stated defect."),
            "B": verdict("refuted", "Addresses a different issue."),
            "C": verdict("refuted", "Procedure alone does not determine authority or outsider protection."),
            "D": verdict("supported", "Matches the director-authority defect."),
        },
        ["A", "D"], "Which legal person or actor lacks power: the company itself or the director.",
        [
            source("Course-Manual-Module-08-Directors-Part-II-Powers-and-Duties.md", "§§1.2-1.3", "Separates lack of director power/procedural irregularity from company capacity and preserves external-enforceability and internal-liability questions."),
        ],
        "high (9/10)",
    ),
    question(
        "MCQ09", "MP05", "Traditional article 80 management power in MCQ09; express shareholder reserve power in MCQ10.",
        "The board refuses a proposed acquisition. The company's management article is the unmodified 1948/Table A article 80 form reproduced in Appendix 1B article 19.1. All propositions are incorrect EXCEPT:",
        "except", ["always"],
        {
            "A": "Shareholders may always bind the board by ordinary resolution.",
            "B": "Shareholders cannot presently bind the board; they must first alter the articles if they wish to control this director power.",
            "C": "Shareholders may direct the board by special resolution under an existing reserve power and use Appendix 21G.",
            "D": "Share ownership alone displaces the board's management power.",
        },
        "B", "Under the traditional article 80 form, powers vested in directors cannot be usurped by member direction; members must alter the articles.",
        ["Course-Manual-Module-07-Directors-Part-I-Role-Appointment-and-Removal-of-Directors.md §2.2", "Appendix-1B-Articles-of-Association-based-upon-Table-A-1948-Act-with.md art.19.1"],
        ["Course-Manual-Module-05-The-Companys-Constitution.md §5 for the amendment route", "Course-Manual-Module-08-Directors-Part-II-Powers-and-Duties.md if the acquisition itself is challenged"],
        ["Appendix-21G-Members-resolution-instructing-board-to-enter.md as presently applicable", "Appendix-16A-Members-resolution-to-authorise-the-board-to-allot-and.md"],
        {
            "A": verdict("refuted", "The absolute qualifier and ordinary threshold are wrong."),
            "B": verdict("supported", "States the traditional allocation and amendment route."),
            "C": verdict("refuted", "Assumes a reserve power absent from the stated articles."),
            "D": verdict("refuted", "Confuses ownership with management authority."),
        },
        ["B", "C"], "The exact management article determines whether an existing special-resolution reserve power exists.",
        [
            source("Course-Manual-Module-07-Directors-Part-I-Role-Appointment-and-Removal-of-Directors.md", "§2.2", "States that under the traditional form shareholders cannot give binding instructions and must alter the articles."),
            source("Appendix-1B-Articles-of-Association-based-upon-Table-A-1948-Act-with.md", "art.19.1", "Vests residual management power in directors."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ10", "MP05", "Express shareholder reserve power in MCQ10; traditional article 80 in MCQ09.",
        "The board refuses the same acquisition, but the articles reproduce the 1985/2008 shareholder reserve power in Appendix 1C article 4. All propositions are incorrect EXCEPT:",
        "except", ["always", "may"],
        {
            "A": "Shareholders may always bind the board by ordinary resolution.",
            "B": "Shareholders cannot presently bind the board; they must first alter the articles if they wish to control this director power.",
            "C": "Shareholders may direct the board by special resolution under an existing reserve power and use Appendix 21G.",
            "D": "Share ownership alone displaces the board's management power.",
        },
        "C", "Where the articles expressly reserve it, members may direct specified director action by special resolution.",
        ["Course-Manual-Module-07-Directors-Part-I-Role-Appointment-and-Removal-of-Directors.md §2.2", "Appendix-1C-Articles-of-Association-based-upon-English-2008-Model.md arts.3-4", "Appendix-21G-Members-resolution-instructing-board-to-enter.md"],
        ["Course-Manual-Module-08-Directors-Part-II-Powers-and-Duties.md for continuing director duties", "Course-Manual-Module-11-Company-Management-Services-and-Beneficial-Owner-Control.md §3.6 if beneficial-owner control is raised"],
        ["Appendix-16A-Members-resolution-to-authorise-the-board-to-allot-and.md", "Appendix-21G-Members-resolution-instructing-board-to-enter.md without first verifying the reserve article"],
        {
            "A": verdict("refuted", "Uses the wrong threshold and an absolute qualifier."),
            "B": verdict("refuted", "No prior amendment is needed where the reserve power already exists."),
            "C": verdict("supported", "Matches the express special-resolution reserve power."),
            "D": verdict("refuted", "Ownership alone still does not displace management power."),
        },
        ["B", "C"], "The exact management article determines whether the special-resolution reserve power already exists.",
        [
            source("Course-Manual-Module-07-Directors-Part-I-Role-Appointment-and-Removal-of-Directors.md", "§2.2", "Explains the modern special-resolution reserve power."),
            source("Appendix-1C-Articles-of-Association-based-upon-English-2008-Model.md", "art.4", "Expressly permits shareholders by special resolution to direct specified action."),
            source("Appendix-21G-Members-resolution-instructing-board-to-enter.md", "operative resolution", "Implements the reserve-power route."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ11", "MP06", "Address changes within the same jurisdiction in MCQ11; domicile changes to another jurisdiction in MCQ12.",
        "The company will move its registered office to a new street address within the same jurisdiction. Which route must be opened first?",
        "correct", ["must"],
        {
            "A": "Appendices 13A and 13B public-to-private re-registration.",
            "B": "Module 4 section 2 and Appendices 10A to 10C migration.",
            "C": "Appendix 31D reinstatement.",
            "D": "Module 5 section 3.2, Module 10 section 5.4, and Appendix 12 address-move resolution.",
        },
        "D", "Moving an address within the jurisdiction is a registered-office change, not a change of nationality or domicile.",
        ["Course-Manual-Module-05-The-Companys-Constitution.md §3.2", "Course-Manual-Module-10-Company-Decision-making-Procedures.md §5.4", "Appendix-12-Board-resolution-to-change-location-of-registered-office.md"],
        ["Course-Manual-Module-09-Other-Officers-Secretary-and-Registered-Agent.md §2 if registered-agent records/actions are raised"],
        ["Appendix-10A-Resolution-of-board-to-migrate-company-by-way-of.md", "Appendix-10B-Resolution-of-members-to-migrate.md", "Appendix-10C-Affidavit-in-support-of-application-to-migrate.md", "Appendix-13A-Board-resolutions-to-re-register-as-a-private-company.md", "Appendix-31D-Application-for-administrative-reinstatement-to-register.md"],
        {
            "A": verdict("refuted", "Changes company type rather than address."),
            "B": verdict("refuted", "Changes domicile rather than street address."),
            "C": verdict("refuted", "Restores a struck company."),
            "D": verdict("supported", "Matches an intra-jurisdiction office move."),
        },
        ["B", "D"], "Street address within one jurisdiction versus domicile/nationality across jurisdictions.",
        [
            source("Course-Manual-Module-05-The-Companys-Constitution.md", "§3.2", "Distinguishes an intra-jurisdiction office move from migration."),
            source("Course-Manual-Module-10-Company-Decision-making-Procedures.md", "§5.4", "Gives the board resolution, notice and records steps."),
            source("Appendix-12-Board-resolution-to-change-location-of-registered-office.md", "operative resolutions", "Authorises the address change and records update."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ12", "MP06", "Domicile changes to another jurisdiction in MCQ12; address stays within one jurisdiction in MCQ11.",
        "The same company instead proposes to move its domicile, governing law, and registered office from State A to State B by continuance. Which route must be opened first?",
        "correct", ["must"],
        {
            "A": "Appendices 13A and 13B public-to-private re-registration.",
            "B": "Module 4 section 2 and Appendices 10A to 10C migration.",
            "C": "Appendix 31D reinstatement.",
            "D": "Module 5 section 3.2, Module 10 section 5.4, and Appendix 12 address-move resolution.",
        },
        "B", "Changing domicile without liquidating the entity is migration/continuance and uses the migration approval/evidence route.",
        ["Course-Manual-Module-04-Registration-and-Migration-of-Foreign-Companies.md §2", "Appendix-10A-Resolution-of-board-to-migrate-company-by-way-of.md", "Appendix-10B-Resolution-of-members-to-migrate.md", "Appendix-10C-Affidavit-in-support-of-application-to-migrate.md"],
        ["Course-Manual-Module-05-The-Companys-Constitution.md §5 for new articles", "Actual laws of both jurisdictions", "Course-Manual-Module-10-Company-Decision-making-Procedures.md §§2-4"],
        ["Appendix-12-Board-resolution-to-change-location-of-registered-office.md as a substitute", "Appendix-13A-Board-resolutions-to-re-register-as-a-private-company.md", "Appendix-31D-Application-for-administrative-reinstatement-to-register.md"],
        {
            "A": verdict("refuted", "Changes company type rather than domicile."),
            "B": verdict("supported", "Matches continuation to another jurisdiction."),
            "C": verdict("refuted", "Is a restoration route."),
            "D": verdict("refuted", "Cannot alter nationality or domicile."),
        },
        ["B", "D"], "Street address within one jurisdiction versus domicile/nationality across jurisdictions.",
        [
            source("Course-Manual-Module-04-Registration-and-Migration-of-Foreign-Companies.md", "§§2.1-2.3", "Describes de-registration, continuation filings and continuity of the entity."),
            source("Appendix-10A-Resolution-of-board-to-migrate-company-by-way-of.md, Appendix-10B-Resolution-of-members-to-migrate.md and Appendix-10C-Affidavit-in-support-of-application-to-migrate.md", "approval and evidence chain", "Supply the standard board/member approvals and supporting evidence."),
        ],
        "high (9/10)",
    ),
    question(
        "MCQ13", "MP07", "Board allocation only in MCQ13; consideration and registration completed in MCQ14.",
        "The board has resolved to allocate 500 unissued shares to an identified applicant for stated consideration, but payment has not yet been received and the register has not been updated. Which is the only accurate classification?",
        "correct", ["only"],
        {"A": "Allotment.", "B": "Transfer.", "C": "Issue.", "D": "Transmission."},
        "A", "Allotment occurs when the board resolves who receives how many shares for what consideration.",
        ["Course-Manual-Module-06-Equity-Capital-and-Distributions.md §1.2.2", "Appendix-16C-Directors-resolution-to-allot-and-issue-new-shares.md"],
        ["Course-Manual-Module-10-Company-Decision-making-Procedures.md §5.9", "Course-Manual-Module-05-The-Companys-Constitution.md capital/authority passages", "Appendix-16A-Members-resolution-to-authorise-the-board-to-allot-and.md if directors lack authority"],
        ["Appendix-18A-Share-transfer-form.md", "Appendix-18E-Request-of-personal-representative-to-be-registered-as.md"],
        {
            "A": verdict("supported", "The board has reached the allocation decision."),
            "B": verdict("refuted", "A transfer moves existing shares."),
            "C": verdict("refuted", "Receipt/registration for the issue stage has not occurred."),
            "D": verdict("refuted", "Transmission arises by operation of law."),
        },
        ["A", "C"], "Board allocation versus receipt of consideration and register entry.",
        [
            source("Course-Manual-Module-06-Equity-Capital-and-Distributions.md", "§1.2.2 stages 4-5", "Separates allotment at the board allocation from issue after consideration and registration."),
            source("Appendix-16C-Directors-resolution-to-allot-and-issue-new-shares.md", "operative stages", "Records the board decision and later payment/register actions."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ14", "MP07", "Consideration and registration completed in MCQ14; board allocation only in MCQ13.",
        "The board has resolved to allocate the same 500 shares; payment has now been received and the allottee entered in the register as legal owner. Which is the only accurate classification of the completed stage?",
        "correct", ["only"],
        {"A": "Allotment.", "B": "Transfer.", "C": "Issue.", "D": "Transmission."},
        "C", "Shares are issued when consideration is received and the allottee becomes legal owner through register entry.",
        ["Course-Manual-Module-06-Equity-Capital-and-Distributions.md §1.2.2", "Appendix-16C-Directors-resolution-to-allot-and-issue-new-shares.md"],
        ["Appendix-16D-Share-certificate.md if a certificate is required"],
        ["Appendix-18A-Share-transfer-form.md", "Appendix-18E-Request-of-personal-representative-to-be-registered-as.md"],
        {
            "A": verdict("partly true but not best", "Allotment occurred earlier; the question asks for the completed stage."),
            "B": verdict("refuted", "No existing share moved from one holder to another."),
            "C": verdict("supported", "Consideration and register entry complete the issue stage."),
            "D": verdict("refuted", "No operation-of-law trigger exists."),
        },
        ["A", "C"], "Board allocation versus receipt of consideration and register entry.",
        [
            source("Course-Manual-Module-06-Equity-Capital-and-Distributions.md", "§1.2.2 stage 5", "States that issue occurs on receipt of consideration and register entry establishing legal ownership."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ15", "MP08", "Internal administrative functions in MCQ15; shareholder meeting representation in MCQ16.",
        "The board appoints an officer to maintain statutory registers, prepare notices and agendas, and take minutes. Which pairing is the only correct one?",
        "correct", ["only"],
        {
            "A": "Registered agent; Appendix 24A.",
            "B": "Company secretary; Appendix 24A, with Appendix 24C if the delegated role description is required.",
            "C": "Corporate director; Appendices 21A and 21B.",
            "D": "Corporate representative; Appendices 25H and 25J.",
        },
        "B", "The stated internal administrative functions are company-secretary responsibilities; Appendix 24A appoints and may incorporate Appendix 24C.",
        ["Course-Manual-Module-09-Other-Officers-Secretary-and-Registered-Agent.md §§1.2-1.4", "Appendix-24A-Directors-resolution-appointing-a-secretary.md", "Appendix-24C-Role-and-responsibilities-of-secretary.md"],
        ["Course-Manual-Module-10-Company-Decision-making-Procedures.md for meeting procedure", "Appendix-24B-Directors-resolution-removing-secretary-and-variation.md only for removal/resignation"],
        ["Appendix-25H-Directors-resolution-to-appoint-corporate.md", "Appendix-25J-Notice-to-company-of-appointment-of-corporate.md", "Appendix-21B-Subscribers-resolution-appointing-first-director-s.md"],
        {
            "A": verdict("refuted", "Appendix 24A is not a registered-agent appointment precedent."),
            "B": verdict("supported", "Matches the office, appointing actor and role schedule."),
            "C": verdict("refuted", "Is a different office and appointment route."),
            "D": verdict("refuted", "Is limited to representation of a corporate shareholder at a meeting."),
        },
        ["A", "B"], "Local statutory-agent compliance function versus internal company-secretary administration.",
        [
            source("Course-Manual-Module-09-Other-Officers-Secretary-and-Registered-Agent.md", "§§1.2-1.4", "Identifies board appointment and the secretary's records, notices, agendas and minutes functions."),
            source("Appendix-24A-Directors-resolution-appointing-a-secretary.md and Appendix-24C-Role-and-responsibilities-of-secretary.md", "appointment and role schedule", "Appoint the secretary and enumerate the delegated responsibilities."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ16", "MP08", "Shareholder meeting representation in MCQ16; internal administrative functions in MCQ15.",
        "A corporate shareholder appoints an individual solely to attend, speak, and vote for it at AB Ltd's general meeting. Which pairing is the only correct one?",
        "correct", ["only"],
        {
            "A": "Registered agent; Appendix 24A.",
            "B": "Company secretary; Appendix 24A, with Appendix 24C if the delegated role description is required.",
            "C": "Corporate director; Appendices 21A and 21B.",
            "D": "Corporate representative; Appendices 25H and 25J.",
        },
        "D", "A corporate shareholder's meeting representative is appointed by its board and notified to the investee company.",
        ["Course-Manual-Module-10-Company-Decision-making-Procedures.md §2.4", "Appendix-25H-Directors-resolution-to-appoint-corporate.md", "Appendix-25J-Notice-to-company-of-appointment-of-corporate.md"],
        ["Actual articles", "Appendix-25F-Open-proxy.md or Appendix-25G-Specific-proxy.md only if the shareholder chooses a proxy route"],
        ["Appendix-24A-Directors-resolution-appointing-a-secretary.md", "Appendix-24C-Role-and-responsibilities-of-secretary.md", "Appendix-21B-Subscribers-resolution-appointing-first-director-s.md"],
        {
            "A": verdict("refuted", "Registered-agent functions are unrelated."),
            "B": verdict("refuted", "A secretary does not thereby exercise the shareholder's vote."),
            "C": verdict("refuted", "This is not a director appointment."),
            "D": verdict("supported", "Matches the corporate-representative appointment and notice chain."),
        },
        ["B", "D"], "Internal attendance/minuting by a secretary versus exercising a corporate shareholder's meeting rights.",
        [
            source("Course-Manual-Module-10-Company-Decision-making-Procedures.md", "§2.4", "Distinguishes proxies and corporate representatives and identifies the 25H/25J chain."),
            source("Appendix-25H-Directors-resolution-to-appoint-corporate.md and Appendix-25J-Notice-to-company-of-appointment-of-corporate.md", "appointment and notice", "The shareholder's board appoints; notice is delivered to the company."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ17", "MP09", "Assets/liabilities remain in MCQ17; zero-state eligibility in MCQ18.",
        "A solvent company has assets to realise and liabilities to pay before surplus can be returned to members. Which route may properly be initiated to terminate it?",
        "correct", ["may"],
        {
            "A": "Voluntary striking off under Appendix 31A plus the jurisdictionally applicable Appendix 31B or 31C.",
            "B": "Administrative reinstatement under Appendix 31D.",
            "C": "Members' voluntary winding-up beginning with Appendices 30A and 30B and continuing through the applicable notices/final-account chain.",
            "D": "Compulsory winding-up solely because the members no longer want the company.",
        },
        "C", "A solvent company with affairs to wind up uses the members' voluntary liquidation sequence, including solvency, member decision, realisation/payment and final account.",
        ["Course-Manual-Module-12-Termination-of-Companies.md §3.1", "Appendix-30A-Directors-declaration-of-solvency.md", "Appendix-30B-Members-resolution-to-voluntarily-wind-up-the-company.md", "Applicable Appendices 30C-30G by stage"],
        ["Course-Manual-Module-10-Company-Decision-making-Procedures.md meeting/written-resolution procedure", "Actual IBC allocation of liquidation powers"],
        ["Appendix-31A-Directors-resolution-to-apply-for-voluntary-striking-off.md as a substitute", "Appendix-31D-Application-for-administrative-reinstatement-to-register.md"],
        {
            "A": verdict("refuted", "The company does not satisfy the zero-state conditions."),
            "B": verdict("refuted", "Reinstatement reverses termination."),
            "C": verdict("supported", "Matches a solvent company whose affairs still require liquidation."),
            "D": verdict("refuted", "The stated desire does not itself supply a compulsory ground."),
        },
        ["A", "C"], "Remaining assets/liabilities require liquidation rather than the zero-state striking-off route.",
        [
            source("Course-Manual-Module-12-Termination-of-Companies.md", "§3.1", "Gives the declaration, member decision, liquidator, notices, account and dissolution sequence."),
            source("Appendix-30A-Directors-declaration-of-solvency.md and Appendix-30B-Members-resolution-to-voluntarily-wind-up-the-company.md", "opening stages", "Supply solvency evidence and commence the members' voluntary winding-up."),
        ],
        "high (10/10)",
    ),
    question(
        "MCQ18", "MP09", "Zero-state eligibility in MCQ18; assets/liabilities remain in MCQ17.",
        "The same jurisdiction permits voluntary striking off, and the company now has no assets, liabilities, claims, proceedings, or business. Which route may properly be initiated to terminate it?",
        "correct", ["may", "best"],
        {
            "A": "Voluntary striking off under Appendix 31A plus the jurisdictionally applicable Appendix 31B or 31C.",
            "B": "Administrative reinstatement under Appendix 31D.",
            "C": "Members' voluntary winding-up beginning with Appendices 30A and 30B and continuing through the applicable notices/final-account chain.",
            "D": "Compulsory winding-up solely because the members no longer want the company.",
        },
        "A", "A qualifying zero-state company may use voluntary striking off, beginning with the board decision and the jurisdictionally applicable filing route.",
        ["Course-Manual-Module-12-Termination-of-Companies.md §6.2", "Appendix-31A-Directors-resolution-to-apply-for-voluntary-striking-off.md", "Appendix-31B-Application-for-voluntary-striking-off-example-of.md or Appendix-31C-Statutory-declaration-of-compliance-in-support-of-voluntary.md according to jurisdiction"],
        ["Actual jurisdiction's availability and conditions"],
        ["Appendix-31B-Application-for-voluntary-striking-off-example-of.md and Appendix-31C-Statutory-declaration-of-compliance-in-support-of-voluntary.md automatically together", "Appendix-31D-Application-for-administrative-reinstatement-to-register.md", "Winding-up appendices as mandatory"],
        {
            "A": verdict("supported", "Matches the expressly available zero-state route."),
            "B": verdict("refuted", "Runs in the opposite lifecycle direction."),
            "C": verdict("partly true but not best", "Formal liquidation may exist, but it is not the best course route on the supplied zero-state facts."),
            "D": verdict("refuted", "No compulsory ground is supplied."),
        },
        ["A", "C"], "The supplied zero-state facts and statutory availability make striking off the best route rather than formal liquidation.",
        [
            source("Course-Manual-Module-12-Termination-of-Companies.md", "§6.2", "States the no-business/assets/liabilities conditions and jurisdiction-specific alternative filing routes."),
            source("Appendix-31A-Directors-resolution-to-apply-for-voluntary-striking-off.md", "recitals and resolution", "Confirms eligibility and authorises the application."),
        ],
        "high (9/10)",
    ),
    question(
        "MCQ19", "MP10", "Bilateral agreement requested in MCQ19; unilateral declaration requested in MCQ20.",
        "The parties want a bilateral nominee shareholder agreement between the registered nominee and beneficial owner. Which is the best-supported course-material route?",
        "best", [],
        {
            "A": "Appendix 26 alone is a complete nominee agreement.",
            "B": "Open Appendix 27B, report that 'etc., as above' leaves operative provisions missing, and do not invent them.",
            "C": "Appendix 18A is the nominee agreement because shares are involved.",
            "D": "Appendix 27A is the bilateral source, but its terms must be adapted and must not be represented as universally complete.",
        },
        "D", "Appendix 27A is the bilateral nominee/beneficial-owner instrument; it must be adapted within the course-material boundary.",
        ["Course-Manual-Module-11-Company-Management-Services-and-Beneficial-Owner-Control.md §2.5", "Appendix-27A-Nominee-shareholder-agreement.md"],
        ["Appendix-26-Irrevocable-instruction-to-transfer-beneficial-ownership.md when an existing beneficial interest is transferred", "Beneficial-owner records"],
        ["Appendix-18A-Share-transfer-form.md as a nominee substitute", "Outside-law boilerplate"],
        {
            "A": verdict("refuted", "Appendix 26 is a transfer instruction, not a complete bilateral agreement."),
            "B": verdict("partly true but not best", "Accurately handles the unilateral source, but the requested form is bilateral."),
            "C": verdict("refuted", "Appendix 18A transfers legal title."),
            "D": verdict("supported", "Matches the bilateral requested form and preserves adaptation limits."),
        },
        ["B", "D"], "Bilateral agreement versus unilateral declaration, with the latter facially incomplete.",
        [
            source("Course-Manual-Module-11-Company-Management-Services-and-Beneficial-Owner-Control.md", "§2.5", "Identifies 27A as the agreement and 27B as an alternative one-party declaration."),
            source("Appendix-27A-Nominee-shareholder-agreement.md", "parties and operative clauses", "Names both parties and states holding, disposal, distribution and voting obligations."),
        ],
        "high (9/10)",
    ),
    question(
        "MCQ20", "MP10", "Unilateral declaration requested in MCQ20; bilateral agreement requested in MCQ19.",
        "The client instead requests a complete unilateral nominee shareholder declaration. Which is the best-supported course-material route?",
        "best", [],
        {
            "A": "Appendix 26 alone is a complete nominee agreement.",
            "B": "Open Appendix 27B, report that 'etc., as above' leaves operative provisions missing, and do not invent them.",
            "C": "Appendix 18A is the nominee agreement because shares are involved.",
            "D": "Appendix 27A is the bilateral source, but its terms must be adapted and must not be represented as universally complete.",
        },
        "B", "Appendix 27B is the relevant unilateral form but is facially incomplete; the course-grounded response is to expose the gap and not supply missing wording.",
        ["Course-Manual-Module-11-Company-Management-Services-and-Beneficial-Owner-Control.md §2.5", "Appendix-27B-Nominee-shareholder-declaration.md"],
        ["Appendix-27A-Nominee-shareholder-agreement.md only to understand the referenced categories, not as automatic completion of the unilateral deed"],
        ["Outside law", "Invented boilerplate", "Appendix-18A-Share-transfer-form.md"],
        {
            "A": verdict("refuted", "Wrong instrument and form."),
            "B": verdict("supported", "Matches the unilateral form and accurately preserves its materials gap."),
            "C": verdict("refuted", "Is a legal-title transfer instrument."),
            "D": verdict("partly true but not best", "Is substantively fuller but bilateral rather than the requested unilateral form."),
        },
        ["B", "D"], "Bilateral completeness versus unilateral form match with a disclosed materials gap.",
        [
            source("Course-Manual-Module-11-Company-Management-Services-and-Beneficial-Owner-Control.md", "§2.5", "Confirms the declaration as the unilateral alternative but does not supply omitted language."),
            source("Appendix-27B-Nominee-shareholder-declaration.md", "operative clause 1", "Contains only 'Hold the Shares ... etc., as above' and an execution block, so a complete declaration cannot be reproduced from the course source."),
        ],
        "high (10/10) for identifying the gap; low (4/10 or below) for any purported complete verbatim declaration",
    ),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    gold = {
        "schema": "section-a-synthetic-gold-v1",
        "frozen_on": "2026-08-30",
        "status": "synthetic regression corpus; not an official paper or exam-accuracy measure",
        "official_section_a_holdout": "absent; a future official paper must be tested unseen",
        "source_boundary": "Course manuals, appendices, Syllabus, question facts and examination attachments only; no external law.",
        "questions": QUESTIONS,
    }
    fixture_questions = [
        {
            "id": item["id"],
            "pair_id": item["pair_id"],
            "single_fact_change_from_pair": item["single_fact_change_from_pair"],
            "stem": item["stem"],
            "polarity": item["polarity"],
            "qualifiers": item["qualifiers"],
            "options": item["options"],
        }
        for item in QUESTIONS
    ]
    fixture = {
        "schema": "section-a-synthetic-question-fixture-v1",
        "status": "synthetic regression corpus; contains no gold fields",
        "questions": fixture_questions,
    }

    gold_path = OUT / "mcq-20-gold.json"
    fixture_path = OUT / "mcq-20-questions.json"
    gold_path.write_text(json.dumps(gold, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    fixture_path.write_text(json.dumps(fixture, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    letters = [item["gold"]["correct_letter"] for item in QUESTIONS]
    counts = {letter: letters.count(letter) for letter in "ABCD"}
    freeze = f"""# Section A Synthetic Corpus Freeze Record

- Frozen: 2026-08-30, before any baseline or candidate answer run.
- Scope: 20 synthetic MCQs in 10 one-fact minimal pairs.
- Gold fields: correct letter, governing proposition, must-open, conditional,
  must-not-open, option dispositions, closest-two distinction, exact course-source
  rationale and expected confidence.
- Answer balance: {counts}.
- Official status: synthetic regression only. No official Section A holdout is present;
  passing this corpus must not be described as real-exam accuracy.
- Gold SHA-256: `{sha256(gold_path)}`
- Question-only fixture SHA-256: `{sha256(fixture_path)}`

The question-only fixture contains no gold fields and is the sole question input for
blind answer agents. The gold file is released only to the independent evaluator after
all answer files are locked.
"""
    (OUT / "mcq-freeze-record.md").write_text(freeze, encoding="utf-8")
    print(f"wrote {gold_path.relative_to(ROOT)}")
    print(f"wrote {fixture_path.relative_to(ROOT)}")
    print(f"wrote {(OUT / 'mcq-freeze-record.md').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
