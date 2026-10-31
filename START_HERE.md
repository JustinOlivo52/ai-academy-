# Start your Academy

Open this repository in VS Code with Codex, or in GitHub Codespaces with your AI tutor. Your current lesson is recorded in [progress](progress/PROGRESS.md). Lesson 01 is the upgraded reference chapter; the other 19 are drafts awaiting the batches in [the upgrade plan](curriculum/UPGRADE_PLAN.md).

Say: **“Start Lesson 01. I have 20 minutes and I’m on my phone. Teach one concept and ask one question at a time.”**

To return: **“Resume my Academy lesson from progress/PROGRESS.md.”** To check readiness: **“Assess my Lesson 01 work; don’t give hints.”** Root AGENTS.md routes these requests to the instructor or assessor skill. If your chat cannot discover repository skills, paste [the session prompt](prompts/START_SESSION.md) and provide the linked files. The CLI navigates; it is not an AI tutor.

You write the code. The tutor teaches, demonstrates separate examples, reviews attempts and pauses for responses. It never fills in your lab. Reading, reasoning in chat and code execution are recorded distinctly. A lesson can span several short sessions; phone work does not require a terminal.

## Laptop / Codespaces setup
Use Python 3.12 (the devcontainer selects it). In VS Code open the repository folder and select your virtual environment. In Codespaces the post-create step installs requirements; select the Python interpreter if prompted. No API keys or paid services are needed.

```bash
python -m venv .venv
# macOS/Linux; Windows PowerShell: .venv\Scripts\Activate.ps1
source .venv/bin/activate
python -m pip install -r requirements.txt
python academy.py next
python -m pytest -q
```

The last command checks course tooling, not mastery. When ready for the Lesson 01 lab:

```bash
python -m pytest -q assessments/lesson_01/test_summary.py
```

Initially those tests FAIL with a clear message because `summarize_tickets` is not implemented. This is expected. Put your own function in the existing `student_work/lesson_01.py` without deleting prior work. A signature-only template is in the lesson's `STARTER.py`; do not copy over an existing attempt. To assess another file, set `ACADEMY_SUBMISSION` to its repository-relative path before running the same command. It must stay inside student_work.

The older `practice/test_ticket_rules.py` is a later Project 1 priority classifier, not Lesson 01. It is intentionally unfinished and outside default checks. Its HIGH/MEDIUM/LOW rule uses urgency AND impact; Lesson 01 counts urgency only.

At session end the instructor summarizes actual learning, records an exact next action, and preserves assessment history. Passing requires tested independent work, your explanation, an edge case and a small fresh modification. Setup and green course checks never pass a lesson.
