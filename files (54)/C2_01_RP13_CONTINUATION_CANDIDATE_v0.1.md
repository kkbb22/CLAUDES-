# C2 — RP-13 Continuation Candidate v0.1 (DERIVED, design-only, NOT EXECUTED)

**Classification of RP-13 (unchanged, not upgraded): `NEEDS EXPERIMENT`.** This document selects no mechanism, approves no policy, authorizes no execution, and does not claim any test ran. It is a **derived candidate**, not a replacement for, edit of, or successor to the unrecovered "RP-13 candidate v3".

## 0. Lineage and status of inputs
| Input | Status |
|---|---|
| RP-13 candidate v3 (hash asserted `3efe555f0b1f96f4…36e47aa6`) + its manifest | **NOT RECOVERED**; cannot be verified or diffed (C2_00 V-2) |
| Oct-13 RP-13 plan, `c2-c6.TXT` L2–565 (self-hash `635a2f83…da6dc3e` reproduced; 55 test IDs, 12 scenarios; all `TEST SPECIFIED`) | VERIFIED self-consistent; DERIVED-copy of an earlier version |
| C2 baseline research `clouds/C2/…RESEARCH.md` (`c6e95c26…0b99`), RP-13 at L790, downgrade to `NEEDS EXPERIMENT` at L1213 | VERIFIED (repo `main`@1458a7f) |
| C2 packs `capabilities/future/C2/…PACKS.md` (`8d6148bf…cc38`): SEC-002 = RP-13; manifest `DESIGNED / NOT_IMPLEMENTED / DOCUMENTATION_ONLY` | VERIFIED |
| AI-OS runtime source, PR #8 (`708142c`, merged in `1458a7f`) | VERIFIED source; behavior UNKNOWN (nothing run) |
| C1 gates `G-5` (RP-13 complete, applies only if `H-03` selects it) and `G-11` (a real implementation environment exists) | VERIFIED text, both NOT MET (v2.1.1 L353/359; v2.1.2 L354/361) |

## 1. Six-question reconciliation (as of this evidence)
Labels: DESIGNED / IMPLEMENTED-UNVERIFIED / TESTED-WITH-EVIDENCE / FAILED / UNKNOWN. "Oct-13" tests = IDs in the recovered plan. All six: **OPEN**.

| Q | Oct-13 property to prove (short) | Oct-13 closure rule | PR #8 runtime reality (static) | Label | Blocking human decisions |
|---|---|---|---|---|---|
| Q1 Key custody | signing material unreachable from Requester/Executor; verifier holds verification material only; key use attributable | C-Q1: T1-01…T1-08 PASS with mutants detected + HD-3, HD-4 recorded + custody access-list review | no keys, no signing, no registry anywhere in `runtime/` (grep) | DESIGNED (research only) | HD-3, HD-4, HD-14 |
| Q2 Authorized identity | only a registered key of an authorized identity is accepted; identity from the verified key, not metadata; no self-approval | C-Q2: T2-01…T2-08 PASS; registry not writable from Requester/Executor; HD-5 | `approver` is a free string (policy.py:57,290; cli.py:131,225; orchestrator.py:183); record is an unsigned JSON file (policy.py:236–280) | FAILED (static: control absent) | HD-5, HD-12, HD-15 |
| Q3 Replay / single-use | at most one execution across restarts, races, state loss; no cross-context reuse | C-Q3: T3-01…T3-09 PASS under proven-concurrent trials; HD-2, HD-8 | random nonce + persisted consumed set; non-atomic; reset to empty on unreadable file (policy.py:179–199, 182–190, 255, 318–337); no audience/task-context binding beyond `task_id` | IMPLEMENTED-UNVERIFIED | HD-2, HD-8 |
| Q4 Expiry | not honoured outside window at execution time; presenter cannot extend; TOCTOU handled | C-Q4: T4-01…T4-08 PASS; HD-6, HD-13 | TTL 300 s (policy.py:291) / 600 s (argon_runtime.py); checked at check/consume before run starts (policy.py:262; orchestrator.py:214); no per-action re-check, no not-before field | IMPLEMENTED-UNVERIFIED | HD-6, HD-13 |
| Q5 Revocation incl. in-flight | after revocation no new execution starts; in-flight behavior defined; outage fails closed | C-Q5: T5-01…T5-09 PASS; HD-7; unresolved limits recorded as human-accepted risk | no revoke API; CANCELLED/REJECTED only as task states (contracts.py:34–50); approval consumed before run | FAILED (static: mechanism absent) | HD-7, HD-8 |
| Q6 Exact payload binding | execution only if presented action equals approved action under a defined canonical form; display derives from signed bytes | C-Q6: T6-01…T6-13 PASS; written canonical-form rule + collision corpus; HD-1, HD-9, HD-10 | unkeyed SHA-256 over `json.dumps(sort_keys, compact, ensure_ascii=False)` of contract (contracts.py:204–245); covers actions/paths/commands/content/verification; **does not cover** repo/ref/base commit, environment/image, executor audience, approver | IMPLEMENTED-UNVERIFIED (partial) | HD-1, HD-9, HD-10, HD-11 |

