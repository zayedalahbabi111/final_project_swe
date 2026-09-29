# Requirements Engineering

## Stakeholders
| Stakeholder | Goals | Concerns | Influence | Conflict |
|---|---|---|---|---|
| Students | Discover communities, publish and discuss | Privacy, harmful content, ease | High | Visibility vs privacy |
| Club Administrators | Manage communities and announcements | Publishing control, concurrent editing | High | Speed vs review |
| Moderators | Review reports and enforce policy | Evidence, auditability, consistency | High | Speed vs fairness |
| University Administration | Safe, reliable, compliant service | Student-data protection, availability | High | Features vs governance |

## Functional requirements
- FR-01: Authenticate users through the university identity mechanism.
- FR-02: Assign Student, Club Admin or Moderator role.
- FR-03: Students browse communities.
- FR-04: Students join communities.
- FR-05: Members leave unless this would remove the last administrator.
- FR-06: Club Admins manage community name, description and membership.
- FR-07: Authenticated users create text posts with selected audience.
- FR-08: Club Admins create official announcements.
- FR-09: Authors edit/delete unpublished content they own.
- FR-10: Only authorized Club Admins publish announcements.
- FR-11: Published content shows author and creation time.
- FR-12: Posts may target the whole university.
- FR-13: Posts may target one community.
- FR-14: Backend enforces authentication, role and audience membership.
- FR-15: Users comment/delete own comments; Club Admins disable announcement comments.
- FR-16: Two or more Club Admins edit an announcement draft through WebSockets.
- FR-17: Accepted draft updates broadcast to authorized editors.
- FR-18: Collaborative updates carry a version; matching current version is accepted.
- FR-19: Stale updates are rejected and latest version is returned.
- FR-20: Users report posts/comments using defined reasons.
- FR-21: Moderators view open reports and reported content.
- FR-22: Moderators dismiss or remove reported content.
- FR-23: Moderation decisions record moderator, decision, reason and time.
- FR-24: Content owners receive moderation outcomes.
- FR-25: AI returns an improved announcement draft.
- FR-26: AI returns a shorter version on request.
- FR-27: AI suggests a title.
- FR-28: AI identifies missing event information.
- FR-29: AI receives only draft/task data, not profiles/private/moderation data.
- FR-30: AI suggestions require human approval.
- FR-31: AI failure leaves manual editing/publishing available.

## Non-functional requirements
- NFR-01: 95% of normal API requests <500 ms under 100 concurrent users.
- NFR-02: 95% of accepted draft updates visible <1 second under first-release load.
- NFR-03: 99.5% monthly availability excluding planned maintenance.
- NFR-04: Recoverable service failure restored within 15 minutes.
- NFR-05: Every protected endpoint enforces server-side authentication/authorization.
- NFR-06: Community content is never returned to non-members.
- NFR-07: 100% of resolved moderation decisions retain audit fields.
- NFR-08: Primary actions are keyboard accessible and controls have labels.
- NFR-09: Signed-in student creates a post within five primary steps.
- NFR-10: Application tier is stateless for horizontal scaling.

## User stories and acceptance criteria
### US-01 Student publishing
As a Student, I want to publish a university post.
- Valid student + valid content + University audience → post created with author/time.
- Missing content → validation error and no post.

### US-02 Community privacy
As a Student, I want community-only visibility.
- Member → post returned.
- Non-member → authorization error and no content.

### US-03 Collaborative announcement
As a Club Admin, I want to edit with another admin.
- Two authorized admins, first sends version N → both receive N+1.
- Stale N → rejected with latest state.
- Unauthorized connection → rejected.

### US-04 Moderation
As a Moderator, I want to review a report.
- Remove → report resolved and audit record contains moderator, decision, reason and time.
- Dismiss → content remains and dismissal is recorded.

### US-05 AI assistant
As a Club Admin, I want announcement suggestions.
- Improve → suggestion returned without publishing.
- LLM unavailable → manual editing remains available.
- Suggestion → cannot become official until approved.

## Validation, assumptions, open questions
Validation checks: observable behavior, measurable quality targets, explicit conflicts, normal/failure/policy stories and traceability.
Assumptions: one university; signed-in users; fictional PoC identities; each community has an admin; human AI review; external services may be mocked; no paid APIs.
Open questions: exact identity protocol; moderation retention; final content policy; maximum community size; production LLM/data-processing agreement; moderator removal scope.