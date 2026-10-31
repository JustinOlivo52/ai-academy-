# Course author / instructor notes

Lesson 01 is the reference-quality upgraded chapter. Lessons 02–20 remain legacy drafts, not validated full chapters. See curriculum/AUDIT.md and curriculum/UPGRADE_PLAN.md. Do not imply the whole Academy upgrade is complete.

Authoring requests use curriculum/COURSE_STANDARD.md; teaching requests use .agents/skills/academy-instructor/SKILL.md; grading uses academy-assessor. Skills are repository instructions, not an automatic grading server or a web UI. The learner must open the repository in a skill-capable tutor or provide the files through the portable prompt.

`python -m pytest -q` runs course-integrity/tooling checks only. `python -m pytest -q assessments/lesson_01/test_summary.py` runs Lesson 01 student acceptance tests and is expected to fail until the learner implements the function. The old practice/test_ticket_rules.py is a later priority-classification lab and also intentionally fails while unimplemented. Neither suite is silently skipped or counted as learner success.

Course quality checks should exercise navigation, lesson examples, links, student boundary contracts and failure behavior. Do not commit a reference implementation of the student's lab. Record actual author validation in curriculum/VALIDATION.md, never in the student's assessment ledger. Runtime testing does not prove an AI tutor will follow instructions in every future conversation; use the scenario checklist there for manual acceptance.
