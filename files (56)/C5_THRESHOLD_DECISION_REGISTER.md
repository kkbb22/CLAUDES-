# C5 — Threshold and Policy Decision Register

**Status:** PROPOSED REGISTER. Every value is **REQUIRES HUMAN DECISION**. C5 chooses no threshold, recommends none, and marks none approved.
**Date:** 2026-11-05 · **Cloud:** C5 · **Mode:** READ-ONLY

Observed implementation defaults are listed only so the owner knows they exist. They are not decisions and must not be read as accepted values.

| ID | Parameter | Value | Used by | Decision owner (per source) | Source / evidence label | Observed default (not a decision) |
|---|---|---|---|---|---|---|
| TH-01 | Participant count and comprehension pass rate for human studies | **REQUIRES HUMAN DECISION** | AT-01, AT-02, AT-10 (E1, E2, E3) | C6 (methodology) + owner sign-off | C5 AT doc section 1.3 (SOURCE-ASSERTED); C6 sets no thresholds | none observed |
| TH-02 | Burst size and pacing for the accidental-approval test | **REQUIRES HUMAN DECISION** | AT-02 (E2) | C6 / C5 owner decision | C5 AT doc section 1.3 (SOURCE-ASSERTED) | none observed |
| TH-03 | STOP latency bound (STOP issued to confirmed halt) | **REQUIRES HUMAN DECISION** | AT-07, T6-003-07, gate G3-6 | C4 (mechanics) + human owner | C6 gate G3-6 'THRESHOLD NOT SET (human owner)' (VERIFIED in C6 pack text) | none observed |
| TH-04 | In-flight semantics: what 'in-flight' means; abort vs finish the atomic step vs quarantine | **REQUIRES HUMAN DECISION** | AT-07, NEW-C5-04 | C4 + human owner | C2 HD-7 (SOURCE-ASSERTED) | none observed |
| TH-05 | Resume policy: may stale state be resumed; what invalidates a checkpoint; must approval be re-obtained after a state change (XC-RESUME) | **REQUIRES HUMAN DECISION** | AT-08, NEW-C5-08, synthesis gate G-8 | C1/C4/C3 + human owner (IC-5 owner unresolved) | Synthesis v2.1.2 XC-RESUME: 'no source-specified acceptance criteria'; C1 no-survival-of-approval position untested | none observed |
| TH-06 | Approval validity window and semantics (start-by vs complete-by), by impact class | **REQUIRES HUMAN DECISION** | AT-08, AT-12, NEW-C5-03 | C2 + human owner | C2 HD-6 (SOURCE-ASSERTED) | Observed code default 300 s (core runtime) and 600 s (standalone runtime) at AI-OS 1458a7f (VERIFIED static read). These are implementation defaults, NOT decisions, and are not endorsed. |
| TH-07 | Tolerated approval rate of seeded mismatched actions (human arm) | **REQUIRES HUMAN DECISION** | AT-10 (E3) | C6 + human owner | Metric defined in C5 v4 E2/E3; value not set | none observed |
| TH-08 | Consecutive auto-approval threshold before forced human approval | **REQUIRES HUMAN DECISION** | AT-06 (T2.1) | C2 (policy) + human | C5 AT doc section 1.3; C2 RP-4 | none observed |
| TH-09 | Approval scope: single-use vs persisted category; unit of binding (action / action set / plan) | **REQUIRES HUMAN DECISION** | AT-05, NEW-C5-01, NEW-C5-02 | Human owner (C2 records REQUIRES HUMAN DECISION) | C2 HD-1, HD-2 | Core runtime issues single-use approvals (consumed flag + nonce) at 1458a7f (VERIFIED static read). Not a recorded policy decision. |
| TH-10 | Revocation mechanism and maximum staleness of revocation state | **REQUIRES HUMAN DECISION** | AT-12, NEW-C5-04 | C2 + human owner | C2 HD-7; 'UNKNOWN' in C2 artifact | none observed |
| TH-11 | Fail-closed vs availability when authorization, replay or revocation state is unreachable, per impact class | **REQUIRES HUMAN DECISION** | AT-09 | C2 + human owner | C2 HD-8 | none observed |
| TH-12 | Stale-display propagation bound (maximum age of operator-visible approval state) | **REQUIRES HUMAN DECISION** | AT-12 | C4/C2 + human owner | C5 AT doc section 1.3 'stale-state propagation bound' | none observed |
| TH-13 | Trusted time source and tolerated clock skew | **REQUIRES HUMAN DECISION** | NEW-C5-03 | Human owner (operational) | C2 HD-13 | none observed |
| TH-14 | Canonical form of the approved payload and display truncation rule (maximum payload shown without truncation) | **REQUIRES HUMAN DECISION** | AT-03, NEW-C5-02 | C2 (canonical form) + C5 (display rule) + human owner | C2 HD-9; truncation limit is a new C5 question (UNSOURCED) | Standalone runtime caps content at 100,000 bytes (VERIFIED static read). Not a decision about display or truncation. |
| TH-15 | Separation-of-duties rule across requester, reviewer, approver, executor, verifier | **REQUIRES HUMAN DECISION** | NEW-C5-06 | Human owner | C5 charter item 4 (UNSOURCED as a numbered rule) | none observed |
| TH-16 | Who may approve and required identity assurance for the approver | **REQUIRES HUMAN DECISION** | NEW-C5-07 | C2 (mechanism) + human owner | C2 HD-4, HD-5 | none observed |
| TH-17 | Emergency-stop authority and escalation path | **REQUIRES HUMAN DECISION** | STOP semantics (proposal section 5) | Human owner | C5 charter section 5 (new) | none observed |
| TH-18 | Whether ARGON invests in cryptographic binding at all vs a recorded but unbound approval | **REQUIRES HUMAN DECISION** | Approval contract signature fields | Human owner | C2 HD-3; synthesis gate G-5 | none observed |
| TH-19 | Envelope for model-regenerated arguments (fresh approval or defined envelope) | **REQUIRES HUMAN DECISION** | Changed-payload behaviour | C2 + human owner | C2 HD-10 | none observed |
| TH-20 | Trial counts N and false-block tolerance for evaluation of these tests | **REQUIRES HUMAN DECISION** | EVAL-002/003 execution | C6 + human owner | C6 pack 'THRESHOLD NOT SET' (G3-4, false-block); not a C5 decision | none observed |

## Closure evidence per decision

A decision is closed only when the owner records it in a named governance artifact with date and approver, the artifact is hash-recorded, and the dependent tests in the acceptance matrix are re-labelled from BLOCKED. A test cannot return PASS on a numeric criterion while its threshold is open.

## Not set by this register

No participant counts, latencies, expiry windows, counters, roles or policies were chosen. C5 does not set project-wide approval policy (dispatch pack, C5 assignment).
