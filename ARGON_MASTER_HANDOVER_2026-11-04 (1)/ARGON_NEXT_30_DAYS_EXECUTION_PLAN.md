# ARGON Next 30 Days Execution Plan

**Planning window:** 2026-11-04 through 2026-12-04  
**Plan type:** conditional, dependency-aware; no implementation or deployment authorization is implied.

> The first 30 days should restore a defensible evidence baseline and resolve the PR-09 security hold. It should not be spent repeating Cloud research or starting a broad product build. The dates are planning windows, not commitments or proof that a gate will pass. If a prerequisite is missing, the dependent activity remains blocked.

## 1. Program objectives for this window

1. Recover the exact local PR-09 follow-up and full 2026-11-02 forensic evidence.
2. Reconcile current AI-OS `main` with the claimed security remediation and identify the exact source revision that is safe to review.
3. Preserve the seven Cloud assignments and complete the artifact/acceptance inventory without restarting their original research.
4. Obtain a revision-pinned independent C7 review; retain HOLD if any required gate is not met.
5. Re-establish an accurate and truthful status for both target repositories.
6. Keep ARGON-HEALTH architecture-only and protected from machine writes.

## 2. Work sequence

### Days 1–3 — Evidence recovery and preservation (Nov 4–6)

**Objective:** know exactly what the PR-09 follow-up worktree and November 2 audit contain.

Actions:
- Obtain a read-only export of `D:/aoswork-pr09-followup`, branch `fix/pr09-security-containment-followup`, expected HEAD `23fb2733549d8c84d8d58817cd0586ac3047fdcc`.
- Record repo remotes, branch list, HEAD/base, `git status`, log, diff, file inventory and hashes.
- Obtain the full November 2 independent audit, report hash, environment details, Docker state, image digest, runtime logs and exact tests.
- Preserve local working copy, untracked files and patch byte-for-byte. No reset/clean/stash/rebase/cherry-pick/merge.
- Collect the exact current PR8 `main` source and test inventory already pinned in this report.

**Deliverable:** `PR09-EVIDENCE-INTAKE` packet with immutable file hashes and explicit gaps.

**Exit condition:** exact base/candidate revision and original audit evidence are identified. If not, status remains `BLOCKED — EVIDENCE REQUIRED`; move no further.

### Days 4–7 — Reconciliation and security gap analysis (Nov 7–10)

**Objective:** reconcile PR-09 follow-up claims against current main source without implementing changes.

Actions:
- Compare the local branch diff against AI-OS main `1458a7f...`.
- Verify whether ToolRegistry host subprocess path was removed/routed, whether Docker isolation exists in the effective execution boundary, and whether fail-closed verification is structurally enforced.
- Reconcile SEC-03 approver identity, SEC-04 audit integrity, nonce race/corruption, stdout/stderr buffering and seccomp profile.
- Confirm exact state of tests, image digests, Docker runtime, tool versions, test fixtures and results.
- Inventory current C1–C7 artifacts, their exact filenames, hashes, manifests, review dispositions and integration refs; do not request repeat research from C2–C6.

**Deliverable:** source-to-claim security reconciliation matrix; current cloud artifact inventory; decision list.

**Exit condition:** each claim is classified as verified, reported-only, disproved on tested ref, or unknown. No claim is promoted because it appears in a report.

### Days 8–14 — C1/C2–C6 provenance reconciliation and independent C7 review readiness (Nov 11–17)

**Objective:** create one reviewable, exact evidence bundle.

Actions:
- Reconcile C1 v2 in main with the v2.1.1 candidate and C7-FFA-004 Revision 5 no-clean-verdict report. Preserve each version and SHA; identify the canonical candidate path by human decision, not inference.
- Verify C2 RP-13 candidate/manifest; C3 r3 review gaps; C4 matrix and recovery files; C5 test candidate and v1 status; C6 accepted design-only pack.
- Keep Plan/Act five/six/seven counting units distinct and map source test IDs to candidate scenarios. Do not decide H-09/OQ-03 on behalf of the owner.
- Verify C4 Wave 3.5 exact original Markdown in the correct target repository/history; otherwise leave it `NOT RECOVERED`.
- Verify C5 v1 exact bytes/hash if available; otherwise retain `NOT RECOVERED`.
- Complete C7 privacy/archive triage with offline, redacted evidence. The prior possible DNS validation exposure remains owner-check-needed until its status is proved.
- Freeze the exact input set for C7; no edits to those inputs during audit.

**Deliverable:** frozen candidate manifest, source-to-claim matrix, open-decision register, privacy triage report, C7 review packet.

**Exit condition:** C7 has exact bytes, source refs, manifests and scope. Missing evidence prevents a clean verdict.

### Days 15–21 — Independent C7 assessment and owner decision gate (Nov 18–24)

