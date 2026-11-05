# ARGON — Parallel Cloud Prompt Pack (2026-10-14)

## Execution order

Run **C7 privacy triage first and in parallel** with C2–C6. Run C2, C3, C4, C5 and C6 concurrently, each in its own isolated staging directory/worktree. C1 should inspect and preserve the existing local synthesis draft in parallel, then finalize the synthesis only after the C2–C6 candidate files have been reviewed and integrated into one review branch. Run C7-FFA-004 only after that integration is frozen for review.

## Current verified GitHub baseline at time of this pack

- `kkbb22/ARGON-AI-OS` default branch `main`: `71a3fa6d1fb1eed0e694886263710d4020e10341`.
- `kkbb22/ARGON-HEALTH` default branch `main`: `fb6e3e38a09769e434dd9a40fb6590c8903ed744`.
- Both repositories are currently public. Re-check these facts before relying on them.
- `ARGON-AI-OS` currently tracks 79 files in `main`. Its `archive/external-health/` includes medical-system reference documents and binaries, including `ARGON-HEALTH-main (3).zip`, an assurance-kit ZIP, healthcare analysis PDF/DOCX, spreadsheet/dashboard, screenshots, HTML visual guides, and a large medical-UI PDF. Their contents have **not** been established as actual patient data; urgently inspect and classify them without exposing sensitive content in reports.
- Local C1 synthesis draft was reported as untracked at `D:\ai-os-argon\clouds\C1\ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.md`. This is not present in remote `main`; verify whether it still exists locally and preserve it before anything else.
- The uploaded work-product file `c2-c6(1).TXT` is 2,240 lines / 221,902 bytes with SHA-256 `a542be977e7af20dfe90be08585b1a05e094351805a0d8c9dcb22301b2d0039a`.

## Shared instructions — prepend this block to each cloud-specific assignment

You are working on ARGON AI-OS continuity, not a new project discovery. Use current repository bytes as the authority; treat historic maps, chat summaries, and reports as leads only.

### Boundaries

