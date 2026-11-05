# C4 — Open-Dependency Register, Input Inventory and Handover (2026-11-05)

## 0. Identity charter (repeat in every handover)

**Cloud identity:** C4 — ARGON Engineering Execution & Mutation-Boundary Architect. **Responsibility:** analyse how engineering plans become controlled actions (mutation surfaces, tool boundaries, workspace scope, command execution, sandbox containment, verification, failure handling, recovery); map attack paths; define testable controls. **Boundaries:** C4 does not authorize execution, does not set human approval policy, does not implement changes, and is not C7's independent auditor. Read-only; no Wave 4; no machine writes to ARGON-HEALTH; Legacy ARGON not inspected. **Persistence:** `ARGON_CLOUD_IDENTITY_C4` is **session-only** — not saved to persistent memory; carry this charter in each continuation.

## 1. Input inventory and hash verification (this continuation)

| Input | Bytes | SHA-256 | Status |
|---|---|---|---|
| `ARGON_COMPLETE_RECOVERY_2026-11-05.zip` | 12,584,992 | `0be6f07ac8d68170a450355cd1b7abe83082d606d414e9845020d6fa8a6b5f16` | original upload; its own `SHA256SUMS.txt` (43 entries) re-checked with `sha256sum -c`: **all OK** (VERIFIED) |
| `01_RECOVERED_LIBRARY_FILES/c2-c6.TXT` | 221,902 | `a542be977e7af20dfe90be08585b1a05e094351805a0d8c9dcb22301b2d0039a` | equals the hash C6 declared for `c2-c6(1).TXT`; byte-identical to the C3-bundle copy (VERIFIED) |
| `…/C6-FUTURE-EVALUATION-CAPABILITY-PACKS.md` (candidate v3) | 53,423 | `213f25a5222a5bfa8a2c6e32df27b565403fcf4ea34d9be5af01d4086d2f020e` | derived design candidate; T6-002/T6-003 rows identical to `main` v4 |
| AI-OS `main` `capabilities/future/C6/…PACKS.md` (v4, accepted design-only) | 55,128 | `dab7060ec1042a9ee09749fc5303b663dea961ab349e6919ede9bc52ee5cbc68` | blob `ca026d893a45f979f29f5fa819a9681a3cf0a9b0`; read from `1458a7f` |
| `ARGON_CLOUD_DISPATCH_PACK_2026-11-04.md` | 19,029 | `3a01e7a06d5d1b2c07a84cfa8a234d907e548b72fe25bf6c42b25feb18207d8e` | VERIFIED vs bundle sums |
| `ARGON_MASTER_HANDOVER_2026-11-04.zip` (inside bundle) | 39,655 | `36fedd57dda2a3fe8e5df014ea571ab140d1b8ac6f74319995722b8744d69a73` | identical to the zip uploaded earlier (VERIFIED) |
| `…/more/مراجعة اخر تحديثات.rar` → synthesis v2.1.2 | 65,971 (member) | `563e72215bd2e3a8791d4aa977484eaeac285e6453d620cf8aa219040638e086` | read through libarchive; derived candidate |
| `…/C7-FFA-004-revision5.md` / `rev6-review-draft` | 22,005 / 10,952 | `e5c4e2ad…0912` / `531c6b7e…6642` | read for IDs only; **not** reviewed as an audit |
| `files__53_.zip` (prior C4 package v3, 6 of ~20 files) | 33,527 | `75b43e700c3c6a09d5cd4cbcf9f2eb023509cc8e4668378ac58b949d4fa371c7` | earlier input; its 5 listed hashes matched |
| AI-OS `main` | — | commit `1458a7f54f5d190ff84fce66cb2568960ff73559` | VERIFIED (`git ls-remote`) |
| ARGON-HEALTH `main` | — | commit `fb6e3e38a09769e434dd9a40fb6590c8903ed744` | VERIFIED |

Not supplied (exact names): PR-09 branch export (`D:/aoswork-pr09-followup`, HEAD `23fb2733549d8c84d8d58817cd0586ac3047fdcc`) and the full 2026-11-02 audit; the original `C4-WAVE3.5-CONTEXT-v2.md`; the 15 remaining C4-package files (4 manifests, 5 evidence files, 6 provenance files); C1/C2/C5 original research files; definitions of C6 `G-13` and `P-01…P-06`, SEC-01, SEC-02.

## 2. Findings summary (evidence-labelled)

| # | Finding | Class |
|---|---|---|
| F1 | PR #8 runtime on `main` has no container/seccomp/digest-pinned isolation; verification runs on the host with inherited environment | VERIFIED (static) |
| F2 | A contract whose actions are read-only-classified can avoid approval while carrying an interpreter command in `verification.commands`; with AP-02 and AP-07 this lets the verification child touch approval/nonce/ledger files | Components VERIFIED (static); composition INFERRED; not demonstrated |
| F3 | The tool registry's handlers and the providers have no reachable call path today (latent) | VERIFIED (grep) |
| F4 | Taxonomy counts: five (S1, S2, S4, S5), six (S6, S7), seven (S8) are different units; none is normative; origin of "five" not located | VERIFIED text / UNKNOWN origin |
| F5 | C6 T6-002/T6-003 rows are identical in candidate v3 and canonical v4 | VERIFIED |
| F6 | Wave 3.5 v2/v1 Markdown absent from all checked locations, including the whole new bundle | VERIFIED absence → NOT RECOVERED |
| F7 | PR-09 changes: no exact evidence; all remain NOT VERIFIED | VERIFIED (absence of evidence) |
| F8 | `G-7`/`G-9` exist as C1 synthesis gates; `G-13`, `P-01…P-06` do not exist in any supplied file | VERIFIED / UNKNOWN |