Cross-cutting (Oct-13 §9): X-01…X-12 "approval issued, then something changes" must PASS for every permitted unit of binding; X-10/X-11 depend on the Plan/Act gate being the only route to mutation (`OQ-02`, never run) → until then any RP-13 result is at best `INCONCLUSIVE` (Oct-13 §4).

## 2. Decision-ready comparison of binding approaches
**Read this first.** Coverage cells are C2's **INFERRED design-level** assessment ("would this approach address the attack if implemented correctly"), never a tested result. Source support is per the Oct-13 evidence register (R1–R9): R1 RFC 9449, R2 RFC 9421 (§1–3.2.1 read), R3 RFC 8693, R4 RFC 8785 (partial), R5 RFC 7009 (excerpts), R6 NIST SP 800-57r5, R7 AgentAck README, R8 HARP samples README (self-described draft v0.2), R9 not reopened. "External precedent ≠ ARGON requirement."

Attack IDs (Oct-13 §6): AS-01 swap action · AS-02 reinterpret bytes · AS-03 TOCTOU on mutable args · AS-04 replay · AS-05 wrong task/audience/env · AS-06 expiry abuse · AS-07 executor obtains/uses signing key · AS-08 identity spoof/self-approval · AS-09 revocation failure · AS-10 display ≠ signed · AS-11 ungated path · AS-12 post-approval change. Cells: **C** addressed by design · **P** partial · **N** not addressed · **?** depends on unseen design.

| Approach | AS-01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | Source support |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **A0** Current: unkeyed SHA-256 digest + nonce file + TTL (+ typed-digest human presence in `argon_runtime.py`) | P | P | ? | P | N | P | N | N | N | ? | ? | P | repo source (VERIFIED existence; behavior UNKNOWN) |
| **A0+** A0 hardened without keys: atomic exclusive consume, fail-closed state, authenticated approver (OS/SSO identity) outside executor's write domain, wider envelope (repo/ref/env/audience/not-before), per-action expiry re-check, revocation list | C | P | P | C | C | C | N | P | P | P | ? | C | INFERRED (no external source needed; engineering control set) |
| **A1** Keyed MAC (symmetric) issued by an approval service | C | P | ? | C | C | C | P | P | P | ? | ? | C | INFERRED; no R-source read on MAC for approvals |
| **A2** Asymmetric signature over canonical payload (JCS RFC 8785 + e.g. Ed25519), key→identity registry, verifier holds public keys only | C | C | ? | C | C | C | C | C | P | P | ? | C | R4 (partial), R8 (E2/E3), R6 for lifecycle; composed construction unvalidated |
| **A3** Holder-of-key proof / signed-message profile (DPoP RFC 9449; HTTP Message Signatures RFC 9421) | C | P | ? | P | P | P | C | C | P | ? | ? | P | R1, R2 (partial read); needs HD-11 (HTTP transport) |
| **A4** Token-style approvals with exchange/revocation endpoint (RFC 8693 / 7009) | P | N | ? | P | P | C | P | P | P | N | ? | P | R3, R5 (excerpts); revocation is an authorization-server op, silent on in-flight work and offline validation (L5, INFERRED) |
| **A5** Independent witness / transparency-log tier on top of A2 (RP-14 tiers) | + | + | + | + | + | + | + | + | P | + | + | + | R9 not reopened; adds evidence-integrity, not authorization (INFERRED) |

