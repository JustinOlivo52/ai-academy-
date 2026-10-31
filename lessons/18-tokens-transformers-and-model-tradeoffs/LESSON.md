# Lesson 18 — Tokens transformers and model tradeoffs

**Stage:** AI Engineering · **Time:** 60–120 minutes · **Prerequisite:** earlier lessons or demonstrate equivalent skill.

## What you will learn
1. Describe the core idea in your own words.
2. Apply it in a small support-ticket workflow.
3. Test expected behavior and edge cases.

## Core lesson — read before coding
Transformers rely on attention to combine token context; inference quality depends on model, prompt and available context. Compare latency, privacy, cost and quality rather than assuming larger models are always superior.

### Why this matters on a real team
A junior engineer is expected to make small, reviewable changes that other people can understand. Treat input as potentially bad, describe the expected behavior explicitly and make your choice testable. If you cannot explain where a failure would be handled, pause and draw the data flow.

## Worked thinking example (do not copy into the assignment)
Imagine a support ticket with `{"ticket_id":"T-101","urgency":4,"impact":3}`. Identify what the program knows, what can be invalid, and which part of the system should make the decision. Write one example of good input, one boundary case and one malformed input before implementing. Separate transformation logic from output or network actions.

## Guided practice (15–20 minutes)
Compare two hypothetical models using a cost/latency/quality decision matrix.

Before typing code, write the function signature or interface and two sample inputs with expected outputs. Ask the tutor for a hint rather than a solution.

## Independent assignment (25–45 minutes)
Write a one-page architectural decision record selecting a model for ticket routing.

**Deliver:** a Python file or design note in `student_work/lesson_18.py` (or `.md` for architecture exercises), tests or a test plan, and a short explanation of one edge case.

## Check your understanding
- Which input would make your solution fail, and how would you detect it?
- What unit or integration test would catch that failure?
- How would you explain the change to a senior engineer in a pull request?

## Completion rubric
- [ ] Working implementation or coherent design is present
- [ ] Happy path and invalid/boundary case are tested
- [ ] I can describe the implementation without reading an AI-generated explanation
- [ ] I made one independent correction after feedback

## Go Deeper — two resources
1. **Read / Real Python or technical article:** https://realpython.com/tutorials/ai/
2. **Official docs / course material:** https://huggingface.co/learn/llm-course/chapter1/1

**Low-energy alternative:** use either link for 10–20 minutes, then add three sentences to progress/PROGRESS.md: a new concept, a practical use, and a question. This is study credit, not assessment completion.

## Next lesson
Return to `curriculum/SYLLABUS.md` and advance only after the completion rubric is met.
