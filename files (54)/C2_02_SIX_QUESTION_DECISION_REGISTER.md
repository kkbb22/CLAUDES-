# C2 — Six-Question Decision Register (RP-13)

C2 records options and consequences only. **No decision below is made.** Status of every item: **OPEN** (Oct-13 plan §12: "none is decided here"; C1 `H-03`: "none"; no owner decision was supplied). HD-n = Oct-13 plan IDs (recovered text, VERIFIED); `H-n` = C1 synthesis v2.1.2 §14 IDs. Owner column = who must decide or supply closure evidence.

## A. Gate context
| Gate | Text (C1 v2.1.2 §15) | Status | Relation to RP-13 |
|---|---|---|---|
| G-5 | `C2-RP13` complete: all six dimensions independently verified | NOT MET | Applies **only if H-03 (= HD-3) selects cryptographic binding**; blocks any live write relying on it |
| G-11 | A real implementation environment exists (the research sprint produced none) | NOT MET | Blocks **every** test, including all 55 + 12 |
| G-4 | Human records the approval baseline (H-04) | NOT MET | Blocks finalizing approval-record schema; interacts with HD-2 |

## B. Decision register — ordered by dependency
| ID | Decision | Options (C2 does not choose) | Consequences / trade-offs | Blocks | Closure evidence | Owner |
|---|---|---|---|---|---|---|
| **HD-3** (=H-03) | Invest in cryptographic binding at all | (a) no binding: recorded, unbound approval + hardened baseline (A0+) · (b) MAC · (c) asymmetric signature · (d) token/holder-of-key · (e) + witness tier | (a) makes G-5 inapplicable but leaves bearer-record forgery as accepted risk; (b)–(e) bring key custody, availability and test cost (see candidate §2) | everything | written owner decision recorded in the C1 decision register; if (a), explicit accepted-risk text for F-02/Q1/Q2 | accountable human; C1 records |
| **HD-1** | Unit of binding | single action · action set · plan (version) | smaller unit = more approvals/friction, tighter invalidation; plan unit makes X-06 central; `OQ-01` says plan, RP-13 says action (F1 wording divergence) | Q6, X-06 | owner choice + canonical-form spec referencing it | accountable human |
| **HD-5** | Who signs/approves | human approver only · Cloud personas for lower tiers · both by tier | defines Q2 entirely; persona signing reopens self-approval (T2-04) | Q2 | approver population + role table | accountable human (+C5 for operator workflow) |
| **HD-4** | Key custody tier & holder | operator-held · managed service · independent witness (RP-14 tiers) | assurance vs cost; DEP-09 (component providing custody/verification) is an unresolved experiment | Q1, Q2 | custody design + access-list review (C-Q1) | accountable human; C4 for infrastructure |
| **HD-14** | Independent witness tier required? | yes / no / by impact class | raises audit strength only; adds witness dependency | Q1 | owner decision | accountable human; C7 as verifier role |
| **HD-9** | Canonical form & equivalence policy | which fields covered; accept reordered/re-spaced equivalents or not; Unicode (NFC/NFD), numbers, duplicate keys | defines "same action"; must be a written rule with a collision corpus (T6-05…08) | Q6 | written rule + corpus + deterministic results across Requester/Approver/Verifier | accountable human; C2 drafts options; C6 oracle |
| **HD-2** | Approval scope & consumption | single-use vs persisted/category; consume at verification vs at commit when execution fails | changes replay and retry semantics (T3-09); overlaps C1 H-04 | Q3, G-4 | owner decision tied to H-04 | accountable human; C5 |
| **HD-6** | Validity window & semantics, by impact class | start-by vs complete-by; TTL per class | seconds-scale TTL (300 s in code) vs long tasks (flagged unresolved); T4-08 BLOCKED until decided | Q4 | decision table by impact class | accountable human |
| **HD-13** | Trusted time source & skew | local clock · NTP-class source · verifier-issued time | T4-07 clock-rollback test needs a defined authority; code uses local `time.time()` | Q4 | documented source & tolerated skew | accountable human; C4 |
| **HD-7** | Revocation & "in-flight" semantics | abort · finish atomic step · quarantine; max staleness; irreversible-step rule | unsolved in sources; cannot promise cancellation of irreversible actions; T5-03 BLOCKED until decided | Q5 | defined semantics + measured staleness (C-Q5) or human-accepted residual risk | accountable human; C4 (action atomicity) |
| **HD-8** | Fail-closed vs availability when replay/revocation/key state unreachable, per impact class | fail-closed all · fail-closed high classes only · fail-open low | PR #8 code currently resets nonce history to empty on unreadable file (policy.py:182–190) = fail-open on that state | Q3, Q5 | per-class table | accountable human |
| **HD-10** | Model-regenerated arguments | always fresh approval · defined envelope allowed | safety vs friction; T6-13 | Q6 | owner decision | accountable human; C3/C5 |
| **HD-11** | Transport/wire format of approvals | local file/CLI · HTTP-based · other | decides whether RFC 9421/9449 profiles apply or only their principles | Q6, Q3 | architecture decision | accountable human; C4/C1 |
| **HD-12** | Meaning of "Delegation Depth = 1" | spawn depth vs authority delegation; subagent approvals needed or not | not defined in anything read (Oct-13 F3) | Q2 | definition recorded in synthesis | C1 (definition), accountable human |
| **HD-15** | Reconcile `OQ-01` vs RP-13 wording and C2 packs staleness | edit owners' docs | documentation ownership; C2 did not modify any file | all | corrected canonical text | document owners (C1 integration) |

