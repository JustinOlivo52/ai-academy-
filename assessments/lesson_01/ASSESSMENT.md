# Lesson 01 assessment — full-course v2

Assessment v2 consists of independent priority_for(ticket) plus the preserved summarize_tickets(tickets) v1 contract in the lesson's ASSIGNMENT.md. Preserve historical v1 records as v1; never retroactively overwrite or upgrade their verdict. There are no recorded passes at authoring time.

## Placement is separate from mastery
Use the published DIAGNOSTIC.md tasks and skip map to exempt already-demonstrated teaching sections. Record actual code/explanation, independence and execution status. A diagnostic does not replace the final practical gate. Guided lab repetition may be skipped only with the full independent diagnostic evidence defined there.

## Conceptual assessment
Ask the chapter's five review questions separately after instruction/application. Evaluate accuracy, reasoning and concrete cases rather than memorized words. Required concepts: ordered overlap, Boolean semantics/truthiness, validation before unsafe operations, guard/loop exit scope, non-mutation, partition invariants, and loop/comprehension choice. Each must be explained accurately; remediate only the gap.

## Practical evidence sequence
1. Inspect learner code before running. Both functions must meet ASSIGNMENT.md. Run `python -m pytest -q assessments/lesson_01/test_priority.py assessments/lesson_01/test_summary.py` on the actual final file (default student_work/lesson_01.py or ACADEMY_SUBMISSION). No network/credentials. Missing callables or NotImplementedError are expected before the learner implements; never xfail them into a pass.
2. Review at least three learner-written tests, including boundaries/overlap, malformed values and a batch/non-mutation regression. Run their actual test file; document command, counts, environment and final code revision/hash. A supplied test suite alone is insufficient evidence of testing judgment.
3. Inspect the learner's corrected debugging preview and regression evidence. Reproduce at least multi-record continuation, a closed-first record and empty input. The uncorrected course fixture must stay faulty. Use ACADEMY_DEBUG_SUBMISSION for a separate learner correction.
4. Ask for an unassisted explanation of why HIGH and urgent are not equivalent, validation precedes comparison, and return belongs after the summary loop. Ask for a new edge case prediction and executed check.
5. Select one fresh small modification after reviewing the code. State a complete change contract, require independently authored code/tests and a brief tradeoff explanation. Do not silently expand the published base contract or give hints during the attempt.
6. Review any corrections without taking over. Re-run affected tests on the final state; log assistance and use a fresh variation where independence was lost.

## Evidence gate and record
Use RECORD_TEMPLATE.md in a NEW actual attempt file. Mark implementation, executed testing, conceptual explanation, checked edge case and fresh modification as met/needs revision/pending with evidence. All must be met. Also require debugging/regression evidence and own tests. A phone trace or unexecuted chat code remains pending execution. Neither diagnostic exemption nor reading nor course-author CI earns a practical pass.

On a genuine pass append the assessment reference and advance Current lesson. On partial work save the exact next action without advancement. Course maintenance must leave progress untouched. FULL COURSE MODE and MOBILE REVIEW MODE share this evidence gate.
