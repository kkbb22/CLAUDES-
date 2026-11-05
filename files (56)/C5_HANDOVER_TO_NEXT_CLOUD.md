# C5 — Handover to the Next Cloud (2026-11-05)

**Identity charter (keep in session context; repeat in any handover):** `ARGON_CLOUD_IDENTITY_C5` — **C5, ARGON Human Operator Control & Approval Architect.** Responsibility: define and evaluate how accountable humans understand, review, approve, reject, revoke and supervise consequential actions (operator experience, approval comprehension, provenance, role separation, escalation, human factors, acceptance testing). Boundaries: does not authenticate identities by UI appearance, implement, choose policy without the accountable owner, set thresholds, or issue C7's independent verdict. READ-ONLY. **Persistence: session-only; not saved to persistent memory.**

**Systems kept separate:** ARGON-AI-OS (in scope); ARGON-HEALTH (not touched); Legacy ARGON (not inspected).

## State
- Deliverables this turn: approval contract proposal, operator acceptance matrix (15 specified AT rows plus 8 NEW unsourced rows, mapped to C6 EVAL-002/003), threshold register (20 items, all REQUIRES HUMAN DECISION), provenance report, two derived byte-extracts.
- Earlier-turn deliverables remain in place, unrevised: the static runtime review (CORE-01..11), 18-row OC catalog (fresh, not r3), decisions register DEC-01..12, requirements, evidence status.
- Test state: SPECIFIED only. Implemented as C5 tests: none. Executed: 0. Passed with evidence: 0.

## Facts the next Cloud must carry
1. r3 (18 tests) and v1 bytes are NOT RECOVERED. A 15-test specification (AT-01..15, 2026-10-13) exists as a derived extract; relationship to r3 UNKNOWN. Nothing relabelled.
2. `G-08` does not exist by that name; `G-8` is a synthesis Wave 4 gate (NOT MET).
3. C6 EVAL-002/003 execution is BLOCKED (no Wave 4 runtime). C6 manifest says staging candidate; acceptance record not supplied.
4. Runtime observations at AI-OS `1458a7f5…`: approver is a caller-supplied string, approval record trusted by file presence, nonce journal fails open, CLI approve has no confirmation step, no operator reject/revoke/stop path found (static read, not executed).

## Open dependencies
| Item | Owner | Closure evidence |
|---|---|---|
| TH-01..TH-20 | Human owner (with C2, C4, C6 as named) | Recorded governance decision, dated, hashed |
| r3 / v1 / 15-test manifest / run logs | Human owner, C1 | Files with hashes or explicit confirmation of absence |
| IC-1, IC-2 authorization record and fail-closed signal | C2 | Canonical schema document |
| IC-3, IC-4 lifecycle events and cancellation semantics | C4 | Canonical spec |
| IC-5 pause/resume owner; gate G-8 | C1/C2/C4 + owner | Named owner and designed-and-tested XC-RESUME |
| Coverage gaps: rejection finality, separation of duties | C6 | New vectors or owner waiver |

## Not authorized
Any implementation, policy approval, threshold choice, repository change, commit, push, PR, merge, deployment, runtime execution, Wave 4 (G-0 NOT MET), machine write to ARGON-HEALTH, or change to Legacy ARGON.
