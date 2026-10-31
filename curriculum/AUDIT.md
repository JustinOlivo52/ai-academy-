# Academy audit — 2026-10-31

Baseline: JustinOlivo52/ai-academy-, master commit 5c735faf44041ed8d288ff0b005a5fa1a19ec2bd. Inspected all 82 tracked text files across README, AGENTS, curriculum, all 20 lesson chapters/readmes, all student files, projects, progress, assessments, prompts, tests and devcontainer. No .agents/skills directory existed. Source was materialized through the connected GitHub tools because the initial local git clone could not reach the proxy. Existing student files are preserved byte-for-byte.

## Findings and disposition
| Area | Evidence / practical problem | This upgrade |
| --- | --- | --- |
| Chapters 01–20 | Each original chapter has a one-paragraph core explanation, generic identical objectives and ticket thinking prompt, three generic questions, no runnable worked code, debugging challenge or topic-specific troubleshooting | Fully rewrite 01; label 02–20 drafts and plan their upgrade before claiming full-course readiness |
| Lesson 01 assignment | summarize_tickets had no output keys, urgent threshold, type/range handling or malformed-value policy | Contract v1 defines all of these, an invariant, non-mutation and empty behavior |
| Later assignments | Examples: 02 rejects duplicate IDs without a full interface/error contract; 08 asks for four tests without a fixed tested interface; 13 asks for a graph but lacks state/transition/error schemas; 18 is an ADR yet shares a generic coding rubric | Detailed batch plan requires precise contracts and appropriate artifact/code rubrics for each |
| Instructor behavior | AGENTS had useful modes and boundaries but no discoverable skills, turn-by-turn workflow, assistance policy or durable section resume | Add instructor/assessor skills and explicit routing, authoring separation and interruption rules |
| Progress | Only Current lesson: 01, no passed lessons and an empty journal | Preserve facts, add pending diagnostic checkpoint and evidence ledger; award no learning credit |
| Tests | Only two default tests, checking headings/link count and container image. No Lesson 01 behavioral tests. Eight practice cases intentionally fail on unimplemented later classifier | Keep suites separate; add navigation/example/link checks and explicit Lesson 01 acceptance suite |
| Projects | Three brief specifications, only sample tickets executable as data; no implemented services or capstone acceptance suites | Preserve project arc, connect 01 explicitly; later batches supply integration tests rather than unrelated apps |
| Resources | Two URLs each, but no recorded verification; some broad or poorly matched (asyncio for retries/approval; generic AI pages for MCP/evals). Old RAG tutorial redirects to Deep Agents RAG, which may change teaching scope | Record HTTP checks, flag semantic review in remaining batches; use focused control-flow references in 01 |
| Student work | 20 small learner-workspace stubs; no completed exercise evident in baseline | Leave all unchanged; add optional template outside student_work |
| Documentation | INSTRUCTOR_NOTES called all 20 chapters usable despite missing teaching depth; setup green could be confused with lab success | State exact readiness and command meanings in README, START_HERE, notes and prompts |
| Local/Codespaces | Python 3.12 devcontainer and requirements already exist, but no workflow validation or CI; CLI silently defaulted to 01 on malformed progress | Strict progress validation, portable CLI tests and a CI integrity workflow; retain devcontainer |

## Lesson inventory
All 20 original chapters were short template drafts with the same missing example/walkthrough/debugging/assessment structure; 01 alone is upgraded in this change. Original topic paragraphs and intended assignments remain available for 02–20, not represented as completed teaching material.

| Lessons | Specific authoring gap / next gate |
| --- | --- |
| 02–05 | Collection, function, class/type/error and file/CLI topics need progressive explanations, validation contracts and separate acceptance suites |
| 06–08 | Git artifact evidence, reproducible bugs/logging and fixture/mock/regression tests need real walkthroughs and instructor review tasks |
| 09–10 | HTTP/status contracts, dependency/persistence lifecycle and parameterized SQL need runnable local service examples and isolated tests |
| 11–12 | Adapter/schema/cost and tool dispatch need mock fixtures, failure behavior and explicit LangChain coverage |
| 13–15 | Stateful graph, reliability/approval and MCP need state/authorization contracts and deterministic simulations |
| 16–18 | Retrieval, eval quality gates and model selection need datasets, numeric examples and ADR/evaluation rubrics |
| 19–20 | Docker/deployment and capstone need reproducible commands, smoke/failure checks and an independent change simulation |

## Link audit limits
See LINK_AUDIT.md for all currently assigned external URLs. No checked URL returned 404 in this run; redirects and HTTP 200 do not prove content relevance or free access. The original Lesson 01 Codecademy link was replaced with focused Python documentation, not diagnosed as broken. All authored relative Markdown links are checked offline. Runtime links and optional subscriptions are not silently assumed to work.
