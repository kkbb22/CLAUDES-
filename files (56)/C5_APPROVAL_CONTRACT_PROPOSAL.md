# C5 — Human-Operator Control Specification and Approval Contract Proposal

**Cloud:** C5 — ARGON Human Operator Control & Approval Architect · **System:** ARGON-AI-OS only · **Date:** 2026-11-05
**Status:** PROPOSAL. `DESIGNED` · `NOT_IMPLEMENTED` · no test executed. Nothing here is a policy, approval or authorization. Open values are `REQUIRES HUMAN DECISION` and are tracked in `C5_THRESHOLD_DECISION_REGISTER.md` (TH-nn).
**Inputs (labels):** C5 v4 research (VERIFIED, hash matches manifest) · C2 RP-13 plan and HD-1..HD-15 (SOURCE-ASSERTED, in `c2-c6.TXT`) · C6 FCP-C6-EVAL-002/003 (VERIFIED present; hash matches manifest; manifest says `STAGING_CANDIDATE_NOT_ACCEPTED_NOT_MERGED`) · synthesis v2.1.2 gate G-8 and XC-RESUME (VERIFIED present) · AI-OS runtime at `1458a7f5…` (VERIFIED by static read).
**Label note:** the directive calls G-08 a "C6 finding". In the supplied files `G-8` is a Wave 4 precondition gate in the cross-cloud synthesis v2.1.2 (`C1-E4` executed and `XC-RESUME` designed and tested; status `NOT MET`). C6's matching work is FCP-C6-EVAL-003. No file labelled "G-08" exists. This document uses G-8 as found.

## 1. Authority principle (carried from C5 v4)

Display and Guidance may live in a UI. Decision, Authorization and Enforcement live only in a trusted backend. A click, dialog, checkbox, CLI invocation or audit log line is a **request** or a **record**, never authorization. A label such as `operator` or `local-operator` is not an authenticated identity.

## 2. Approval object — proposed fields

The object is created only by a trusted authorization service after an authenticated decision event. "Source" shows where the need is stated; "Current" is the static read of `policy.py` `ApprovalRecord` at AI-OS `1458a7f5…`.

| # | Field | Binds | Rule (proposal) | Source | Current (VERIFIED static) | Open decision |
|---|---|---|---|---|---|---|
| F01 | `schema_version` | contract revision | Verifier refuses unknown versions | C4 ENG-001 sc.11 analogy (INFERRED) | absent | none |
| F02 | `approval_id` | the approval | Unique, unguessable | C2 | present | none |
| F03 | `approver_principal_id` | **approver** | Derived by the authorization service from an authenticated session, never from caller input | C2 Q2 identity binding | `approver` is a caller-supplied string | TH-16 |
| F04 | `approver_identity_source` + `assurance_level` | **identity** | Records how identity was established (for example "service-authenticated") | C5 charter item 7 (proposal) | absent | TH-16 |
| F05 | `requester_principal_id` | who asked | Authenticated; needed for role separation | C5 charter item 4 (proposal) | absent | TH-15 |
| F06 | `executor_principal_id`, `verifier_principal_id` | roles | Recorded when policy needs separation; may be filled at Act/Verify | C5 charter item 4 (proposal) | absent | TH-15 |
| F07 | `action_type` and `action_id` | **action** | Exact action, not a category (unless TH-09 selects persisted scope) | C2 RP-13; H-04 | action list inside plan digest | TH-09 |
| F08 | `target` = repository, immutable ref, path or resource, environment | **target** | Immutable reference, never a branch name alone | C5 charter item 2 | paths only | none |
| F09 | `payload_hash`, `hash_alg`, `canonical_form_id` | **payload hash** | Hash over the canonical form of the exact payload including content, commands, parameters, timeouts | C2 RP-13 `artifactHash`; Q6 | `plan_digest` over contract (VERIFIED) | TH-14 |
| F10 | `displayed_content_hash` | what the operator **saw** | Hash of the rendered review view; must equal the hash of a view derived from F09 bytes | C2 Q6 P6.5 'display derives from signed bytes' (SOURCE-ASSERTED) | absent | TH-14 |
| F11 | `scope` and `unit_of_binding` | **scope** | `once` (single execution) or an owner-defined persisted scope; unit = action, action set or plan | C2 HD-1, HD-2; RP-13 `scope` | `scope` is free text from the contract | TH-09 |
| F12 | `issued_at`, `not_before`, `expires_at` | **expiry** | Enforced at point of use by a trusted time source; bound cannot be extended by the presenter | C2 Q4; RP-13 `expiresAt` | `issued_at`, `expires_at` present; no cap | TH-06, TH-13 |
| F13 | `nonce` | replay | Unique; consumption recorded atomically; fail-closed if the journal is unavailable | C2 Q3; RP-13 `nonce` | present; journal fails open (VERIFIED static) | TH-11 |
| F14 | `policy_id`, `policy_version` | **policy version** | Identifies the rule set that required and permitted the approval | C5 charter item 7 (proposal) | absent | owner |
| F15 | `decision` | decision | One of `APPROVED`, `REJECTED`, `CHANGES_REQUESTED`, `DEFERRED`; derived states `EXPIRED`, `REVOKED`, `CONSUMED` | C5 charter item 5 | declared, only approve and consume reachable | owner vocabulary |
| F16 | `decision_reason` | accountability | Required for reject, changes, emergency actions | C5 charter item 7 | absent | none |
| F17 | `revocation_state` and `revoked_at` | revocation | Server-side; checked at consume time | C2 Q5; HD-7 | absent | TH-10 |
| F18 | `consumed_at`, `execution_id` | single use | Links approval to the one execution | C2 Q3 | `consumed_at` present | none |
| F19 | `signer_key_id`, `signature` | record authenticity | **Only if** the owner selects cryptographic binding; otherwise the record is trusted-store only and labelled "unbound" | C2 RP-13 sample fields (SOURCE-ASSERTED), HD-3, HD-4 | absent; record trusted by file presence | TH-18 |

