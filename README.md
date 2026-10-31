# AI Engineering Academy

An original, project-based junior AI Automation Engineering bootcamp. **20 short lessons**, three progressive project stages and one capstone. Built for local VS Code, Codex, Claude, and GitHub Codespaces.

## Full-course reference status
Lesson 01 is rebuilt as a 60–90-minute Python Control Flow and Business Logic course with a diagnostic skip path, full worked support-ticket example, guided lab, independent priority/summary assignment and debugging assessment. **FULL COURSE MODE is default; MOBILE REVIEW MODE is explicit opt-in.** Start with [START_HERE.md](START_HERE.md); [the current rebuild audit](curriculum/FULL_COURSE_REBUILD.md) records scope and validation. Lessons 02–20 remain preserved drafts awaiting [the batches](curriculum/UPGRADE_PLAN.md). No student work or progress is reset.

## Start here
1. Read `curriculum/SYLLABUS.md` and `AGENTS.md`.
2. Open `lessons/01-python-diagnostic-and-control-flow/LESSON.md` (or locate Lesson 01 from the syllabus).
3. `python -m pip install -r requirements.txt` and `python -m pytest -q`.
4. Run `python academy.py next` for your next lesson; `python academy.py status` for progress.
5. Work in `student_work/` or the associated project directory. Do not ask the tutor to automatically write the answer.

## Study pattern
**Diagnostic → substantial chapter teaching → worked demonstration → guided lab → independent implementation → assessment/review.** Familiar concepts can be skipped only using diagnostic evidence; short sessions resume the same full course.
For low-energy days, use a lesson's two **Go Deeper** resources (reading or video), then write a three-sentence learning note. Doing supplemental material does **not** count as passing the hands-on assessment.

## Project arc
- Stage 1: pure-Python ticket processor (`projects/01_ticket_processor/`).
- Stage 2: tested API + persistence (`projects/02_service/`).
- Stage 3: mock-first LLM workflow with evaluation and human approval (`projects/03_ai_service/`).
- Stage 4: capstone and junior engineer simulation.

**No paid API key is required.** Mock services and fictional business data are the default. Do not put employer secrets, patient data, or client code here. This repo is a personal learning system, not company material.

## Codex / Claude
`AGENTS.md` contains tutor policies for Codex; `CLAUDE.md` carries the same rules for Claude. `prompts/START_SESSION.md` is a portable activation prompt for ChatGPT, Claude and Codex when the referenced files are available. Course source material is local Markdown so learning works even when course websites are inaccessible.

## Schedule
Target essential Python, engineering, API and automation skills before Nov 23, 2026. Continue the deeper AI engineering track across the first 90 days. Hours are estimates, not guarantees.
