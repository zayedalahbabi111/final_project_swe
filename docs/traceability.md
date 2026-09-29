# Requirements Traceability Matrix
| Stakeholder need | Requirements | Story/scenario | Architecture |
|---|---|---|---|
| Identity/access | FR-01, FR-02, NFR-05 | US-01 auth | Auth + Authorization |
| Communities | FR-03–FR-06 | join/leave | Community |
| Publishing | FR-07, FR-09, FR-11–FR-14 | US-01 | Content + Authorization |
| Privacy | FR-12–FR-14, NFR-06 | US-02 failure | Authorization + Persistence |
| Collaboration | FR-08, FR-10, FR-16–FR-19, NFR-02 | US-03 | Collaboration + Content |
| Discussion | FR-15 | comment/delete/disable | Content |
| Moderation | FR-20–FR-24, NFR-07 | US-04 | Moderation + Persistence |
| AI | FR-25–FR-31 | US-05 | AI Assistant |
| Reliability | NFR-01–NFR-04, NFR-10 | failure/recovery | API + DB |
| Accessibility | NFR-08, NFR-09 | US-01 | Frontend |

## Component ownership
| Component | Requirements | Owner |
|---|---|---|
| Authentication | FR-01,02,NFR-05 | Aktore |
| Communities | FR-03–06 | Aktore |
| Content | FR-07–15 | Aktore + Rowda |
| Authorization | FR-12–14,NFR-06 | Zayed + Aktore |
| Collaboration | FR-16–19,NFR-02 | Rowda |
| Moderation | FR-20–24,NFR-07 | Fatima |
| AI Assistant | FR-25–31 | Fatima |
| Persistence | NFR-01–07 | Aktore + Fatima |
| Frontend | NFR-08–09 | Rowda |
| Integration/docs | cross-cutting | Zayed |