**Verification rule (proposal):** Act refuses with a reason code when any required field is missing or malformed, when the presented action's canonical digest differs from F09, when F12 has lapsed, when F13 is consumed or unknowable, when F17 is revoked, or when F03/F05/F06 violate the owner's role rule. Candidate reason codes follow C2's closed set: `BIND_MISMATCH`, `EXPIRED`, `NOT_YET_VALID`, `REPLAY`, `STATE_UNAVAILABLE`, `IDENTITY_MISMATCH`, `NOT_AUTHORIZED_FOR_ACTION`, `KEY_REVOKED`, `SIG_INVALID`, `MALFORMED` (SOURCE-ASSERTED, C2 `E4` proposal).

## 3. Operator journey — Plan → Review → Approval → Act → Verify

| Stage | Operator sees (Display) | Operator decides | Backend must (Enforcement) |
|---|---|---|---|
| **Plan** | Objective, scope, planned actions, risk class, reason a gate applies | Nothing authorizes yet; may edit, discard, submit | PLAN has no mutation-capable path (C6 T6-002-01); plan digest computed |
| **Review** | Every changed path/resource with exact content or diff; commands verbatim; repo, immutable ref, environment; reversibility and external effect in words; uncertainty; roles; digest and expiry; any hash-covered field not shown is labelled "not shown" | Approve, Reject, Request changes, Defer. Default focus is Reject or Defer, never Approve | Review view derived from the same bytes that F09 hashes; F10 recorded |
| **Approval** | Result stated as "approval recorded" only after the service confirms; never "authorized" from UI state alone | — | Authorization service creates F01–F19 after an authenticated decision event (BE-01..BE-04) |
| **Act** | Live state re-read from enforcement state: `stop_requested`, `stopping`, `stopped`, `completed_before_stop`, `failed (with what executed)` | STOP, Revoke (before consume) | Re-verify at point of use; consume atomically before first mutation; block substituted action |
| **Verify** | Result shown as `unverified` unless independent evidence exists; self-report never shown as verified | Accept result, reopen | Verifier distinct from producer; evidence record bound to the approval |

### 3.1 Required behaviour per case (proposal; numeric values are open)

| Case | Operator-visible behaviour | Backend behaviour required |
|---|---|---|
| **Rejection** | "Rejected: this plan will not run." Reason captured | Terminal for this plan digest; any later execute is refused; new plan needs new approval |
| **Request changes** | Plan returns to editable state; old approvals shown as voided | Plan digest changes; prior approvals fail `BIND_MISMATCH` |
| **Defer** | "No decision. Nothing is authorized." | No approval created; task stays pending |
| **Timeout (expiry)** | Absolute expiry time and remaining time shown; on lapse, "expired" with consequence | Expiry enforced at Act by trusted time (TH-06, TH-13); lapse between Review and Act, or during queue delay, refuses with `EXPIRED` |
| **Cancellation (before Act)** | "Cancelled before execution. Nothing ran." | Task terminal; approval cannot be consumed |
| **Revocation (before consume)** | Revoke control; confirmation says what is invalidated | Approval invalid server-side; consume refused (`KEY_REVOKED` or revoked-state code); UI showing "approved" after revocation still cannot execute (C6 T6-002-13) |
| **Revocation in flight** | Operator told which actions already ran and which stop | Semantics owner-defined (TH-04, TH-10); until decided, no claim is made |
| **Changed payload** | "Plan changed after approval; approval void" with a diff against what was approved | Digest compare at Act; refusal `BIND_MISMATCH`; substituted action blocked, not merely logged (C6 T6-002-10) |
| **Changed state during pause** | "Working state changed while paused; resume needs review" | Stale-state resume rejected or forces re-approval; outcome recorded (XC-RESUME proposal `[PROP]`; TH-05; gate G-8 NOT MET) |
| **Backend unavailable** | "Cannot confirm authorization; nothing executed" | Fail-closed or per-class availability rule (TH-11) |