## C. Per-question disposition (all OPEN)
| Q | Needs decisions | Needs another Cloud | Closure (Oct-13 §13) | Today's evidence strength |
|---|---|---|---|---|
| Q1 key custody | HD-3, HD-4, HD-14 | C4 (environment/custody infrastructure), C7 (independent review) | T1-01…08 PASS with mutants; custody list; no canary leakage | none executed; no keys in code |
| Q2 identity | HD-5, HD-12, HD-15 | C5 (operator/approver workflow), C1 | T2-01…08 PASS; registry not writable from Requester/Executor | `approver` is free string (VERIFIED static) |
| Q3 replay | HD-2, HD-8 | C4 (state store durability) | T3-01…09 PASS under proven-concurrent trials | non-atomic nonce handling (VERIFIED static; exploit UNTESTED) |
| Q4 expiry | HD-6, HD-13 | C4 | T4-01…08 PASS; time source documented | start-of-run check only (VERIFIED static) |
| Q5 revocation | HD-7, HD-8 | C4 | T5-01…09 PASS; semantics defined | mechanism absent (VERIFIED static) |
| Q6 payload | HD-1, HD-9, HD-10, HD-11 | C6 (oracle), C5 (display derivation T6-12/X-12) | T6-01…13 PASS + written rule + corpus; X-01…12 PASS | partial digest binding (VERIFIED static) |

## D. Cross-cloud dependency list (named owner, exact closure evidence)
| Dep | Owner | Exact closure evidence |
|---|---|---|
| D-C1-1 Record HD-3/H-03 | accountable human via C1 | entry in C1 decision register with date, option, rationale |
| D-C1-2 Adopt classification contract (see C2_03) | accountable human; C1 adopts, C2 does not | recorded decision + updated canonical C1/C2/C5/C6 text |
| D-C4-1 Implementation environment (G-11) | accountable human; C4 designs | disposable environment spec + provenance; **C4 authorization is separate and not given here** |
| D-C5-1 Approver display derivation (T6-12, X-12) | C5 | operator UI spec showing signed-bytes derivation |
| D-C6-1 RP-13 oracle slots / mutant | C6 | C6 pack 002 oracles (TV-002-A…I) bound to the chosen unit of binding; mutant "binding disabled → A, B must fail" |
| D-C7-1 Independent verification | C7 (not C2) | issued C7 report over an exact frozen bundle; currently NOT ISSUED |
| D-USER-1 RP-13 v3 file + manifest | user | exact file named in the 10-16 review with SHA-256 `3efe555f0b1f96f4…36e47aa6` (full hash needed) |
