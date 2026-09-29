# Data Model / ERD
USER(id PK, university_id UNIQUE, display_name, role, created_at)
COMMUNITY(id PK, name, description, created_by FK USER, created_at)
MEMBERSHIP(user_id FK USER, community_id FK COMMUNITY, role, joined_at, PK(user_id, community_id))
POST(id PK, author_id FK USER, community_id FK COMMUNITY nullable, audience_type, content, status, created_at, updated_at)
COMMENT(id PK, post_id FK POST, author_id FK USER, content, created_at, deleted_at)
REPORT(id PK, reporter_id FK USER, target_type, target_id, reason, status, created_at)
MODERATION_DECISION(id PK, report_id FK REPORT, moderator_id FK USER, decision, reason, decided_at)
ANNOUNCEMENT_DRAFT(id PK, community_id FK COMMUNITY, created_by FK USER, content, version, status, updated_at)
AI_SUGGESTION(id PK, draft_id FK ANNOUNCEMENT_DRAFT, task, suggestion, approved_by FK USER nullable, created_at)

Relationships: USER↔COMMUNITY through MEMBERSHIP; USER→POST; COMMUNITY→POST; POST→COMMENT; USER→COMMENT; REPORT→MODERATION_DECISION; COMMUNITY→DRAFT; DRAFT→AI_SUGGESTION.
Integrity: composite membership key; community audience requires community_id; published announcements require authorized admin; moderation decisions require moderator; draft version increments transactionally.