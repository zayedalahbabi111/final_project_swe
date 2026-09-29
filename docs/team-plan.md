# Project Management & Team Plan
## Responsibilities
- Zayed — Product & Requirements: scope, stakeholders, FR/NFR, stories, traceability, integration, final documentation.
- Aktore — Backend/API: FastAPI, contracts, authz, persistence, PoC backend/tests.
- Rowda — Frontend/Collaboration: React, rich text, WebSocket client, collaboration UX/tests.
- Fatima — AI/Moderation/Architecture: AI workflow, moderation, ERD, diagrams, ADRs/tests.

## Git workflow
Issue → feature branch → implementation → tests → pull request → review → merge. Suggested branches: feature/requirements-zayed, feature/backend-aktore, feature/frontend-rowda, feature/ai-moderation-fatima. Main is integrated work.

## Change log
Scope/requirement changes use GitHub issues and update requirements + traceability. Architecture changes require an ADR update/new ADR.

## Methodology
Five Scrum-inspired iterations: foundation; core social network; collaboration; moderation/AI; integration/testing.

## AI tool review
AI may help draft code/docs/tests. A human reviews generated artifacts; executable artifacts are tested; contributors must understand their work. AI is not used during the oral exam.

## Risks
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| LLM unavailable | Medium | Medium | Manual editing + mock |
| Unauthorized exposure | Medium | High | Server authz + tests |
| WebSocket conflict | Medium | High | Versioning + sequence test |
| DB outage | Low | High | Transactions + recovery |
| Scope creep | High | Medium | Bounded release |
| Merge conflicts | Medium | Medium | Small branches + review |
| Incorrect AI | Medium | Medium | Human approval |
| Member unavailable | Medium | Medium | Cross-training |
| Security defect | Medium | High | Authz tests |

## Assignment 2 timeline
Week 1 repo/requirements/diagrams; Week 2 backend/API/tests; Week 3 React/integration; Week 4 PostgreSQL/auth; Week 5 WebSockets/conflicts; Week 6 moderation/audit; Week 7 LLM adapter/human approval; Week 8 security/performance/accessibility/final demo. Each milestone is verifiable by PR, tests or demo.