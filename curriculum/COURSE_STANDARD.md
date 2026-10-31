# Academy course standard

The course is self-paced and instructor-led through an AI conversation in the repository. Original chapters must suffice without subscriptions. Authoring produces materials, never completed student work. Lesson 01 is the reference; Lessons 02–20 remain legacy drafts until reviewed against this standard.

## Required lesson structure
1. Title, lesson number, stage, measurable objectives, specific prerequisites and honest duration with interruptible sections.
2. Original textbook explanation: define terms, connect prior knowledge, explain execution/data flow and tradeoffs. More than a heading and paragraph; learners should predict behavior before implementation.
3. Concrete junior-engineer relevance tied to a fictional ticket project.
4. Multiple runnable annotated examples with expected outputs. Examples must differ from the independent assignment so reading is not copying its solution.
5. One practical walkthrough: inputs, explicit rule, intermediate state trace, result and edge case.
6. Guided practice with instructor turn boundaries; a question, pause, response review and progressively stronger hints. Do not publish an answer beside the question.
7. Independent assignment with precise interface, file, input types, output schema, valid/invalid/boundary behavior, non-mutation rule and acceptance criteria.
8. Debugging challenge with reproducible faulty behavior, expected behavior and regression-test requirement. Student makes the fix.
9. Exactly five conceptual knowledge-check questions; ask individually during teaching.
10. Automated acceptance tests for executable tasks; for design/Git work, a reproducible artifact-check procedure plus human rubric. Detect plausible bugs, not just file presence. Keep course checks distinct from incomplete student labs.
11. Common mistakes, symptoms, causes and troubleshooting steps.
12. A substantive summary connecting to the next lesson/project.
13. Exactly two relevant optional Go Deeper resources; record link-check date/status. Paywall or network failure never blocks the original lesson.
14. Completion criteria requiring independent code, test evidence, explanation, an edge case and a fresh small modification. Studied is not passed.

## Author review gate
Trace each objective to explanation → exercise → evidence. Execute examples and starter imports; placeholders fail only in documented ways. Run repository checks and explicit lab tests. Verify acceptance tests against controlled correct/incorrect behavior without committing an assignment answer. Check internal links and external resource availability; label uncertainty instead of inventing success.

Read student_work and progress before writing. Do not edit student attempts; add versioned templates or tests elsewhere. Preserve old evidence when changing a contract, document migration and never retroactively revoke a pass. Assessment records contain date, attempt path/hash, assistance, command/results, explanation and modification evidence, verdict and next action.

Validate one batch before authoring the next. Headings and word counts do not establish chapter quality. Use manual pedagogical review and conversation scenarios as well as automated checks. No deadline, including November 23, warrants invented mastery.
