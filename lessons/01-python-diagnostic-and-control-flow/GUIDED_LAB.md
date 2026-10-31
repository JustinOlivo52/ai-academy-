# Guided lab — preview the escalation queue

**Time:** about 15 minutes. Read chapter §§3–6 first unless the diagnostic exempts refreshers. Use the complete worked function in examples/escalation.py as a dependency; you implement the batch behavior. This is guided practice, not the independent urgency/impact assignment.

The fictional operations team needs a preview before any notification is sent. The output is a list of `(ticket_id, channel)` tuples, one per input record in original order. A closed record still appears with IGNORE so the reviewer can account for it. Bad timing appears with REVIEW. There is no notification API and no data mutation.

The optional starter is labs/GUIDED_STARTER.py. Copy it only to a NEW student file, for example student_work/lesson_01_preview.py. If that path exists, choose a new name. Do not modify the course example or overwrite earlier attempts. Tests select the file through ACADEMY_GUIDED_SUBMISSION; default is that example student path.

## Stage 1 — establish the expected preview
The input contains: open G-1 waiting 60 minutes, non-VIP; closed G-2 with no timing; open G-3 waiting 3 minutes, non-VIP. State the full expected output before code and explain why the closed ticket remains in the list. The instructor waits, reviews the reasoning and explains any policy confusion before asking for implementation.

## Stage 2 — learner writes the batch function
Implement `preview_escalations(tickets)`. Assume a list of dictionaries with guaranteed string ticket_id fields; routing fields follow the worked contract. Call `escalation_channel` from the supplied example. Preserve every input record in the output (including IGNORE/REVIEW), ordering and input objects. Empty input returns a fresh []. No printing, file access or real effects.

Use a loop or a clear comprehension, and explain the choice. Do not add ID validation or sorting that the contract did not ask for. The instructor reviews actual code rather than supplying the loop. If the learner is stuck after an attempt, the first hint should concern output scope; a stronger scaffold may show the function signature and a blank accumulation step, not the answer.

Run from the repository root:

```bash
python -m pytest -q assessments/lesson_01/test_guided.py
```

Expected before implementation: a clear missing-submission/callable failure or the starter's NotImplementedError. Expected after correct independent typing: all supplied guided cases pass. Their result is practice evidence, not lesson mastery.

## Stage 3 — boundary regression and review
Write one additional test comparing ordinary tickets at 59 and 60 minutes. Explain why the pair detects a reordered or wrong-boundary rule. If the instructor showed that exact case during earlier explanation, choose a distinct VIP boundary pair. The learner authors the assertion. Review a sample for input preservation and ensure two calls do not share an output list.

## Done evidence
Actual expected preview, learner-authored function, relevant executed tests or explicitly pending execution, one own boundary regression, and a brief explanation of collection/control-flow choices. Log assistance. A strong full diagnostic may exempt this repetition, but the final independent assignment and debugging assessment remain required.
