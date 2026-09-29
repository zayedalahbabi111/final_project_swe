# ADR-003: WebSockets for Collaboration
Status: Accepted
Context: Club admins need near-real-time announcement editing.
Decision: Use authenticated WebSockets with optimistic versioning.
Consequences: Low-latency updates; reconnect and conflict handling are required.