## 4. Backend enforcement requirements (UI is not authorization)

| ID | Requirement | Evidence that would demonstrate it |
|---|---|---|
| BE-01 | Only the authorization service can create or alter an approval record; UI, CLI and executor have no write path to it | Write-path analysis; attempt by an unprivileged writer is refused |
| BE-02 | Approver identity is derived from an authenticated session by the service; caller-supplied labels are ignored | Denial of `--approver admin`-style input without authentication |
| BE-03 | Approval authenticity does not rest on file presence: integrity or authenticity of the record is verifiable (mechanism reserved: TH-18, C2) | Tamper test on a stored record |
| BE-04 | Single-use consume is atomic and fail-closed; replay state loss blocks execution | Concurrent-consume and corrupted-journal tests (C6 EVAL-003 neighbourhood; C2 Q3) |
| BE-05 | Digest, expiry, revocation and role checks run at **point of use**, not at display | Queue-delay and TOCTOU vectors (C2 T4-06) |
| BE-06 | A UI that shows "approved" while enforcement state is absent, revoked or expired cannot cause execution | C6 T6-002-13 with mutant M-002b |
| BE-07 | A mismatching action is blocked and the operator is told what differed | C6 T6-002-10 |
| BE-08 | The review view is derived from the bytes hashed in F09; F10 is recorded | Display-to-record parity (AT-03) |
| BE-09 | Every decision, refusal and consume emits a record that names principal, digest, policy version and time; the log is audit evidence, not the authorization event | Record export; tamper detection |
| BE-10 | Exactly one approval surface can enable a mutation | Path analysis of all mutation routes (not done; the repo has two approval paths) |

## 5. STOP semantics (proposal)

Division of ownership: **C4 defines what STOP does** at each lifecycle point (AT-07, IC-3, IC-4); **C5 specifies what the operator is told**; **C6 measures** (T6-003-07). C5 sets no latency.

1. STOP is a request, never a result. The operator sees five distinct states: `stop_requested`, `stopping`, `stopped`, `completed_before_stop`, `stop_failed`. STOP is never silently queued or ignored (C6 gate G3-5 target: 0 silently ignored STOPs).
2. On `stopped`, the UI states the last completed action, the first action that did not run, and any residual side effects from an executor inventory independent of the UI (IC-3).
3. Before approval, the operator is told which actions cannot be stopped or undone mid-run.
4. A STOP that arrives after the mutation point reports `completed_before_stop`, not a failure to stop.
5. After STOP, **no approval is assumed to survive**. Whether and when it may be reused is the XC-RESUME / G-8 question; C1's no-survival position is untested (TH-05).
6. Emergency-stop authority and escalation: TH-17.
7. Latency bound: **REQUIRES HUMAN DECISION** (TH-03, gate G3-6). Stale-display propagation bound: **REQUIRES HUMAN DECISION** (TH-12).

## 6. Mapping to C6 EVAL-002 and EVAL-003 (no execution claimed)

See `C5_OPERATOR_ACCEPTANCE_MATRIX.csv`. Summary of what the sources themselves establish:

| C6 vector | Cites C5 source ID | Maps to C5 test (per the AT coverage map) | Label |
|---|---|---|---|
| T6-002-10 (approve A, substitute B) | T3.2, E3 | AT-11 (backend), AT-10 (human) | SOURCE-ASSERTED |
| T6-002-13 (UI shows approved after revocation) | E8 | AT-12 | SOURCE-ASSERTED |
| T6-003-07 (STOP at each stage) | E4 | AT-07 | SOURCE-ASSERTED |
| T6-003-08 (zero duplicates, zero orphaned approvals) | E5 | AT-08 | SOURCE-ASSERTED |
| T6-002-11, T6-003-11, T6-003-04, T6-002-14 and others | none by ID | AT-04/05/06/09/12 and NEW-C5 rows | INFERRED |
| none | — | AT-01, AT-02, AT-15; NEW-C5-05, NEW-C5-06 | **no EVAL-002/003 vector (gap)** |

C6 states its whole execution is `BLOCKED` on the Wave 4 runtime, which does not exist, and that T6-002-11 is `BLOCKED` on the C2 binding design.

## 7. What this proposal does not do

It selects no threshold, role rule, scope policy, signing mechanism, expiry value or STOP latency. It does not claim the runtime meets any requirement. It authorizes nothing and implements nothing. It does not authorize Wave 4 (gate G-0 NOT MET), machine writes to ARGON-HEALTH, or changes to Legacy ARGON.
