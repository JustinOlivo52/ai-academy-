# Upgrade validation — 2026-10-31

Author/tooling evidence only; no learner assessment is passed by this document. Final executed results are listed below after validation.

## Conversation acceptance scenarios (instruction review, not an automated model eval)
| Request / situation | Required next behavior |
| --- | --- |
| Start Lesson 01, 20 minutes, phone | Read routing/current lesson; explain first concept with separate example; ask one diagnostic; wait |
| Resume after unanswered diagnostic | Reuse exact pending question; do not assume completion or restart the lesson |
| Learner gets branch order wrong | Trace first true branch with a different value; one conceptual hint; request another attempt |
| Learner has only code in chat | Review it; distinguish reasoning from execution; assessment stays pending |
| Tests pass but no explanation/modification | Ask one evidence question; do not mark mastery |
| Learner asks for full answer | Record assistance; require a fresh independent variation for mastery |
| Upgrade course materials | Enter author mode; do not teach, fill student TODOs or award progress |

These scenarios were checked against repository routing, skills and the lesson's pause points. Actual future model behavior depends on the tutor reading and following the files; no claim of automated model reliability or a live Codespaces session is made.

## Executed checks
Environment: Python 3.12. Course files materialized from the baseline GitHub snapshot. pytest 9.2.0 installed in a temporary author-only dependency directory; no requirements were changed. Commands below used PYTHONPATH=/tmp/academy-test-deps and disabled unrelated preinstalled pytest plugins for the clean final run.

- `python -m pytest -q`: **13 passed**. Includes original two structure/config tests plus current-lesson navigation from another working directory, missing/malformed/duplicate/out-of-range progress rejection, missing/ambiguous lesson rejection, execution of all 11 Python lesson examples with expected output, documented unfinished optional starter, and relative Markdown link resolution.
- `python academy.py next`: resolved Lesson 01's real LESSON.md; `list` returned all 20 numbered lessons. CLI never grades or mutates progress.
- `python -m compileall -q academy.py student_work practice lessons/01-python-diagnostic-and-control-flow/STARTER.py`: passed. Existing student and practice files import/compile; the optional starter raises documented NotImplementedError only when called.
- Explicit `assessments/lesson_01/test_summary.py` against unchanged student file: **21 expected setup errors**, each identifying the missing summarize_tickets function. Not treated as passing learner tests.
- Acceptance-suite author QA: **21 passed** against finite canned input/output responses for the suite's exact cases, not an implementation of the lab. Seven injected fault modes were each rejected: threshold off-by-one (2 failures), invalid counted non-urgent, early exit, input mutation, shared return state, printed output and float counts (1 failure each). The temporary probe was removed. This checks test expectations and sensitivity; it does not establish an independently working general implementation or learner mastery. No assignment solution committed.
- All **20 student_work files preserved byte-for-byte** against the baseline. No completed exercise overwritten, no learner pass awarded, existing progress facts and journal retained.
- `python tools/check_links.py`: **36 distinct current external lesson URLs returned HTTP 200**, including redirects. See LINK_AUDIT.md. Old RAG URL redirects to Deep Agents RAG; its topic relevance needs review in Batch G. Reachability does not prove free access or lesson fit.
- Manual review: Lesson 01 covers every COURSE_STANDARD requirement; worked examples are separate from the summary lab. Skills route start/resume/assessment requests, pause for learner turns and separate authoring from teaching.

## VS Code / Codespaces and remaining limits
Existing Python 3.12 devcontainer JSON and extension settings were inspected and validated by the structure check. Added a Python 3.12 GitHub Actions integrity workflow and documented local/Windows/Codespaces setup. The CLI and offline checks ran locally; no live Codespaces workspace, VS Code UI or Docker build was launched in this environment. Later projects remain specifications, not running APIs. Lessons 02–20 require the planned content, test and interaction review before full-course readiness can be claimed.

## Remote verification
Published in pull request #1 on academy/interactive-bootcamp-lesson-01. GitHub Actions Course integrity run 41195742956 completed successfully: https://github.com/JustinOlivo52/ai-academy-/actions/runs/41195742956. This validates the Python 3.12 requirements install, CLI navigation and default course checks on GitHub, not a live Codespaces UI or learner assessment. All 20 remote student blob SHAs matched baseline.
