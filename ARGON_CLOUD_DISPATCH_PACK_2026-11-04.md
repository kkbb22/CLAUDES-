# ARGON — Cloud Dispatch Pack
**Date:** 2026-11-04  
**Purpose:** Evidence-only recovery and reconciliation of the seven original Cloud workstreams.  
**Mode:** READ-ONLY. No implementation, repository mutation, commit, push, PR, merge, deployment, or authorization.

---

## How to use this pack

1. Send the **Shared Instructions** below to every Cloud session.
2. Send each Cloud only its own assignment section and its own supporting evidence files.
3. Keep each Cloud in a separate session and separate staging/output folder.
4. C2–C6 can work concurrently. C1 may preserve and inspect its existing synthesis in parallel, but must not finalize a replacement synthesis until C2–C6 outputs are reconciled. C7 begins with privacy triage; its final synthesis audit happens only after the complete candidate set is frozen.
5. Do not ask all Clouds to review all seven handover documents. They are project-coordination documents, not seven identical tasks.

## Shared Instructions — prepend to each Cloud assignment

You are continuing the existing ARGON project. You are not starting a new project, replacing its architecture, or repeating completed research.

### Fixed repository boundaries

- `kkbb22/ARGON-AI-OS`: engineering automation/orchestration system.
- `kkbb22/ARGON-HEALTH`: distinct target healthcare architecture/product repository. READ-ONLY during this assignment.
- Legacy ARGON/Firebase: separate historical/production system. Do not inspect or modify it under this task.
- Never mix AI-OS research or implementation with HEALTH product architecture or Legacy ARGON.

### Known repository references (verify before relying on them)