("+" = adds nothing to authorization coverage of the base approach; A5 raises audit/evidence strength only.)

**Common residual risks for every keyed approach (Oct-13 §6, INFERRED):** a signature binds what the signing component signs — if the signing/approval UI is deceived (Oct-13 adversary A4, AS-10) or key custody is compromised (AS-07), cryptography does not help alone. AS-03 and AS-11 are execution-boundary properties, not cryptographic ones — they depend on the Plan/Act gate and isolation (C4 domain), not on which approach is chosen.

### Failure modes and operational cost (INFERRED)
| Approach | Typical failure modes | Operational cost | Key/lifecycle burden (NIST SP 800-57 topics) | Availability dependency |
|---|---|---|---|---|
| A0 | forged record by any writer; replay under concurrency/corruption; identity unprovable | lowest | none | none |
| A0+ | still bearer-trust in the approval store's access control; no non-repudiation | low–medium (engineering only) | none (but access-control lifecycle) | local state store must be reliable → HD-8 |
| A1 | verifier can forge (shared secret); service becomes high-value target | medium | generation, rotation, backup, destruction of one secret | approval service reachable |
| A2 | key theft/loss; registry tampering; canonicalization bugs (Unicode, big ints, duplicate keys — T6-06…08) | medium–high | full lifecycle per key and per approver; registry integrity | registry + revocation state (HD-8 fail-closed vs availability) |
| A3 | needs request/response transport; nonce-uniqueness enforcement is application-defined (L7); pre-generation/replay/nonce downgrade (L8) | high if no HTTP architecture exists | holder keys | nonce state, time source (HD-13) |
| A4 | revocation does not stop work already executing (L5); token exchange creates no linkage (L6) | medium–high | token/signing key plus server | auth server availability |
| A5 | witness becomes dependency; operational complexity | highest | witness key + log operations | witness availability |

### Required experiments per approach (from the recovered 55/12 set; none executed)
| Approach | Minimum tests | Hard prerequisites |
|---|---|---|
| A0 / A0+ | characterization of T3-01…09, T4-01…08 (no T4-04), T6-01…13, T2-03/T2-04 (as "does control exist"), X-01, X-04, X-06, X-07, X-09, X-10 | disposable environment (`G-11`); no key custody needed |
| A1 | A0+ set plus T1-01…08 on the approval-service key, T2-* with MAC identity mapping | HD-4 custody tier; separation Verifier≠Executor |
| A2 | all 55 + all 12 | HD-1, HD-3, HD-4, HD-5, HD-9; synthetic keys only (Oct-13 sentinel + `SYNTH-KEY-SENTINEL` canary); `G-11` |
| A3 | A2 set mapped to the profile + transport tests | HD-11 decided |
| A4 | T5-01…09 emphasis + in-flight tests T5-02/T5-03 | HD-7 defined first (else BLOCKED) |
| A5 | evidence-integrity tests (Oct-13 §11) | C7-role independent reviewer |

## 3. What C2 can and cannot say today
- **Can say (VERIFIED):** the repo has no cryptographic mechanism; the current approval is an unsigned bearer record bound to an unkeyed digest; identity is a string; revocation is absent; the Oct-13 plan specifies 55 tests/12 scenarios, unexecuted.
- **Cannot say:** that any approach is selected; that RP-13 is closed or "adopt-ready"; that v3's content equals the Oct-13 plan; that any test passes.
- **Decision gating:** `H-03` (C1) = C2 `HD-3`. If the owner records "no cryptographic binding", `G-5` does not apply and the six questions become accepted-risk statements (owner decision); if the owner selects binding, `G-5` requires all six independently verified, and `G-11` (an implementation environment) must exist first.

## 4. Delta versus the Oct-13 plan (what this continuation adds)
Added: PR #8 static characterization column (§1); approaches comparison (§2); links to the decision register, classification contract, test plan v2 and PR-09 checklist. Unchanged: classification, 55/12 test inventory, HD-1…HD-15 definitions, closure criteria C-Q1…C-Q6/X. Not added: any mechanism, any "pass".
