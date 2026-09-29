# AI1220 Software, Web & Mobile Engineering
## Assignment 1 — Requirements Engineering, Architecture & Proof of Concept

**Product:** UniBoard  
**Team:** Zayed Al Ahbabi, Aktore, Rowda, Fatima

### 1. Product foundation
UniBoard is a private university social network where students and clubs share posts and announcements, discuss topics, collaborate on announcement drafts and control audience visibility.

**Problem:** university information is fragmented across email, messaging and social media.

**First release:** identity and roles; communities; posts/announcements; university/community audience control; comments; collaborative drafts; reporting/moderation; human-reviewed AI announcement assistant.

**Out of scope:** anonymous accounts, DMs, payments/tickets, video hosting, emergency alerts, automatic AI publication/moderation.

### 2. Requirements engineering
Stakeholders: Students, Club Administrators, Moderators and University Administration.

The requirements catalogue contains 31 functional requirements covering identity, communities, publishing, audience control, interaction, real-time collaboration, moderation and AI, plus 10 measurable non-functional requirements covering performance, collaboration latency, availability, recovery, security, privacy, auditability, accessibility, usability and scalability.

Five user stories cover normal behavior and failure/policy scenarios: student publishing, community privacy, collaborative announcements, moderation and AI assistance. Acceptance criteria are observable and testable. Assumptions and open questions are recorded.

### 3. Architecture
Architectural drivers are ranked as security/audience authorization, privacy, collaboration, scalability, AI integration/data minimization, availability/recovery, auditability and usability.

C4 diagrams cover context, containers and backend components. The system uses React, FastAPI, WebSockets, PostgreSQL and an external LLM provider in the planned first release.

The backend performs server-side authorization and audience checks. Collaborative editing uses optimistic versioning: the first update matching the current version is accepted; stale updates are rejected with the latest state.

The interface contract includes REST endpoints and a WebSocket contract. The ERD covers users, communities, memberships, posts, comments, reports, moderation decisions, announcement drafts and AI suggestions.

Four ADRs document FastAPI, PostgreSQL, WebSockets and human-in-the-loop AI.

### 4. Project management
Zayed owns product/requirements/integration; Aktore owns backend/API/PoC backend; Rowda owns frontend/collaboration; Fatima owns AI/moderation/data/architecture.

Workflow: issue → feature branch → implementation → tests → pull request → review → merge.

The plan uses five Scrum-inspired iterations and records risks, AI-tool review, requirement/decision changes and an eight-week Assignment 2 milestone plan.

### 5. Proof of Concept
The working PoC demonstrates one complete contract:

**Browser → POST /posts → FastAPI validation → HTTP 201 → browser display**

It intentionally uses fictional user data and omits real authentication, React, PostgreSQL, WebSockets and LLM integration. These are Assignment 2 targets; the PoC proves the API/frontend contract without unnecessary implementation scope.

### 6. Oral examination
Each member has a primary ownership area, but every member is expected to understand the complete submission and explain design decisions, requirements, architecture, trade-offs, failures and the PoC.

### 7. Submission map
- Requirements: docs/requirements.md
- Traceability: docs/traceability.md
- Architecture: docs/architecture.md
- Data model: docs/data-model.md
- Project management: docs/team-plan.md
- ADRs: docs/adr/
- Editable diagrams: docs/diagrams/*.mmd
- Vector diagrams: docs/diagrams/*.svg
- PoC: poc/
- Tests: tests/
- PDF: report/UniBoard_Assignment1.pdf