**Objective:** obtain independent disposition before any implementation is considered.

Actions:
- C7 performs a read-only audit against exact frozen revisions: hashes/provenance, source-to-claim, cloud consistency, PR8 security claim mapping, policy decisions, tests, archive exposure and sequencing.
- C7 does not edit the reviewed code/documents and does not run unsafe code. Runtime tests, if needed, must use a separately approved isolated environment with fixtures and a documented test harness.
- C7 chooses an evidence-supported verdict: `CLEAN WITH OPEN EXPERIMENTS`, `CORRECTIONS REQUIRED`, or `BLOCKED BY MISSING EVIDENCE` for the audit scope.
- Human authority decides any remaining architectural/security policy matters: approval model, whether to invest in RP-13 crypto binding, Plan/Act taxonomy H-09/OQ-03, interface choice, resume semantics, thresholds and target implementation gate.

**Deliverable:** C7 audit report tied to exact input hashes and human decision register.

**Exit condition:** only a clean verdict plus explicit human authorization can open a bounded next step. If C7 reports corrections or missing evidence, no Wave 4 or autonomous runtime activity.

### Days 22–30 — Conditional, tightly bounded remediation planning or execution (Nov 25–Dec 4)

**Default path if any gate remains open:**
- Continue HOLD.
- Produce a narrow remediation plan, patch design, test specification and evidence checklist only.
- Do not modify main, create/merge PRs, deploy, or enable writes.

**Conditional path only if C7 is clean for the relevant scope and the human authority separately authorizes a bounded security change:**
- Work on a dedicated isolated review branch, not main.
- Fix only approved P0 security items (execution boundary, approver identity, nonce atomicity/fail-closed behavior, audit integrity, output limits, seccomp/pinned image as applicable).
- Build tests around exact threat vectors and negative controls before enabling the affected capability.
- Execute tests in an isolated environment; record exact source SHA, image digest, tool versions, fixtures, commands, results and independent reviewer.
- Re-run independent security review; keep ACT disabled until required gates pass.
- Update STATUS/NEXT-ACTIONS and handover snippets only after acceptance and human authorization.

**Deliverable:** either (a) a revised evidence-backed remediation plan with blockers or (b) an independently tested, review-branch-only remediation candidate with complete logs. Neither outcome automatically authorizes merge, production or Wave 4.

## 3. Decision gates and stop rules

| Gate | Required before | Evidence | If not met |
|---|---|---|---|
| G-A — PR-09 worktree recovered | Any integration decision | Exact branch/HEAD/base/diff and audit provenance | Stop; preserve unknown local branch. |
| G-B — security findings reconciled | Any runtime execution authorization | Source traceability and controlled tests for process, identity, nonce, audit, output, Docker/seccomp | HOLD. |
| G-C — Cloud candidates reconciled | C7 final synthesis audit | Exact manifests/hashes, accepted/staging/rejected status | C7 audit remains blocked. |
| G-D — C7 clean for exact revision | Wave 4/runtime implementation consideration | Independent report tied to immutable source/image/test hashes | No runtime/Wave 4. |
| G-E — human approval | Any write or policy change | Explicit scope-bound decision and owner record | No write, merge, deployment or policy change. |
| G-F — runtime isolation proven | Protected ACT use | Effective container/OS enforcement plus adversarial test evidence | ACT remains disabled. |
| G-G — Health-specific authorization | Any Health implementation or write | ADR-000 trigger, accepted scoped decision, clinical/security/legal readiness | Health stays architecture-only. |

## 4. Parallelism without role drift

- C2–C6 should not be asked to repeat the October design research. Their existing deliverables should be preserved, inventoried and only the missing evidence requested.
- C1 should reconcile the synthesis versions using source hashes and the human decision register, not settle disputed policy unilaterally.
- C7 should be independent, read-only and downstream of frozen evidence.
- Integraphy should own engineering integration only after the project owner gives a bounded task and the security gates allow it.
- No two workstreams edit the same shared register or candidate file concurrently. A single integration owner updates shared registers serially after accepted decisions.

## 5. End-of-window success criteria

The 30-day window is successful if, by Dec 4, one of these outcomes is achieved truthfully:

**Outcome A — Security/governance baseline cleared:** exact PR-09 branch/report reconciled; all relevant security issues independently verified; C7 clean for the exact reviewed scope; owner decisions recorded; a narrowly scoped next step is explicitly authorized.

**Outcome B — Evidence-backed HOLD maintained:** missing local worktree/report/runtime evidence is documented; C7 findings remain open with owners and closure criteria; no protected write or Wave 4 activity occurs; Integraphy receives an exact, reproducible handover.

Outcome B is preferable to an unsupported “ready” declaration. A clean document package is not the same as an operationally secure engineering machine, and an architecture blueprint is not the same as a deployed medical product.
