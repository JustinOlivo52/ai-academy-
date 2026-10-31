# Lesson 01 full-course rebuild audit

## Why the first upgrade still failed the learning goal
The previous Lesson 01 contained about 2,907 words, but the instructor skill explicitly required a 1–3-paragraph opening, one tiny diagnostic, and compressed phone pacing. This delivery path caused the chapter to be replaced by miniature explanation/quiz turns. More text in a file did not solve the architecture problem.

The chapter had useful conditions/loops/validation instruction, but no mapped diagnostic exemptions, no substantial Boolean/truthiness treatment, no guard-clause design section, no comprehension tradeoffs, and no complete realistic ticket decision implementation. Its worked example summed waiting times. Guided practice was a three-item counting exercise without a separate programming lab starter/tests. The independent assignment only summarized urgency; branch overlap and multi-field business policy were not assessed. The debug task was a tiny early-return snippet rather than a reproducible project exercise.

## Rebuild scope
- Root routing and instructor skill now default to FULL COURSE MODE. A meaningful section includes connected explanation, annotated examples and realistic reasoning before a checkpoint. Phone/time context cannot automatically turn it into review. MOBILE REVIEW MODE requires explicit review intent.
- Six substantial chapter sections cover policy tables; Boolean logic/short-circuiting/truthiness; ordered conditions/guards/early returns; validation/boundaries; loops/comprehensions; and a complete support-ticket escalation workflow with trace and executable source.
- DIAGNOSTIC.md supplies independent filtering, overlap/guard reasoning and batch debugging tasks, exact evidence criteria and section exemptions. Strong existing skills skip repetition, not final assessment.
- GUIDED_LAB.md, its interface-only starter and explicit tests create a staged escalation-preview lab. ASSIGNMENT.md adds urgency/impact decisions alongside the unchanged summary v1. A separate intentionally faulty batch fixture and regression suite support debugging.
- Assessment v2 requires independent code, own meaningful tests, conceptual understanding, a corrected debug regression, edge-case evidence and a fresh change. Historical v1 records remain historical; they are never silently relabelled.
- Existing 20-lesson repository and projects remain. Lessons 02–20 are not rewritten. Their future standard now includes diagnostic skipping and substantial default delivery.

## Preservation and resume migration
This upgrade does not change any student_work file, progress file or historical assessment record. The old unanswered branch quiz remains in the historical checkpoint. The instructor skill explicitly treats a new full-course activation as the new diagnostic route instead of endlessly repeating that miniature prompt. Only actual learner diagnostic outcomes may create exemptions or new progress entries. No learner mastery or completed lab is claimed.

## Manual instructional acceptance review
| Scenario | Required behavior after this rebuild |
| --- | --- |
| Start my Academy | FULL COURSE MODE; deliver chapter opening policy scenario/table/example, then one coherent diagnostic task |
| I’m on my phone, 20 minutes | Keep full content depth, split at a meaningful section boundary and resume later |
| Mobile review / quiz me | Explicit MOBILE REVIEW MODE, same correctness standard |
| Strong independent diagnostic | Skip mapped refreshers; review worked architecture then apply/practice independently |
| Partial diagnostic shows truthiness gap | Teach that subsection substantially without restarting all syntax |
| Learner asks a question mid-section | Answer it directly, then return to section; no compulsory flashcard interlude |
| Learner submits wrong code | Explain the observed gap, then offer a conceptual hint; learner changes code |
| Tests green but explanation/change absent | Keep assessment pending and collect missing evidence |
| Upgrade materials | Authoring mode only, no teaching or learner credit |

These are file/workflow reviews, not measured model-behavior evaluations. The new chapter and rules must still be used by the actual tutor. Automated test results and remaining limits are recorded below after execution.

## Executed validation — 2026-10-31
Python 3.12, pytest 9.2.0 via the temporary author dependency directory. Commands used PYTHONPATH=/tmp/academy-test-deps and PYTEST_DISABLE_PLUGIN_AUTOLOAD=1; those variables are environment-specific, not course requirements.

- Default `python -m pytest -q`: **47 passed**. Includes 34 actual worked-example checks (all waiting/VIP boundaries, malformed fields, lifecycle precedence, non-mutation/no output, demo output and importable unfinished guided starter), 11 navigation/chapter/starter/internal-link checks and the original two course structure/config checks. All 10 Python chapter blocks executed with the documented outputs.
- Worked demo ran successfully with the five documented decisions: IGNORE, SERVICE_DESK, ON_CALL, REVIEW, QUEUE. The deliberately faulty debug demo produced only the first tuple and None for empty input, confirming the reproducible defect.
- Explicit independent suites: **70 expected missing-callable setup errors** against the preserved student file (49 priority and 21 summary cases). Guided suite: **3 expected missing-submission setup errors**. These are unfinished labs, not failed installation and not a learner pass.
- Debug reproduction suite: **3 expected failing assertions** against the intentionally faulty course file: empty result, continuation after closed, and closed-first record. The course fixture remains faulty for learner investigation.
- Acceptance-test author QA: **76 passed** against fixed exact-input canned response tables (70 independent + 3 guided + 3 debug). **13 injected faults were rejected**: summary threshold/early exit/mutation/shared state/count types; priority ordering/AND-vs-OR/boundary/invalid type/mutation/output; preview early exit/closed-record omission. This validates case expectations and test sensitivity, not a general working implementation of the independent assignment. No general assignment solution is committed, and the temporary probe was removed.
- Compile checks passed for the lesson source and assessment files; `python academy.py next` resolved the current Lesson 01.
- Preservation check: all 20 student files, the progress record, and all 38 Lesson 02–20 chapter/readme files are unchanged from the pre-rebuild snapshot. Existing summary contract and its tests remain v1. No learner activity or mastery was recorded by this upgrade.
- External lesson links were rechecked using tools/check_links.py; see LINK_AUDIT.md for exact HTTP status and redirects. Reachability does not prove paid/free access. Both Lesson 01 resources supplement a self-contained chapter.

## Remaining limits
These checks exercise real teaching example code and course tooling. They do not certify that an AI tutor will follow the new workflow in every conversation, and the canned-response QA is not a substitute for a student's independent tested implementation. No live VS Code/Codespaces UI or Docker deployment was launched for this rebuild. Lessons 02–20 remain drafts. Material depth, labs and default delivery now have a reference for their later upgrades; no full-course completion is claimed.