- ARGON-AI-OS `main` observed at `1458a7f54f5d190ff84fce66cb2568960ff73559` (PR #8 merge, 2026-10-24).
- ARGON-HEALTH `main` observed at `fb6e3e38a09769e434dd9a40fb6590c8903ed744` (PR #2 merge, 2026-10-10).
- These are investigation references, not permission to write.

### Mandatory restrictions

- READ-ONLY source inspection only. Do not edit either repository, any shared register, or any reviewed candidate.
- Do not commit, push, create/merge PRs, deploy, change repository visibility, delete files, rewrite history, or rotate credentials.
- Do not run untrusted code, execute a runtime, or access production systems or patient data.
- Do not enable autonomous execution, ACT, Wave 4, or any machine write to ARGON-HEALTH.
- Do not mark an item implemented, tested, passed, accepted, or integrated without evidence tied to exact file hashes, commit IDs, test commands, environment, logs, and review records as applicable.
- Preserve unknowns and disagreements. Do not settle human decisions, choose thresholds, invent missing source material, or infer approval from a merge/title.
- Never overwrite historical work. Any new report must be separately named in your own staging/output folder.
- Do not edit `STATUS.md`, `NEXT-ACTIONS.md`, `OPEN-QUESTIONS.md`, `DEPENDENCY-REGISTER.md`, or the capability index. One integration owner updates shared registers serially after review.

### Required output from every Cloud

Return a self-contained report with:

1. Original role and exact assignment recovered from the 2026-10-14 prompt pack.
2. Files actually inspected, exact paths, repository commit/ref, file SHA-256, and source TXT line ranges where applicable.
3. Deliverable inventory: original filename, candidate revision, manifest, SHA-256, current location, and status.
4. What is already integrated, what is only staged, what was rejected/superseded, and what is unknown. Cite exact PR/commit or review evidence.
5. Changes since the previous report — do not repeat unchanged research.
6. Tests: distinguish `TEST SPECIFIED`, `TEST EXECUTED`, and `PASS WITH EVIDENCE`; include exact commands/logs or state `NOT EXECUTED`.
7. Open questions, missing files, owners, dependencies, and exact evidence needed to close each item.
8. A short recommendation for the next owner, without implementing it.
9. SHA256SUMS for every file you produce.

Use only these statuses where appropriate: `NOT STARTED`, `IN PROGRESS`, `DELIVERABLE PRODUCED`, `AWAITING REVIEW`, `ACCEPTED`, `INTEGRATED`, `REJECTED`, `BLOCKED`, `UNKNOWN — EVIDENCE REQUIRED`.

Output only to your own isolated staging folder. Stop and report a blocker if required evidence is not available.

---

# C1 — Orchestration, Cross-Cloud Architecture and Synthesis

### Supporting files to provide

- `ARGON_MASTER_PROJECT_STATE.md`
- `ARGON_SEVEN_CLOUDS_RECOVERY.md`
- `ARGON_REMAINING_WORK_AND_DEPENDENCIES.md`
- Original 2026-10-14 `ARGON_CLOUDS_1-7_PARALLEL_PROMPT_PACK_2026-10-14.md`
- Merged `architecture/synthesis/ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.md` from AI-OS PR #7
- Candidate `ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.1.1` and exact C7-FFA-004 Revision 5 report
- Current C2–C6 reports/candidates and their reviews as they become available

### Assignment

Recover and preserve the existing C1 synthesis lineage. Do not restart cross-cloud research and do not create a new architecture.

1. Verify PR #7's merged v2 draft and record its exact path, commit, and hash.
2. Reconcile v2, v2.1, v2.1.1, the C7-FFA-004 Revision 5 findings, and the current `main` state. Preserve each revision; do not overwrite one with another.
3. Identify exactly which C2–C6 artifacts are canonical, staging-only, accepted design-only, rejected, or missing. Do not call a candidate canonical merely because it exists in a Library/archive.
4. Maintain the distinction between five source-defined Plan/Act acceptance vectors, the proposed six-surface union, and C4's seven concrete PAM test cases. Do not choose a taxonomy or close H-09/OQ-03 on behalf of the human owner.
5. Preserve unresolved RP-13, context isolation/resumption, interface, checkpoint ownership, approval baseline, thresholds, and human decisions.
6. Produce an updated cross-cloud traceability and discrepancy table. Do not finalize a new synthesis until C2–C6 evidence has been reconciled and frozen.
7. When all inputs are frozen, prepare a separately versioned synthesis candidate and companion manifest for independent C7 review. Do not self-certify it.

### Required C1 outputs

- `C1_SYNTHESIS_LINEAGE_AND_STATUS.md`
- `C1_CROSS_CLOUD_TRACEABILITY_AND_DISCREPANCIES.md`
- If and only if inputs are frozen: a new, separately named synthesis candidate and manifest; never overwrite v2/v2.1.1.

---

# C2 — Security, Trust and Authorization

### Supporting files to provide

- `ARGON_SECURITY_AND_GOVERNANCE_STATUS.md`
- `ARGON_REMAINING_WORK_AND_DEPENDENCIES.md`
- Original 2026-10-14 prompt pack
- C2 canonical security research and C2 future security pack from AI-OS `main`
- C2 RP-13 experiment-plan candidate v3, its manifest, extraction/provenance note, and the 2026-10-16 C2–C6 review
- C7-FFA-003 and C7-FFA-004 Revision 5
- PR-09 follow-up evidence only if its exact files/report are supplied; do not infer it from the summary

### Assignment

Your original assignment is security/trust and the RP-13 cryptographic-binding experiment plan. Continue from the existing candidate; do not redo broad market/vendor research.

1. Verify the RP-13 candidate v3, manifest, source provenance, and the 2026-10-16 review findings against exact bytes.
2. Confirm that its 55 tests and 12 scenarios remain `TEST SPECIFIED` unless exact execution records prove otherwise. Do not claim they ran.
3. Preserve all six RP-13 questions: key custody, authorized identity, replay prevention, expiry, revocation/in-flight semantics, and exact-payload binding.
4. Reconcile the security findings relevant to PR-09, including SEC-03 approver identity and SEC-04 audit integrity, but classify each as source-verified, reported-only, disproved on a named revision, or unknown. Do not propose that a plain local-operator string is authenticated identity.
5. Do not select the cryptographic scheme, key custody model, approval baseline, or human policy. Identify the specific human decision and test prerequisites.
6. Identify any C2 artifact/provenance gaps and produce a minimal closure matrix.

### Required C2 outputs

- `C2_RP13_CANDIDATE_RECONCILIATION.md`
- `C2_SECURITY_FINDINGS_AND_OPEN_DECISIONS.md`
- Exact hashes and manifest verification record; no code changes.

---

# C3 — Context, Knowledge, Freshness, Isolation and Resumption

### Supporting files to provide

- `ARGON_MASTER_PROJECT_STATE.md`
- `ARGON_REMAINING_WORK_AND_DEPENDENCIES.md`
- Original 2026-10-14 prompt pack
- C3 canonical research and future pack from AI-OS `main`
- C3 reconciled r3 candidate, manifest, raw TXT extraction for lines 567–968
- `ARGON_C3_REVIEW_REPORT_2026-10-17.md`
- C2–C6 review dated 2026-10-16

### Assignment

Continue the source-backed C3 experiment specification. Do not redesign the context engine and do not claim runtime isolation exists.

1. Verify the r3 candidate, manifest, raw extraction and exact source line range.
2. Reconcile the 2026-10-17 C3 review's HOLD findings: missing historical `logs/input-hashes.txt`, absent checker/machine-readable output for the 71-row anchor validation, missing/unfinished fixture payloads and ground-truth/oracle material.
3. Determine whether any of those exact files have since been recovered. If not, keep them explicitly missing. Do not manufacture a replacement and label it historical.
4. Keep context semantics, freshness, provenance, leakage/isolation, concurrency and safe-resumption questions separate from C2 authorization and C4 mutation mechanics.
5. Keep all unspecified thresholds, freshness windows, retry limits, isolation trial counts, snapshot schemas, checkpoint/journal ownership and P15 decisions open.
6. State exactly what additional reproducible evidence is needed before the candidate can leave staging.

### Required C3 outputs

- `C3_R3_RECONCILIATION_AND_REVIEW_GAPS.md`
- `C3_FIXTURE_ORACLE_AND_PROVENANCE_GAP_REGISTER.md`
- Exact hashes and manifest verification; no code changes or tests claimed.

---

# C4 — Engineering, Mutation Boundaries and Wave 3.5 Recovery

### Supporting files to provide

- `ARGON_SECURITY_AND_GOVERNANCE_STATUS.md`
- `ARGON_REMAINING_WORK_AND_DEPENDENCIES.md`
- Original 2026-10-14 prompt pack
- C4 canonical engineering research and future pack from AI-OS `main`
- C4 Plan/Act mutation matrix candidate v3 and available manifests/diffs/logs
- C4 Wave 3.5 recovery report and all available archive/manifests
- C2–C6 review dated 2026-10-16
- ARGON-HEALTH `main` and exact historical commit references for read-only searching only

### Assignment

Continue C4's original engineering/mutation and historical recovery assignment. Do not implement or enable the runtime.

1. Reconcile the matrix's many-to-many source mapping. Keep source-defined five-vector taxonomy, proposed six-surface union, and seven concrete PAM tests distinct. Identify missing companion manifests, logs, diffs or fixtures.
2. Inspect the actual C4 Wave 3.5 manifest in AI-OS `archive/historical/wave3.5/`. It declares `repo_target: kkbb22/ARGON-HEALTH`, expected Markdown hash `22ca9931e0799e3285ac802f65677bc0859790acb9081b65addc340477f60a90`, and historical `verified_repo_head: 3520d70946f6623875c6f7d6ea47ef40f5bcc316`.
3. Search only read-only in the correct HEALTH repository/history and at the declared historical ref for the exact v2 and superseded v1 artifacts. Report commands/paths/results. A manifest alone is not proof of recovery.
4. If exact original bytes cannot be found and hash-matched, retain `NOT RECOVERED`. Never fabricate or create a file using either original filename. A separately named reconstruction would require a new explicit owner decision and must be labeled reconstruction.
5. Review PR-09 execution-containment claims only as they relate to C4's engineering boundary. The supplied 2026-11-02 summary is not enough to prove the actual branch code. Request the full branch diff and audit bundle if missing.

### Required C4 outputs

- `C4_MUTATION_MATRIX_AND_PROVENANCE_RECONCILIATION.md`
- `C4_WAVE35_EXACT_SOURCE_RECOVERY_REPORT.md`
- `C4_PR09_EXECUTION_BOUNDARY_REVIEW_NOTES.md` (only if exact branch evidence is supplied)

---

# C5 — Human Control and Operator Acceptance

### Supporting files to provide

- `ARGON_MASTER_PROJECT_STATE.md`
- `ARGON_SECURITY_AND_GOVERNANCE_STATUS.md`
- Original 2026-10-14 prompt pack
- C5 canonical operator-control research and current future pack from AI-OS `main`
- C5 operator-control acceptance-test candidate r3, manifest, extraction/provenance notes
- 2026-10-16 C2–C6 review and C7-FFA-003

### Assignment

Continue C5's original operator-control and acceptance-test work. Do not take over backend security enforcement or choose project-wide approval policy.

1. Verify the C5 acceptance-test candidate r3 and its source/test-ID lineage against exact files.
2. Verify whether the original C5 future-pack v1 bytes can be recovered from current repository, all accessible refs/history, manifests, archives and source-move records. If not, state `NOT RECOVERED`; do not call v2 a recovered v1 or invent missing test IDs.
3. Preserve the distinction between operator-visible display, human comprehension, human decision, authorization, and backend enforcement. A confirmation dialog is not proof of backend authorization.
4. Keep human-study thresholds, STOP latency, pause/resume policy, sample sizes, and all unsourced/new requirements explicitly open.
5. Identify missing files, provenance artifacts and exact closure evidence. Do not rewrite shared registers.

### Required C5 outputs

- `C5_OPERATOR_ACCEPTANCE_TESTS_LINEAGE_REVIEW.md`
- `C5_V1_PROVENANCE_RECOVERY_REPORT.md`
- Exact hashes and manifest verification; no runtime tests claimed.

---

# C6 — Evaluation, Verification and Value/Cost Measurement

### Supporting files to provide

- `ARGON_MASTER_PROJECT_STATE.md`
- `ARGON_REMAINING_WORK_AND_DEPENDENCIES.md`
- Original 2026-10-14 prompt pack
- C6 canonical evaluation research and manifest from AI-OS `main`
- Accepted C6 future evaluation capability packs, manifest and reconciliation report
- `governance/decisions/C6-DESIGN-ONLY-ACCEPTANCE-2026-10-21.md`
- PR #3, #4, #5, #6 metadata or links

### Assignment

C6 future packs were accepted as a **design-only** deliverable through PR #5, with provenance correction through PR #6. Do not re-author the five packs or repeat the original research.

1. Verify the current canonical C6 pack and companion manifest against exact bytes and the acceptance record.
2. Confirm the accepted boundary: `DESIGNED`, `NOT_IMPLEMENTED`, `TEST SPECIFIED`, `TEST EXECUTED = 0`, `PASS WITH EVIDENCE = 0` unless newer exact evidence proves otherwise.
3. Reconcile C6 interfaces with C2 security classification, C3 context/trajectory/resumption, C4 mutation/oracle mapping, C5 STOP/operator semantics, and C7 verification authority.
4. Preserve every `THRESHOLD NOT SET`, missing schema owner, and cross-Cloud discrepancy. Do not silently treat C6's six-route union wording as a final human-approved taxonomy.
5. Produce only a concise current-state and dependency confirmation. New pack versions are not requested unless a concrete, source-backed defect requires a separately named candidate.

### Required C6 outputs

- `C6_ACCEPTED_DESIGN_ONLY_STATUS_CONFIRMATION.md`
- `C6_CROSS_CLOUD_INTERFACE_DEPENDENCY_MATRIX.md`
- Exact hash/manifest/acceptance-record verification; no evaluation execution claims.

---

# C7 — Independent Forensic Audit and Privacy Triage

### Supporting files to provide

- `ARGON_MASTER_PROJECT_STATE.md`
- `ARGON_SECURITY_AND_GOVERNANCE_STATUS.md`
- Original 2026-10-14 prompt pack, especially both C7 sections
- C7-FFA-003
- C7-FFA-004 Revision 5 and all candidate/revision correction matrices available
- Frozen C1–C6 candidates, manifests, reports and integration records when ready
- PR-09 follow-up branch export and full 2026-11-02 audit only when their exact bytes are supplied

### Assignment — Phase A: start now, privacy/public-exposure triage

1. Conduct read-only inspection of the public AI-OS repository and accessible history, prioritizing `archive/external-health/`, ZIP/DOCX/PDF/XLSX/HTML/screenshots, `evidence/`, and archived source artifacts.
2. Do not assume that healthcare-related material is patient data. Classify findings as confirmed sensitive, possible/ambiguous, synthetic/demo, public reference, or no issue observed.
3. Redact sensitive values. Report only exact path, commit/hash, page/sheet/archive member, category, confidence, and recommended owner action.
4. Do not delete, modify visibility, rotate tokens, rewrite Git history, or perform remediation.
5. State scan coverage and limitations. Zero pattern matches is not proof of zero sensitive material.

### Assignment — Phase B: only after all candidate inputs are frozen

1. Independently audit the exact C1–C6 candidates and manifests, source-to-claim map, cross-Cloud decisions, repository state drift, PR-09 evidence and governance gates.
2. Independently recompute hashes. Tie every finding and verdict to exact immutable revisions.
3. Do not author, repair, or edit the artifacts being audited. Do not audit a moving branch.
4. Distinguish documentary/consistency assurance from empirical runtime-security certification.
5. Issue only an evidence-supported verdict: `CLEAN WITH OPEN EXPERIMENTS`, `CORRECTIONS REQUIRED`, or `BLOCKED BY MISSING EVIDENCE`.
6. No clean verdict may be inferred from a prior C7 result, a GitHub merge, or an implementation report.

### Required C7 outputs

- Phase A: `ARGON-AI-OS-PUBLIC-REPOSITORY-PRIVACY-TRIAGE.md`
- Phase B: `C7-FFA-004` audit candidate tied to the frozen input manifest
- Independent hash and evidence inventory. No code changes.

---

## Integration owner / user decision gate

Do not merge Cloud files into repositories. Collect each Cloud's output in a separate staging folder, verify its hashes, compare it with the prior deliverable, and update one consolidated inventory. C1 synthesizes only after C2–C6 are reconciled. C7 audits only after that set is frozen. Human decisions and repository writes remain with the project owner.

## Immediate critical evidence still needed for PR-09

The following are not contained in the seven-document handover and must be supplied by whoever holds the local follow-up worktree:

- Full read-only export of `D:/aoswork-pr09-followup` at expected HEAD `23fb2733549d8c84d8d58817cd0586ac3047fdcc`.
- Exact branch/base commit, `git status`, `git log`, full `git diff` against base and against current AI-OS `main`, and file inventory.
- Full 2026-11-02 independent forensic audit, exact report SHA-256, commands, Docker daemon/runtime facts, image digest, tool versions, fixtures, test logs and outputs.
- No `git clean`, reset, stash, rebase, cherry-pick, merge, push or other mutation while collecting this evidence.

Until this packet is available and reconciled, PR-09 remains `REQUEST CHANGES / HOLD`; autonomous execution, Wave 4 and ARGON-HEALTH machine writes remain prohibited.
