# ADR-002: PostgreSQL Persistence
Status: Accepted
Context: UniBoard needs relational memberships, content, reports, audit and transactional draft versions.
Decision: Use PostgreSQL.
Consequences: Strong integrity and transactions; more deployment work than the in-memory PoC.