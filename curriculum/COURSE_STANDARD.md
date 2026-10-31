# Full educational bootcamp course standard

The Academy is a self-paced original textbook plus instructor-led programming course. FULL COURSE MODE is default; MOBILE REVIEW MODE is explicit optional reinforcement. A phone never lowers depth. Curriculum authoring changes material, not learner progress. Lesson 01 is the reference; do not rewrite Lessons 02–20 before validating it.

## Required architecture for every future lesson
1. Substantial self-contained chapter, with measurable objectives, prerequisites, an honest duration and connected explanations. Define mechanisms, data flow, tradeoffs and failure modes, not just syntax.
2. Concrete professional relevance in the progressive support-ticket projects.
3. Several runnable annotated examples with output explanations and edge cases.
4. A full realistic worked example: requirements, decision table, implementation, trace and tests. Its solution must differ from the independent assignment.
5. Guided programming lab with stages, starter interface, exact contracts and automated stage checks. Ask for student code after meaningful teaching, not after every paragraph.
6. Independent assignment with precise input/output/validation behavior and acceptance tests. Keep student attempts outside lesson source; never overwrite them.
7. Intentionally faulty runnable code, reproducible failure cases and a learner-written regression fix.
8. Conceptual and practical assessment requiring independent code, executed tests, explanation, checked edge case and fresh modification. Separate content consumption, diagnostic exemption and practical mastery.
9. At least two supplementary resources, with Real Python where relevant, checked for reachability and semantic fit. All required teaching stays in the original chapter.
10. Published diagnostic tasks with concept-to-section mapping, independent evidence criteria, partial-result remediation and a documented skip path. Prior project experience alone is not evidence; one tiny quiz does not exempt all basics.
11. Troubleshooting, clean-code guidance, review checklist, summary and explicit completion criteria.

## Delivery standard
An instructional turn completes a meaningful teaching section, using several connected paragraphs, annotated code and realistic reasoning before asking one checkpoint task. Learners can ask questions at any point. Use the written chapter rather than improvising a miniature lesson. Full chapters can span short sessions without shrinking the material. Mobile review is optional and has the same correctness/assessment requirements.

## Validation gate
Execute example files and assert their documented behavior. Exercise actual contract cases including boundary/type/error/continuation/non-mutation behavior. Student starters must import and fail only with documented NotImplementedError until attempted. Never make unfinished assignments green via hidden reference answers or xfail. Keep default course checks separate from explicit learner suites.

Check test sensitivity using fixed finite responses or injected faulty variants without committing a general independent-assignment solution. Report that limitation accurately. Rehearse mode routing, diagnostic skip, substantial-section delivery, wrong-answer feedback, question interruption, phone behavior and assessment handoff. Structural tests alone do not prove good teaching or future model compliance.

Read progress/student work before authoring; preserve their bytes and history. Version changed contracts, retain prior evidence, and never retroactively revoke passes. Only actual learner evidence can update mastery. Subsequent lesson batches follow this standard after Lesson 01 review.
