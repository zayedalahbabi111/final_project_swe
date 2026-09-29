# Rubric Audit — Assignment 1

## Section 1 — Requirements Engineering (30%)
- Stakeholders: PASS — 4 stakeholders with goals, concerns, influence and conflicts.
- Functional requirements: PASS — identity, communities, publishing, real-time collaboration, audience control, interaction, moderation and AI.
- Observable/testable behavior: PASS — requirements and acceptance criteria use observable outcomes.
- Behavior vs design/technology: PASS — requirements are behavioral; architecture separately records React/FastAPI/WebSockets/PostgreSQL/LLM.
- Measurable NFRs: PASS — latency, availability, recovery, security, privacy, auditability, accessibility, usability and scaling targets.
- User stories: PASS — 5 stories across stakeholders, including normal, failure, concurrency and policy cases.
- Acceptance criteria: PASS — each story has explicit outcomes.
- Validation/assumptions/open questions: PASS.
- Traceability: PASS — stakeholder needs → requirements → stories/scenarios → architecture components.

## Section 2 — System Architecture (45%)
- Architectural drivers ranked: PASS.
- C4 Context: PASS.
- C4 Container: PASS.
- C4 Component: PASS.
- Diagram explanations/boundaries/responsibilities/communications: PASS.
- Technology choices: PASS and aligned with Assignment 2 constraints.
- Authorization/publishing/collaboration/live updates/moderation/appeals/AI/failures/trade-offs: PASS at Assignment 1 design level.
- UML sequence for collaborative interaction with concurrency/failure: PASS.
- Component ownership/development/testing: PASS.
- Interfaces with endpoint/event/data/response/auth/failure details: PASS for primary contract and planned interfaces.
- Repository structure and secrets: PASS.
- ERD/data model: PASS.
- Four ADRs from different parts: PASS.

## Section 3 — Project Management (15%)
- Team structure/responsibilities/codebase: PASS.
- Git/GitHub workflow, branches, PRs, review, issues/task tracking: documented PASS; real member PR history still must be created by the team.
- Decision/requirement change logging: PASS.
- AI development-tool review/testing/understanding: PASS.
- Methodology and iterations: PASS.
- Feedback/testing/documentation approach: PASS.
- Risks with likelihood/impact/mitigation: PASS.
- Assignment 2 timeline with verifiable milestones: PASS.

## Section 4 — Proof of Concept (10%)
- Working backend: PASS — FastAPI.
- Working browser frontend: PASS — minimal HTML/JS.
- One interface contract: PASS — POST /posts.
- Matching request/response: PASS.
- README setup/run instructions: PASS.
- Simplifications explained: PASS.
- Demo path: PASS.
- Repository/team evidence: structure PASS; genuine multi-member history still required.

## Final checks before submission
1. Wait for Build Assignment PDF workflow and confirm report/UniBoard_Assignment1.pdf appears on main.
2. Each teammate makes at least one genuine contribution/PR matching their assigned area.
3. Run the PoC and pytest locally.
4. Verify all four members can explain the whole architecture and their own contribution.
5. Give the professor/TA the repository access and submit the generated PDF plus editable diagram sources.

This audit aligns the repository to the supplied Assignment 1 brief. It cannot guarantee a particular grade because the oral examination and instructor judgment determine the final mark.