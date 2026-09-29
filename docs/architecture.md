# System Architecture

## Ranked architectural drivers
1. Security/audience authorization
2. Privacy
3. Real-time collaboration
4. Scalability
5. AI integration/data minimization
6. Availability/recovery
7. Moderation auditability
8. Usability/accessibility

## C4 Context
Actors: Student, Club Administrator, Moderator, University Administration. External systems: University Identity Provider and LLM Provider. System: UniBoard.

## C4 Container
React Frontend communicates with FastAPI Backend over HTTPS REST and WebSockets. Backend uses PostgreSQL and an LLM Provider.

## Components
Auth, Authorization, Community, Content, Collaboration, Moderation, AI Assistant and Persistence. Only Persistence talks directly to PostgreSQL.

## Behavior
1. Request enters through REST or authenticated WebSocket.
2. Authentication identifies user.
3. Authorization checks role, ownership and audience membership.
4. Domain service performs operation.
5. Persistence commits.
6. Response/event returns.
7. Collaboration compares client version: match → accept/increment; stale → reject with latest.

## Authorization
Students read university posts and community posts only when members. Club Admins manage only administered communities. Only authorized Club Admins publish. Moderators access moderation queues/audit. AI receives draft/task only.

## Failures
401 unauthenticated; 403 unauthorized; 404 missing/hidden resource; 409 stale collaboration; 422 invalid request; 5xx service failure. WebSocket disconnect triggers reconnect/reload. DB failure fails writes safely. AI failure never blocks manual editing.

## Technology
React + rich text; FastAPI/Python; WebSockets; PostgreSQL; external LLM. PoC uses FastAPI + minimal HTML/JS.

## Interface contract
POST /posts request:
{"content":"Welcome to the club","audience_type":"UNIVERSITY","community_id":null}
201 response:
{"id":"p_001","content":"Welcome to the club","author_id":"u_001","audience_type":"UNIVERSITY","community_id":null,"created_at":"2026-09-29T10:00:00Z"}
Failures: 400 business data; 401 unauthenticated; 403 unauthorized; 422 malformed; 500 service failure.

Other REST: GET /communities; POST /communities; POST /communities/{id}/members; DELETE /communities/{id}/members/me; GET /posts; POST /posts/{id}/comments; POST /reports; GET /moderation/reports; PATCH /moderation/reports/{id}; POST /announcements; POST /announcements/{id}/publish; POST /ai/announcement/suggest.
WebSocket: /ws/announcements/{draft_id}; edit includes version; server returns update or conflict.

## Secrets
Secrets use environment variables; .env ignored; .env.example committed. PoC needs no keys.