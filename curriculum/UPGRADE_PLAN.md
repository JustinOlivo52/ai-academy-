# Remaining Academy upgrade batches

Keep all 20 lesson numbers and project directories. Lesson 01 is the reference validated first. This is an authoring backlog, not a new student schedule or a promise to finish before November 23. Prioritize independent correctness over course percentages. Do not begin the next batch until the current batch passes the standard and a teaching rehearsal.

## Repeatable batch definition of done
For every chapter: original textbook explanations, multiple executed annotated examples, traced walkthrough, guided turn boundaries, exact independent contract, debugging task, five knowledge checks, meaningful acceptance suite (or artifact rubric), troubleshooting, summary, exactly two checked references and evidence-based completion gate. Preserve attempts; document migrations; no student solution committed. Run offline course checks, validate contract boundary/failure tests and rehearse one wrong answer, hint, phone interruption and assessment handoff. Publish audit evidence before proceeding.

## Batch A — 02–03: collection and interface fluency
- 02: list/dict lookup, iteration, transformations, comprehensions and duplicate-ID policy. Teach loop form before comprehension. Specify index_tickets input/output and duplicate/absent ID errors; test order/duplicates/non-mutation. Guided example uses a different record type.
- 03: parameters/return, scope, small modules, pure interfaces and imports. Design calculate_priority using Project 1's documented AND/OR thresholds. Expand existing practice cases to cover all boundaries and invalid types rather than replacing student work.
- Integration: call learner-authored 01 summary and 02 index from a small project interface. Gate: explain transformation versus lookup and implement a fresh rule variation independently.

## Batch B — 04–05: validated local applications
- 04: classes versus dictionaries, dataclasses, typing limits, exceptions and validation ownership. Specify Ticket construction errors (including bool) and typed boundaries; test bad/missing fields, exception scope and readable errors.
- 05: JSON serialization, file encoding, pathlib, context managers and argparse. Specify malformed file, missing file, output path and exit behavior; use tmp_path and CLI subprocess tests.
- Integration: finish Project 1 CLI using earlier learner components; add sample input/output documentation. Gate: round-trip JSON, invalid data and a testable error path without input mutation.

## Batch C — 06–08: professional change workflow
- 06: working tree/index/commit/branch/PR, safe conflict practice in a temporary repository. Assessment is a small diff plus real history and PR-style explanation, not a fabricated Python task.
- 07: traceback reading, logging levels/context, narrow exceptions and debugger use. Supply a reproducible ticket defect and noisy/broken logs. Learner reproduces before fixing; never use real tickets.
- 08: assertions, parametrization, fixtures, monkeypatch/mock boundaries and regression proof. Supply a stable contract and controlled failing variants; tests must detect a defect and pass after the learner's fix.
- Integration: reviewable Project 1 change with tests and branch history. Gate: independent reproduction, regression test and small fix plus explanation of what mocks do not prove.

## Batch D — 09–10: API and persistence
- 09: HTTP request/response, JSON/status codes, FastAPI routes, dependency injection and Pydantic validation. Define /health and POST/GET ticket contracts with 200/201/404/422 behavior; TestClient tests run without a server or network.
- 10: tables/keys, CRUD, parameterized SQL, transactions, SQLite connection lifecycle and environment config. Specify duplicates and rollback behavior; isolate each database in a temporary directory.
- Integration: Project 2 uses learner's deterministic ticket logic; persistence tests cover close/reopen and failure cases. Gate: explain a request end-to-end and fix an input-validation regression.

## Batch E — 11–12: mock-first LLM and tools
- 11: model adapters, messages, typed structured outputs, malformed responses, token accounting and cost arithmetic. Include explicit LangChain adapter comparison after plain Python behavior. No live key required; hosted provider setup is optional separate work.
- 12: tool schemas, call validation, deterministic dispatch, tool result versus user response and side-effect boundaries. Teach plain functions first, then LangChain tool binding with a fake model. Specify unknown tool/invalid argument outcomes.
- Integration: Project 3 starts with fixed model responses and safe fictional lookups. Gate: adversarial malformed response and denied write tool both tested; no network in default suite.

## Batch F — 13–15: state, reliability and integration protocols
- 13: explicit state schema, node updates, conditional edges, stop conditions and LangGraph execution; compare deterministic pipeline to framework flow. Tests cover routes and termination.
- 14: transient versus permanent errors, bounded retries/backoff, idempotency, timeouts and human approval. Fake clock/sleeper, duplicate events and denied/missing approval cases. Replace weak asyncio reference with a topic-specific source after verification.
- 15: MCP client/server/tool/resource concepts, schemas and local transport lifecycle. Wrap a proven pure function in a tiny local example; specify protocol errors, no real external writes.
- Integration: Project 3 route/verify/approve simulation. Gate: show retries terminate, approval blocks effects and state remains explainable.

## Batch G — 16–18: retrieval, evaluation and model tradeoffs
- 16: chunking, embeddings/similarity, retrieval context, grounded response and abstention. LangChain retrieval adapter follows a deterministic fixture retriever. Verify replacement for the old URL that redirects to Deep Agents RAG. Test ranking, empty retrieval and irrelevant context.
- 17: labels, precision/recall, groundedness, failure slices and quality gates. Ship a fictional dataset and numeric worked confusion matrix; protect holdout cases. Gate tests detect deliberate regressions.
- 18: tokens/context, transformer mental model, latency/quality/cost and model selection. Original annotated arithmetic examples plus a reproducible comparison harness using fixture measurements. Assessment is an evidence-based ADR, not a token quiz alone.
- Integration: evaluate Project 3 against versioned cases; gate shows measured improvement and a documented tradeoff without invented benchmark numbers.

## Batch H — 19–20: production and junior simulation
- 19: Docker layers/build context, environment configuration, health checks, deployment/rollback and observability. Add Dockerfile only after service exists; build/run/smoke checks, no credentials in image or logs. Validate locally/Codespaces before hosting.
- 20: unseen fictional bug report, scoped change, acceptance criteria, tests, PR-style description, architecture note and independent demo. Rubric measures understanding, debugging, review response and delivery.
- Integration: package and demonstrate the existing capstone. Gate: independent small feature/bug fix, reproducible evidence and honest limitations. Remote deployment is optional and requires a real target; local smoke checks never imply it happened.

## Sequencing and readiness
Lessons 01–12 and 14 remain the pre-onboarding priority. Do not skip an unproven prerequisite to meet a date. After each batch, update its material-readiness status in SYLLABUS, record author checks in VALIDATION, and leave learner PROGRESS unchanged until actual learning/assessment evidence exists.
