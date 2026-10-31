# Independent assessments

Read .agents/skills/academy-assessor/SKILL.md before grading. Each actual attempt gets a new record based on RECORD_TEMPLATE.md; no hypothetical or pre-awarded passes. Lessons 02–20 still need lesson-specific contracts and acceptance suites under the upgrade plan.

Lesson 01: read lesson_01/ASSESSMENT.md and run `python -m pytest -q assessments/lesson_01/test_summary.py` against the learner's submission. Initial missing implementation is an expected failure. Default repository tests are not assignment tests.

Passing requires independently authored behavior, relevant executed tests, an unassisted explanation, a checked edge case and a fresh small modification. Review constructively, but let the learner change code. Assisted work may earn study credit; use an unseen variation for independent reassessment.

Stage simulations build on existing projects: reproduce a ticket bug; add a regression test and fix; expose tested API/persistence behavior; validate mock model output and approval routing; then deliver a capstone change with a PR-style summary, architecture note and independent demo. Each future simulation needs a precise published contract and rubric before grading.
