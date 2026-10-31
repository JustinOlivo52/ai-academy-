# Project 1 — Ticket processor

Business request: a fictional support team receives tickets with ID, title, urgency (1–5), impact (1–5), and notes. Build a CLI that validates, classifies, and exports ticket summaries as JSON. No LLM required.

Acceptance criteria: unique IDs, clear validation failures, deterministic priorities, JSON export, at least 5 tests, helpful README.

Sample rule: priority is HIGH when urgency >= 4 AND impact >= 4; MEDIUM if either >= 3; otherwise LOW. Document alternatives if you change the rules.

Use `sample_tickets.json`. Never copy real work or medical data into this project.


## Lesson integration
Lesson 01 now teaches urgency/impact priority decisions and a pure urgency summary, with independent contracts and acceptance suites outside student_work. Its worked example covers waiting-time escalation and the guided lab previews a batch. It does not yet validate IDs. Lesson 02 adds indexing; 03 refactors learner-authored priority logic into reusable interfaces; 04 adds validation/types; 05 adds JSON/CLI. Later engineering lessons bring those learner-authored pieces into a tested service. Do not replace student code with a course-author solution.