- Only `ARGON-AI-OS` work may be prepared or modified in this task set.
- `ARGON-HEALTH` is READ-ONLY and remains a distinct target architecture repository. Do not confuse it with legacy ARGON/Firebase or with AI-OS research artifacts.
- Do not modify either repository's `main`, delete files, change architecture decisions, run destructive Git operations, commit, push, open/merge PRs, deploy, or change repository visibility.
- Do not access production systems, patient databases, secrets, or use real patient data.
- Produce artifacts in an isolated local staging directory outside the canonical repository, for example `D:\ARGON-STAGING\2026-10-14\C2\`. Do not concurrently edit shared registers or one shared working tree.
- Before work, record verified GitHub SHA, local branch/HEAD/status and input file hashes. Use a separate working clone/worktree for source inspection if available; never overwrite existing untracked work.
- The attached TXT is a source container, not a canonical repository. Preserve its SHA-256 and exact source line range for each extracted output. Preserve an untouched raw extraction outside the repository, then put corrections only in the candidate version with a change log.
- A hash of the TXT is not the hash of a contained Markdown artifact. Compute each candidate file's SHA-256 from its final exact bytes and put that value in a companion manifest. Do not normalize newlines when claiming byte identity. If a prior embedded hash refers to a different copy or is unverifiable, label it as such.
- Keep the status vocabulary truthful: `DESIGNED`, `NOT_IMPLEMENTED`, `TEST SPECIFIED`, `TEST EXECUTED`, `PASS WITH EVIDENCE`. Never claim execution or a pass without actual logs, fixtures, exact tested revision hashes and an independent oracle where required.
- Preserve `NEEDS EXPERIMENT`, `UNKNOWN`, `BLOCKED`, `THRESHOLD NOT SET` and `REQUIRES HUMAN DECISION` wherever evidence does not close them. Do not invent policy, numeric thresholds, source files, history, or human decisions.
- Keep a file-by-file change report, exact SHA-256 list, validation commands and observed outcomes. Stop with a clear blocker report instead of guessing if essential evidence is missing.

---

# C2 — Security and Trust

**Work concurrently; output only to the C2 staging directory.**

Review TXT lines 2–564 (excluding the `c2` separator and separator before C3). The proposed target is `assurance/experiments/C2-RP13-CRYPTOGRAPHIC-BINDING-EXPERIMENT-PLAN.md` with a companion manifest.

1. Start with a byte-preserving extraction of the section into a raw staging copy. Record `c2-c6(1).TXT`, its SHA-256 (`a542be...d0039a`) and source lines 2–564. Do not claim that the extracted Markdown hash equals the TXT hash.
2. Recheck the extracted plan against current `clouds/C2/C2-CLOUD-SECURITY-ADAPTER-RESEARCH.md`, `capabilities/future/C2/C2-FUTURE-SECURITY-CAPABILITY-PACKS.md` and manifest, `assurance/audits/C7-FFA-003.md`, C1 research, C4 Pattern F, and current `OPEN-QUESTIONS` / `DEPENDENCY-REGISTER`.
3. Correct stale statements such as the C7 audit being unavailable. The current repository contains `C7-FFA-003.md`. Distinguish the nonexistent older filename `C7-CLOUD-EVOLUTION-FINAL-AUDIT.v3` from the actual audit.
4. Check the mismatch between the five-vector Plan/Act requirement and any C2 test row that covers only a direct write-tool call. Create a source-backed correction proposal; do not silently alter the taxonomy or change security policy.
5. Preserve all six RP-13 questions as open: key custody, authorized identity, replay, expiry, revocation/in-flight semantics and exact-payload binding. No cryptographic scheme or token policy is chosen by C2 in this task.
6. Record every human decision, missing runtime prerequisite, oracle, positive control, mutant check, exact test ID, fixture, expected reason, evidence bundle and closure criterion.
7. Produce the candidate Markdown and manifest, an extraction/provenance note, and a short list of proposed corrections to C2's current future pack. Do not edit shared registers or the current canonical C2 files.

**C2 final report:** source inventory; raw extraction SHA; corrected candidate SHA; changes vs raw extraction; cross-cloud discrepancies; decisions still open; tests explicitly not executed.

---

# C3 — Context Isolation, Evidence Freshness and Resumption

**Work concurrently; output only to the C3 staging directory.**

Review TXT lines 567–968. Target candidate: `assurance/experiments/C3-CONTEXT-ISOLATION-AND-RESUMPTION-PLAN.md` plus a companion manifest.

1. Preserve a raw extraction and record the TXT SHA and exact line range.
2. Revalidate against current C3 research and future pack, current C1 design, C2 trust boundaries, C4 execution/side-effect semantics, C5 operator flows and C6 evaluation plan. The prior draft's statements that C1, C2–C5 packs, `OPEN-QUESTIONS.md`, `DEPENDENCY-REGISTER.md`, and `NEXT-ACTIONS.md` were absent are false for the current AI-OS `main`; correct them in the candidate.
3. Search current and historical artifacts for Wave 3.5 schema definitions and any true missing convergence patch. Do not say a schema is missing simply because it was not supplied into the earlier isolated session.
4. Preserve ownership: C3 owns context semantics, isolation, freshness, provenance and context resumption requirements; C4 owns mutations and side effects; C2 owns authorization decisions; C5 owns operator-facing flows; C6 owns evaluation method; C1 ratifies cross-cloud contracts.
5. Include fixture definitions, controlled staleness conditions, independent oracles, concurrency and leakage cases, interruption points, evidence chain checks, result statuses, and regression-retention rules.
6. Do not invent tier ceilings, token budgets, retry guarantees, freshness windows, compression windows, acceptable leakage counts beyond source-defined zero-tolerance requirements, or a checkpoint owner where the source disagrees.
7. Output candidate plan + manifest + source traceability/correction log. Never claim a checkpoint, memory service, isolation mechanism or test was implemented/executed.

**C3 final report:** corrected claims; evidence that was found vs not found; exact outstanding C1/C2/C4/C5/C6 dependencies; thresholds that remain unset.

---

# C4 — Plan/Act Mutation Matrix and Wave 3.5 Recovery Correction

**Work concurrently; output only to the C4 staging directory.**

Review TXT lines 971–1218 for the matrix and lines 1220–1351 for the recovery report.

### Deliverable A — normalized matrix

Candidate: `assurance/experiments/C4-PLAN-ACT-MUTATION-TEST-MATRIX.md` plus a manifest.

1. Preserve raw extraction and TXT line provenance.
2. Compare directly against current C1 source `clouds/C1/C1-CLOUD-HARNESS-ADAPTER-RESEARCH.md`, C2 RP-1 / test matrix, C4 Pattern F, C6 integration vectors and C7-FFA-003. Do not repeat the previous report's claim that C1 source was unavailable.
3. Distinguish the original five-vector acceptance taxonomy from the union of all distinct concrete attack mechanisms. Verify whether the previously reported seven-vector union survives line-by-line source comparison. Show an explicit many-to-many map; never force unlike mechanisms together merely to retain a count of five.
4. The oracle for PLAN must show mutation capability absent or structurally blocked at the execution boundary, not merely a prompt refusal or a log message. Keep the actual security test `TEST SPECIFIED / NOT EXECUTED` because no runtime exists.
5. Separate PLAN-side vectors from ACT-side authorization/idempotency/rollback preconditions; identify owners instead of taking over C2/C6 policy.

### Deliverable B — corrected recovery report

Candidate: `assurance/experiments/C4-WAVE35-ARTIFACT-RECOVERY-REPORT.md` plus a manifest.

The prior recovery report is factually stale. Current AI-OS main contains `archive/historical/wave3.5/C4-WAVE3.5-CONTEXT-v2.manifest.yaml`. Its relevant fields include:
- `repo_target: kkbb22/ARGON-HEALTH`
- `filename: C4-WAVE3.5-CONTEXT-v2.md`
- expected SHA-256 `22ca9931e0799e3285ac802f65677bc0859790acb9081b65addc340477f60a90`
- `verified_repo_head: 3520d70946f6623875c6f7d6ea47ef40f5bcc316`
- supersedes a v1 named `C4-WAVE3.5-ARGON-CONTEXT-MODEL.md` with a separate hash.

1. Read the actual manifest bytes and record their blob SHA.
2. Keep repository boundaries strict: this manifest is archived inside AI-OS but declares its target as ARGON-HEALTH and points to health-repository evidence. Do not reclassify its content as canonical AI-OS or modify ARGON-HEALTH.
3. Search current ARGON-HEALTH main and the exact `verified_repo_head` tree/history for both the v2 and v1 filenames and the expected SHA. State precisely what was searched and what was found. A manifest's existence proves metadata exists, not that the Markdown is recoverable.
4. If exact original bytes are absent, do not fabricate them or create any file under either original historical filename. Recommend either retaining the orphan manifest and missing-source note, or a separately named `C4-WAVE3.5-CONTEXT-RECONSTRUCTION-v1.md` clearly labeled reconstruction, not recovery, pending owner authorization.
5. Correct all claims that the manifest itself was unavailable. Keep all health source references read-only and report the historical artifact's cross-repository nature.

**C4 final report:** exact matrix mapping; source-supported corrections; recovery search evidence; original source status; no reconstruction or tests claimed unless actually done.

---

# C5 — Operator-Control Acceptance Tests and v1 Provenance

**Work concurrently; output only to the C5 staging directory.**

Review TXT lines 1354–1508 (v1 baseline recovery) and 1511–1767 (operator acceptance tests).

1. Preserve raw extractions and source line ranges for both documents.
2. Search the current repo, all Git refs/history, `evidence/MANIFEST.json`, `evidence/source_moves_registry.json`, every relevant archive/ZIP in `archive/external-health/` and `archive/duplicates/`, C5 manifests, and all versions/references for the original C5 future-pack v1 filename and claimed hash. Search the contained-file listings without executing any archive contents.
3. Determine whether the original v1 bytes can be recovered exactly. If found, compute SHA-256 from the actual bytes and compare with the claimed value. If not found, state `NOT RECOVERED`; do not call the v2 pack a recovered v1 and do not invent missing original test IDs.
4. Produce a v1 provenance report that lists each candidate, path or commit/archive source, expected hash, actual hash, and reason it is or is not the exact original.
5. Review current C5 v2 pack and the supplied operator test suite. Create/retain `assurance/experiments/C5-OPERATOR-CONTROL-ACCEPTANCE-TESTS.md` as a self-contained candidate, with a companion manifest. Map each test ID to an existing source requirement. Distinguish inherited IDs that are proven from newly assigned test IDs and IDs whose historical lineage is unknown.
6. Correct stale claims that C1/C7/current C3/C6 files or shared registers were unavailable when they are present in the current repository. Preserve the boundary between UI clarity, human-comprehension research, operator workflow and backend security enforcement.
7. Preserve thresholds, sample sizes, STOP latency, pause/resume decisions and human-study requirements as open whenever no owner decision or valid evidence exists.

**C5 final report:** v1 recovery verdict with exact proof; ID lineage table; tests specified vs actually executed; UI/backend ownership; outstanding interfaces and human decisions.

---

# C6 — Future Evaluation Capability Packs

**Work concurrently; output only to the C6 staging directory.**

Review TXT lines 1771–2240. Candidate target: `capabilities/future/C6/C6-FUTURE-EVALUATION-CAPABILITY-PACKS.md` plus `C6-FUTURE-EVALUATION-CAPABILITY-PACKS.manifest.yaml`.

1. Preserve the raw extraction and record the source TXT SHA and exact range.
2. Reconcile the pack with the live C6 engine and manifest, current C2–C5 source artifacts and future packs, C1, C7-FFA-003, capability index and dependency/unknown registers. The previous draft's claims that these repository files were absent are outdated; correct them.
3. Preserve the five current proposed packs unless a source-backed finding shows duplication or a missing capability: (001) evidence-backed state transitions, (002) adapter/gate integration vectors, (003) interruption/resume/failure injection, (004) cross-cloud regression and traceability, (005) value-for-cost experiments.
4. For every pack, give owner, property, prerequisite, fixture, oracle, test IDs, expected result, sensitivity/mutant check, evidence record, metrics, unknown thresholds and closure rule.
5. Keep the C6 role limited to evaluation design and evidence conventions. Do not decide C2 security policy, C3 semantic contracts, C4 execution mechanics or C5 operator policy.
6. Do not claim test results or measurements. Keep `THRESHOLD NOT SET` and `BLOCKED` where appropriate.
7. Verify manifest compatibility against current C2/C4/C5/C6 manifest conventions. Compute the candidate Markdown's exact SHA-256, store it in the manifest according to the established convention and verify it independently. Keep source TXT hash and artifact hash as separate fields.
8. Prepare a proposed capability-index row as a separate snippet only; do not edit shared index/registers in this task.

**C6 final report:** five-pack traceability table; manifest and SHA result; corrected stale-source assumptions; missing interface contracts; tests/metrics not executed.

---

# C1 — Cross-Cloud Synthesis v2 (two-stage task; do not wait idle)

**Work only in a separate C1 staging directory.**

### Stage A — immediate, while C2–C6 work

1. Verify current `ARGON-AI-OS/main` SHA and inspect whether the reported local untracked file exists at `clouds/C1/ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.md`.
2. If it exists, copy it unchanged to a protected backup outside the repository, calculate exact-byte SHA-256 and preserve its original path/status. Never overwrite it. If it does not exist, report this fact and create no fictional provenance.
3. Review the draft against current C1–C6 research, capability packs, C7-FFA-003, `STATUS.md`, `NEXT-ACTIONS.md`, `OPEN-QUESTIONS.md`, `DEPENDENCY-REGISTER.md`, and capability-index. Produce a claim-to-source traceability matrix and a prioritized correction list immediately.
4. Reconcile the original five-vector acceptance taxonomy against C2/C4's complete concrete-vector inventory without hiding non-equivalent vectors. Include the distinction between a policy taxonomy and a larger concrete attack coverage set.
5. Correct the path conflict: `STATUS.md` points to `clouds/C1/...v2.md`, while `NEXT-ACTIONS.md` points to `architecture/synthesis/...v2.md`. The candidate canonical path is `clouds/C1/ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.md`; do not create duplicates.
6. Preserve RP-13 and delegation-depth as `NEEDS EXPERIMENT` / proposal where appropriate. Describe delegation depth = 1 as ARGON's own design proposal, not a verified vendor capability. Preserve the C1/C2/C4/C6 boundaries and self-verification restriction.
7. Do not claim C2–C6 new deliverables are canonical yet. List them as pending inputs until integrated and reviewed.

### Stage B — after C2–C6 candidates have been integrated into a single review worktree

Update the synthesis candidate to cite the final exact paths and SHA-256 values of the accepted C2–C6 deliverables. Revalidate all claims, open questions, experiment states, source references and manifests. Output the finished synthesis candidate, a change log from the preserved draft, and a final traceability table. Do not edit the repository's shared registers; provide proposed exact updates separately for the integration owner.

No commit/push. No architectural decisions invented. Do not claim C7 approval in advance.

---

# C7 — Immediate privacy and public-exposure triage (run first)

**READ-ONLY. Do not change repo visibility, delete files, rewrite history, rotate secrets, commit, push or open a PR.**

Review the full public `kkbb22/ARGON-AI-OS` repository at its current verified default-branch commit and inspect accessible history/references. `ARGON-HEALTH` may be consulted read-only only to understand provenance; do not modify it. Do not inspect or mix in legacy production systems.

Priority scope includes all of `archive/external-health/`, especially:
- `ARGON-HEALTH-main (3).zip`
- `ARGON-HEALTH-Assurance-Kit-v1.0.zip`
- `argon-assurance-merge-P0.zip`
- healthcare analysis PDF/DOCX
- the tracker XLSX and dashboard/screenshots
- medical UI HTML/PDF guides
- screenshots and embedded metadata
- `evidence/` archives, manifests and source-move registry.

1. Enumerate the current public tree and all archive contents safely. Do not execute code from archives. Inspect PDFs, DOCX, XLSX (including hidden sheets, comments, document properties and embedded objects), HTML, images/screenshots and ZIP members with suitable local/offline tools. Do not upload artifacts to third-party scanners or services.
2. Review current files and accessible Git history for:
   - actual patient/clinical data, real or plausibly identifying medical records, names linked to diagnoses, MRNs, birth dates, phone/address combinations, appointment/treatment information, patient images;
   - real staff/customer personal data beyond intended public attribution;
   - credentials/tokens/private keys/session cookies or sensitive connection strings;
   - internal endpoints, signatures, proprietary material or archive contents that should not be public according to repository context.
3. Classify every finding as `CONFIRMED SENSITIVE`, `POSSIBLE/AMBIGUOUS`, `SYNTHETIC/DEMONSTRATION`, `PUBLIC REFERENCE MATERIAL`, or `NO ISSUE OBSERVED`. A document about healthcare or a fictional sample is not automatically PHI. Use evidence appropriate to the classification.
4. Do not repeat suspected patient data, tokens or full personal identifiers in your report. Provide path, commit/hash, page/sheet/member, category, confidence and a short redacted evidence description only.
5. If confirmed sensitive data or a live credential is discovered, immediately report a P0/P1 finding to the owner and recommend containment: owner-led visibility decision, credential revocation/rotation where applicable, and a controlled historical purge if approved. Do not perform these changes yourself.
6. Check whether the `ARGON-HEALTH-main (3).zip` contains a faithful copy of the separate target-architecture repository and whether it contains anything beyond public architecture docs. Do not treat a bundled repo as proof of patient data; inventory its members and perform the same privacy checks.
7. Report scan coverage and limitations precisely. Zero pattern hits is not proof of zero secrets/PHI. Identify unscanned binary formats, inaccessible history, encrypted archives or unsupported formats explicitly.

**C7 privacy deliverable:** `ARGON-AI-OS-PUBLIC-REPOSITORY-PRIVACY-TRIAGE.md` in C7 staging only, with severity, exact evidence path/hash, exposure status, containment recommendation and no sensitive values inlined. End with one clear outcome: `NO CONFIRMED SENSITIVE MATERIAL FOUND WITHIN STATED SCOPE`, `POSSIBLE EXPOSURE REQUIRES OWNER REVIEW`, or `CONFIRMED EXPOSURE — IMMEDIATE OWNER ACTION REQUIRED`.

---

# C7 — Final independent synthesis audit (run later, not concurrently)

Only begin after C2–C6 deliverables and C1 synthesis have been integrated into one review worktree, their exact hashes recorded, and no further edits are planned during audit.

1. Review `clouds/C1/ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.md` against the exact current versions of all C1–C6 research files, packs, experiment plans, manifests, current dependency/open-question registers and `C7-FFA-003.md`.
2. Independently verify input manifests and output SHA-256 values. Trace each major synthesis claim to exact source sections; do not use the synthesis itself as evidence.
3. Audit cross-cloud consistency for Plan/Act taxonomy, C2 RP-13, C3 isolation/resumption, C4 execution/rollback, C5 operator controls, C6 evaluation records/thresholds, C1 checkpoint/Kernel duties, and the C4/C5 recovery/provenance reports.
4. Confirm that no future capability is promoted from `DESIGNED` to `IMPLEMENTED`, and no test from `TEST SPECIFIED` to `TEST EXECUTED` or `PASS WITH EVIDENCE` without records tied to the exact tested artifact revision.
5. Check archive/history recovery claims, especially that the C4 Wave 3.5 manifest exists in AI-OS's historical archive but declares `repo_target: kkbb22/ARGON-HEALTH`; verify that the missing original has not been fabricated or mislabeled as recovered.
6. Check C5 v1 provenance and test-ID lineage; check all cross-references, single canonical synthesis path, manifest schemas, hash chain and source status claims.
7. Do not author or fix the reviewed artifacts. Report findings only, severity-ranked, with exact path and source reference plus minimal correction. Independent review must not self-certify.

Create `assurance/audits/C7-FFA-004.md` only as a staging candidate. Verdict must be one of `CLEAN WITH OPEN EXPERIMENTS`, `CORRECTIONS REQUIRED`, or `BLOCKED BY MISSING EVIDENCE`. State explicitly that this is a document/consistency audit, not runtime security certification.

---

## Integration owner — final controls

No cloud agent may edit `STATUS.md`, `NEXT-ACTIONS.md`, `OPEN-QUESTIONS.md`, `DEPENDENCY-REGISTER.md` or `capabilities/capability-index.md` during parallel work. After all individual outputs are reviewed, a single integration owner should:

1. Compare candidate diffs and the exact local C1 draft before applying anything.
2. Resolve filenames, provenance and manifest schemas.
3. Apply accepted changes to a dedicated review branch only.
4. Update shared registers once, serially.
5. Run link/path checks, manifest hash verification and a secret/privacy re-scan on the proposed diff.
6. Present the complete diff and permission summary to the owner.
7. Stop. No commit, push, PR, merge, repository visibility change, deletion or Wave 4 runtime work without explicit authorization.
