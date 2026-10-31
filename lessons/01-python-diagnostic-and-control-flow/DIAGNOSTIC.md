# Lesson 01 diagnostic and concept exemptions

Purpose: locate gaps in an experienced Python/LangGraph developer's independent skills. This is placement, not lesson mastery. FULL COURSE MODE opens with the chapter's professional scenario and decision-table demonstration, then presents A. Ask one coherent task at a time, not a sequence of tiny predictions. No hints before an attempt. If help is needed, record assistance and route to remediation; use a fresh variant before awarding an exemption.

Save attempts to new files under student_work or accept code in chat. Never overwrite older work. The learner can request full instruction instead of placement. No diagnostic outcomes have been recorded by the course author.

## A — Independent filtering with a contract (about 4 minutes)
Implement `ready_ids(tickets)` returning IDs of records whose status is exactly "open" and whose `approved` field is the Boolean True. Preserve input order and input dictionaries. Assume a list of dictionaries with a guaranteed string ticket_id; missing status/approved is not ready. The string "True", the number 1 and other true-like values are not Boolean approval. Empty input returns []. No I/O.

Before submitting, include two self-chosen assertions, one checking a misleading true-like value. Explain why your condition matches the contract. The teaching example uses different fields and rules. A loop or comprehension is acceptable; do not require both if one is clear and correct.

Observable checks: open/True included; open/False excluded; closed/True excluded; open/"True" and open/1 excluded; absent approval excluded; empty list; order/non-mutation. A correct answer without execution is marked reasoning demonstrated, execution pending, not invented passing tests.

## B — Overlap and guard reasoning (about 2 minutes)
A separate policy returns "EXPEDITE" when urgency >= 4 AND impact >= 4, "NORMAL" if either score >= 3, otherwise "BACKLOG". Both are validated integers 1..5. Explain what goes wrong if the NORMAL condition is checked first, identify one overlapping boundary input, and write the corrected decision sequence yourself. Explain how a guard would protect this logic if inputs were untrusted. Do not show the learner a solution before their response.

This diagnostic uses abstract decision labels; the final assignment requires a separate independent implementation and malformed-input tests. Seeing a worked diagnostic answer does not earn an exemption.

## C — Batch exit and collection design (about 2 minutes)
Inspect the faulty preview in labs/buggy_preview.py. Explain which records the function processes for its three-ticket demonstration and what empty input returns. Describe why each exit belongs to a different scope and whether a comprehension would simplify the corrected preview. Predict first; run if available. Do not fix it for the learner. A correct explanation can exempt a refresher but the debugging implementation/regression remains required for final mastery.

## Evidence-to-section skip map
| Evidence demonstrated independently | Instruction that may be skipped | What remains |
| --- | --- | --- |
| A: correct filtering, strict Boolean semantics, order, own assertions and explanation | §2 elementary comparisons/truthiness; §5 basic iteration/list-comprehension refresher; guided stage 1 prediction | Apply validation/partition rules in independent work |
| B: overlap input, correct ordered logic and guard explanation | §3 branch-order/guard refresher | Explain worked scenario precedence and its changed requirement |
| A + B: explicit handling of missing/type-invalid inputs before unsafe comparisons | §4 elementary lookup/type refresher | Lab-specific domains/boundaries and final validation tests |
| C: accurate trace including empty input and scope explanation | §5 continue/break/return refresher | Independently fix faulty preview and add regression tests |
| A+B+C all independent, code/tests executed and clear explanations | Guided repetition may be bypassed; instructor gives worked scenario architecture review then independent assignment | Debugging regression, conceptual checks, final code/tests and fresh modification |

Do not skip an entire section based on a guessed output or prior project names. Unexecuted but correct chat reasoning can skip repeated explanation provisionally; record execution pending and require later tests. Partial answers receive narrow remediation (e.g., truthiness only, not a whole restart). If A/B/C evidence is mixed, teach only the uncovered subsection at full depth, then give an adjacent new application.

## Record format for actual use
Task / attempt path or chat evidence / independent or assistance / assertions and actual execution status / concepts demonstrated / sections exempted or pending / narrow gap / next section. Append these facts to a real session checkpoint only after the learner performs them. A course upgrade does not create diagnostic evidence.
