# Lesson 01 assessment contract, version 1

Primary submission: `student_work/lesson_01.py`, function `summarize_tickets(tickets)`.
Read the exact input/output contract in the lesson. All submitted code must be learner-authored; a template is not an attempt. The acceptance suite imports but does not edit the submission. Read code before executing it.

## Evidence sequence (one item per learner turn)
1. Independent implementation; run `python -m pytest -q assessments/lesson_01/test_summary.py`. Missing function and NotImplementedError are expected before the learner starts. Do not xfail real bugs to make the suite green.
2. Ask the learner to explain why invalid records cannot reach the urgency comparison and why the summary is returned after processing the whole list.
3. Ask for one boundary or malformed case not already discussed, its predicted summary, then an executed check. Prediction alone is not execution.
4. Select a small fresh modification after inspecting the submission, such as accepting a caller-supplied threshold with an explicit default and validation contract. Require learner-written code and a test for the change. Do not add it to the base contract automatically.
5. Review readability and any independent correction; re-run affected checks on final code. Store actual evidence using the record template.

## Pass gate
All assessor dimensions must be met. Also complete the debugging challenge and answer the five knowledge checks in the lesson (ask separately, review misconceptions). Document guided help separately from the unassisted final variation. Phone tracing or an unexecuted design note remains study/in-progress. The course author must not record a pass for validating this suite.

The contract intentionally assumes a list of dictionaries. Top-level non-lists, non-dictionary records, duplicate IDs and invalid IDs are outside Lesson 01 scope; later lessons add structure and exception validation. Do not invent hidden requirements in grading.