## 3. Work completed in this continuation

Taxonomy comparison; adapter-manifest contract and golden-vector format (proposal); traceability matrix (25 rows; strengths `SUPPORTED`/`PARTIAL`/`NOT SUPPORTED`/`UNRESOLVED`, none executed); PR #8 mutation-surface map with PR-09 reconciliation; Wave 3.5 recovery continuation; this register. Nothing was executed against any runtime; no repository, HEALTH or Legacy access beyond read-only git reads of the two public repositories.

## 4. Open-dependency register

| ID | Dependency | Owner | State | Exact closure evidence |
|---|---|---|---|---|
| OD-01 | Taxonomy level and acceptance list (A1, A2) → H-09 / OQ-03 / G-1 | C1; human owner decides H-09 | OPEN | Stated definition + chosen list in the canonical file that owns the acceptance list |
| OD-02 | Origin text of the "five" requirement (A3, "X1") | C1 / integration owner | UNKNOWN | The originating requirement text |
| OD-03 | PAM-05 vs PAM-06: one mechanism or two (A4) | C1 | OPEN | C1 definition of "second tool" and dispatcher treatment of nested calls |
| OD-04 | Identity of C6 `G-13` and `P-01…P-06`; confirm whether `G-07`/`G-09` mean synthesis gates G-7/G-9 | Human owner | UNKNOWN | The file or text defining them |
| OD-05 | PR-09 branch export and 2026-11-02 audit | Human owner (local worktree); C7 for review | NOT SUPPLIED | Read-only `git bundle` + diffs + Docker files + logs + image digest + full report (list in `C4_PR09_FOLLOWUP_DIFF_AND_ASSURANCE_REVIEW.md`) |
| OD-06 | Original Wave 3.5 v2 (and v1) Markdown | Human owner; C7 | NOT RECOVERED | Bytes with SHA-256 `22ca9931…` (v1 `a845053f…`), or written owner statement it is unrecoverable; Option A/B choice |
| OD-07 | Remaining C4-package files (4 manifests, 5 evidence files, 6 provenance files; internal count inconsistency "v2 = 6" vs 4 listed) | Human owner | NOT SUPPLIED | The files, hashed against the package's list |
| OD-08 | Remediation decisions for AP-01…AP-18 (design owner) and independent verification | C2/C5/human for policy; C7 for verification | OPEN | Accepted design changes + executed tests with logs + C7 review (none exists) |
| OD-09 | Authorization to run the safe future test plan | Human owner (separate written authorization) | NOT AUTHORIZED | Written authorization naming commit, disposable environment, reviewer |
| OD-10 | PLAN oracle semantics: is control-plane persistence (task JSON, ledger, approvals dir) a "mutation"? (TM-20) | C1 / C2 | OPEN | Decision recorded in the canonical C1/C2 file |
| OD-11 | Approver identity model and approval-record integrity (SEC-03, AP-08, AP-12; RP-13 binding build decision) | C2 design; C5 operator; human decision | OPEN | Authenticated-principal design + negative tests |
| OD-12 | Ledger integrity (SEC-04, AP-13) anchoring design | C2/C3/human | OPEN | Design + fork/rewrite tests |
| OD-13 | Definitions of SEC-01 and SEC-02 | C7 / human | UNKNOWN | The defining text |
| OD-14 | Adapter contract decisions AD-1…AD-6 (see adapter document) | C4→C2/C3/C6; human | OPEN | As listed there |
| OD-15 | Checkpoint/journal storage owner and step granularity (D-02, C4 U1) | C1/C3/C6 | OPEN | Named owner + schema |
| OD-16 | Hash convention for manifests (raw vs LF) | Human / C5 | OPEN | Stated convention |
| OD-17 | Classification label set 3 vs 4 (D-03) | C1/C2 | OPEN | Harmonized set |
| OD-18 | Repository state hygiene: tracked `.argon/` runtime state and 19 `__pycache__` files on `main` | Human owner | OPEN (owner decision; no action taken) | Owner decision recorded; any change via its own reviewed PR |
| OD-19 | Hash-only scan of `archive/external-health/` zips was done by C1 (SOURCE-ASSERTED); content privacy triage | C7 / human | UNKNOWN | C7 privacy triage; not needed to close OD-06 |
| OD-20 | Rev5/rev6 C7 documents were read for identifiers only | C7 | NOT REVIEWED by C4 | C7-issued audit result |

## 5. What remains unauthorized

Running any test, command or script against the runtime or either repository's code; Docker execution; mutation tests; any commit, push, merge, PR, deployment or file edit in a repository; any access to real health data; autonomous execution; **Wave 4**; **any machine write to ARGON-HEALTH**; any change to or inspection of Legacy ARGON; treating any document here as a security certification or as C7's audit. No acceptance of the adapter contract, taxonomy or remediation is implied.

## 6. Handover to the next Cloud (concise)

1. Charter above applies; C4 is session-only.
2. Evidence base: AI-OS `main` `1458a7f`; HEALTH `main` `fb6e3e3`; runtime blobs listed in the surface map. All C4 findings are static (A2); nothing executed.
3. Highest-risk observation to take to C2/C5/C7: AP-01/02/07 composition (read-only-classified contract → host interpreter → writable approval/nonce/ledger files).
4. Do not pick a mutation taxonomy for the owner; use the comparison document. Treat `G-7`/`G-9` as C1 gates and `G-13`/`P-01…06` as unresolved.
5. Wave 3.5 v2/v1 is `NOT RECOVERED`; never reconstruct under the original names.
6. PR-09 stays `NOT VERIFIED` until the read-only export arrives.
7. The next useful input is OD-05 (PR-09 export) and OD-04 (definitions of G-13/P-01…06).
