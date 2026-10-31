# Course author / instructor notes

Lesson 01 is the reference-quality upgraded chapter. Lessons 02–20 remain legacy drafts, not validated full chapters. See curriculum/AUDIT.md and curriculum/UPGRADE_PLAN.md. Do not imply the whole Academy upgrade is complete.

Authoring requests use curriculum/COURSE_STANDARD.md; teaching requests use .agents/skills/academy-instructor/SKILL.md; grading uses academy-assessor. Skills are repository instructions, not an automatic grading server or a web UI. The learner must open the repository in a skill-capable tutor or provide the files through the portable prompt.

`python -m pytest -q` runs course-integrity/tooling checks only. `python -m pytest -q assessments/lesson_01/test_summary.py` runs Lesson 01 student acceptance tests and is expected to fail until the learner implements the function. The old practice/test_ticket_rules.py is a later priority-classification lab and also intentionally fails while unimplemented. Neither suite is silently skipped or counted as learner success.

Course quality checks should exercise navigation, lesson examples, links, student boundary contracts and failure behavior. Do not commit a reference implementation of the student's lab. Record actual author validation in curriculum/VALIDATION.md, never in the student's assessment ledger. Runtime testing does not prove an AI tutor will follow instructions in every future conversation; use the scenario checklist there for manual acceptance.

## Full-course reference revision
The first upgrade's 1–3-paragraph opening and automatic short phone format produced miniature instruction despite a longer chapter. Those rules are superseded. FULL COURSE MODE now delivers the chapter's meaningful sections and worked code, with diagnostic-driven exemptions; MOBILE REVIEW MODE requires explicit opt-in. The full-course audit and current validation are in curriculum/FULL_COURSE_REBUILD.md. The original VALIDATION.md is historical evidence for the first upgrade, not the current test counts.

Lesson 01's assessment v2 adds priority_for alongside the unchanged summary v1 contract. Guided preview and intentionally faulty debugging fixture have separate explicit suites. Preserve all historical student/assessment records; no authoring change awards a learner pass. Old unanswered miniature checkpoints remain historical, but a new full-course activation uses the new diagnostic route instead of repeating them indefinitely.
