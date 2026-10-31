# Start the full Academy course

Open the repository in VS Code/Codex or GitHub Codespaces. Read [the current lesson](lessons/01-python-diagnostic-and-control-flow/LESSON.md), or say:

> Start Lesson 01 in FULL COURSE MODE. Use the diagnostic to skip skills I can already demonstrate, then teach the full chapter and guide me through the labs.

**FULL COURSE MODE is the default.** “Start my Academy” activates it too. The instructor teaches a meaningful chapter section with annotated examples and a worked scenario before a checkpoint. You can ask questions during instruction. A phone or a 20-minute window changes session boundaries, not educational depth; the course resumes across sessions.

For optional reinforcement, explicitly say: **“Use MOBILE REVIEW MODE for a short control-flow review.”** It uses tracing, small exercises and quizzes with the same correctness standard. It does not replace the full course or make assessment easier.

## What Lesson 01 contains
- [Original chapter](lessons/01-python-diagnostic-and-control-flow/LESSON.md): business policies, Boolean logic, truthiness, guards/early returns, validation, batches, comprehensions and a complete support-ticket escalation example.
- [Diagnostic and skip map](lessons/01-python-diagnostic-and-control-flow/DIAGNOSTIC.md): demonstrate existing skills; skip only the associated refreshers.
- [Guided lab](lessons/01-python-diagnostic-and-control-flow/GUIDED_LAB.md): build an ordered escalation preview around the worked decision.
- [Independent assignment](lessons/01-python-diagnostic-and-control-flow/ASSIGNMENT.md): urgency/impact priority plus the preserved queue-summary contract.
- [Assessment](assessments/lesson_01/ASSESSMENT.md): conceptual explanations, independent implementation, own tests, debugging regression, edge case and a fresh small modification.

You write the lab code. Worked examples are complete teaching material, while starters deliberately raise NotImplementedError. Copy a starter only into a new student file, never over an existing attempt. Diagnostics exempt repeated instruction, not the practical mastery gate. Existing progress and student files remain intact. Lessons 02–20 are drafts pending [the batch plan](curriculum/UPGRADE_PLAN.md).

## Setup and commands
Python 3.12 is selected by the existing devcontainer; its post-create command installs requirements. For local VS Code, select your environment. No paid APIs, external services or terminal are needed to begin reading/learning.

```bash
python -m venv .venv
# macOS/Linux; Windows PowerShell: .venv\Scripts\Activate.ps1
source .venv/bin/activate
python -m pip install -r requirements.txt
python academy.py next
python -m pytest -q
```

The final command checks course/tooling integrity, not learner mastery. Run the worked example:

```bash
python lessons/01-python-diagnostic-and-control-flow/examples/escalation.py
```

Explicit learner suites:

```bash
python -m pytest -q assessments/lesson_01/test_guided.py
python -m pytest -q assessments/lesson_01/test_priority.py assessments/lesson_01/test_summary.py
python -m pytest -q assessments/lesson_01/test_debug.py
```

Guided and independent tests intentionally fail until your implementation exists. The debug suite intentionally fails against the faulty course fixture. Select your own files with ACADEMY_GUIDED_SUBMISSION, ACADEMY_SUBMISSION and ACADEMY_DEBUG_SUBMISSION, respectively, using repository-relative paths inside student_work. Examples: on macOS/Linux, `ACADEMY_SUBMISSION=student_work/my_attempt.py python -m pytest -q assessments/lesson_01/test_priority.py`; on PowerShell set `$env:ACADEMY_SUBMISSION = 'student_work/my_attempt.py'` before running pytest. The debugging fix stays in your workspace; never repair the intentionally faulty course example.

To resume: **“Resume my Academy in FULL COURSE MODE using my saved evidence and diagnostic exemptions.”** If a tutor cannot discover repository skills, provide [the portable prompt](prompts/START_SESSION.md) and lesson files. The CLI navigates; it is not an AI tutor or automatic grader. At the end, record only actual learner work and exact next actions.
