# ARGON Security and Governance Status

**Cut-off:** 2026-11-04  
**Posture:** HOLD — no autonomous execution, no protected writes, no Wave 4 clearance.

> **Critical distinction:** PR-09 findings dated 2026-11-02 were supplied as a summary in the user's handover. They are treated as reported findings until the original report, source revision and logs are provided. Separately, static inspection of current AI-OS `main` (`1458a7f...`, PR #8 merge) found source paths that do not match at least part of the reported remediation. This is not proof that the local PR-09 follow-up branch lacks the fixes; that local branch was not accessible.

## 1. Executive security decision

**Autonomous execution remains on HOLD.**

The available evidence does **not** support:

- enabling autonomous or unattended repository writes;
- treating PLAN/REVIEW/APPROVAL/ACT/VERIFY as mechanically enforced across all mutation routes;
- treating Docker isolation as runtime proven;
- treating a local SHA-256 JSONL chain as tamper-proof or nonrepudiable;
- accepting a plain local-operator string as a trustworthy authenticated approver identity;
- allowing ARGON-AI-OS to write to ARGON-HEALTH or any production/patient data;
- claiming C7-FFA-004 clean closure or Wave 4 authorization.

C7-FFA-003's `CLEAN WITH OPEN EXPERIMENTS` is an earlier audit of the canonical C1–C6 research package. It is not a security certification of PR #8's runtime.

## 2. PR-09 historical audit findings supplied by the user

The handover says the earlier PR-09 independent review issued `REQUEST CHANGES — AUTONOMOUS EXECUTION ON HOLD` and a later forensic audit (2026-11-02) reported:

### Reported remediation claims

1. Direct host subprocess execution was reportedly removed from ToolRegistry path and routed through VerificationEngine.
2. Docker execution configuration reportedly included network isolation, a non-root user, dropped capabilities, no-new-privileges, resource limits and workspace mounting.
3. Verification reportedly became fail-closed when required verification commands are missing or unsuccessful.

### Reported remaining critical issues

- Docker isolation was **not runtime-verified** because Docker daemon was unavailable.
- Docker image was mutable and not digest-pinned.
- Configured Python image reportedly lacked Git and pytest tooling.
- SEC-03: approver identity was an unauthenticated local-operator string.
- SEC-04: local SHA-256 audit chain remained vulnerable to privileged local rewriting.

### Reported additional issues

- stdout/stderr memory buffering;
- nonce synchronization race;
- missing custom seccomp profile.

### Reported governance state

- PR-09: `REQUEST CHANGES`;
- C7-FFA-004: `OPEN`;
- autonomous execution: `HOLD`;
- Wave 4: `BLOCKED`;
- ARGON-HEALTH machine write operations: `PROHIBITED`.

**Evidence class:** REPORTED BY USER from the supplied handover. The original 2026-11-02 audit file and full logs are not currently available. These findings must not be silently closed.

## 3. Reconciliation against current AI-OS `main`

Inspected repository revision: `1458a7f54f5d190ff84fce66cb2568960ff73559` (merge PR #8). The following are static source observations, not execution test findings.

| Control | Current source observation | Security interpretation |
|---|---|---|
| Host subprocess containment | `runtime/core/tools.py` contains a direct `subprocess.run` call in ToolRegistry's verification-command handler. | The PR-09 report's claim that the ToolRegistry host subprocess path was removed is not reflected in this inspected `main` path. Confirm whether PR-09 follow-up code is missing from main or whether another wrapper is intended. |
| Verification subprocess | `runtime/core/verifier.py` also calls `subprocess.run` directly with a workspace cwd and `shell=False`; it has executable-name/argument filtering. | `shell=False` and command allowlisting reduce some risks but do not prove OS/container isolation. The path still invokes host process execution unless an external boundary not visible in these files is in force. |
| Docker isolation | No Docker API/configuration, digest pin, container entrypoint, or seccomp profile was identified in the inspected ToolRegistry/VerificationEngine path. | Docker containment is NOT VERIFIED FROM CURRENT SOURCE PATHS. This is not a full repository-wide search or runtime experiment; PR-09 local branch still needs exact inspection. |
| Approver identity / SEC-03 | `runtime/core/policy.py` uses a plain string approver with defaults such as `local-operator`/`operator`; the caller supplies that string. | No authentication/identity proof is visible in the inspected code. SEC-03 remains OPEN unless an external authenticated principal boundary is demonstrated. |
| Nonce storage and replay | Consumed nonce registry is a local JSON file. The loader resets to an empty set when file I/O/JSON parsing fails; save/read-check-write is not protected by an inter-process lock or atomic transaction in the inspected path. | Fail-open replay-state loss and race conditions are plausible source-level defects. A corrupt state file must not restore consumed approvals. Nonce consumption needs concurrency/rollback tests and fail-closed recovery. |
| Audit ledger / SEC-04 | `runtime/core/evidence.py` describes a local JSONL SHA-256 chain and notes that a privileged writer can rewrite the complete chain. | It is a tamper-evidence convenience, not a protected immutable audit log or cryptographic nonrepudiation. SEC-04 remains OPEN. |
| stdout/stderr buffering | Tool execution captures output in memory and returns captured content. | This is consistent with the reported memory-buffering issue; size/time/streaming/secret-redaction controls need explicit limits and tests. |
| seccomp / least privilege | No custom seccomp policy or verified runtime profile was found in the inspected execution code. | Missing/NOT VERIFIED. A Docker flag in a configuration is not proof the daemon actually enforced it. |
| Task/contract enforcement | Task/contract classes carry allow-path/tool fields, but the effective enforcement path requires a source-to-runtime review and adversarial tests. | Do not assume contract metadata enforces a boundary until execution tests show denied actions cannot cross it. |
| Health pipeline | `runtime/core/health_pipeline.py` is a small in-memory demo pipeline using synthetic records/tenant comparison, not a database/API/FHIR application. | No clinical application readiness, tenant RLS or production-grade patient-data control can be inferred. |

Relevant current source paths:

- `runtime/core/tools.py` (blob SHA observed: `b59487f7794e151fdee976c268aa7899e527c854`)
- `runtime/core/verifier.py` (blob SHA observed: `c186331a62f91a337c01686cc0982d31319a5aa3`)
- `runtime/core/policy.py` (blob SHA observed: `8a969a641fa62e5791db90e9cda6c616f94f4afb`)
- `runtime/core/evidence.py` (blob SHA observed: `fc52c6ef07865f744784fee44c41fd59f5735fcb`)
- `runtime/core/orchestrator.py`
- `runtime/core/workspace.py`
- `runtime/core/health_pipeline.py`
- `runtime/argon_runtime.py`

## 4. SEC-01 through SEC-04 status

The supplied material explicitly names SEC-03 and SEC-04 but does not provide the canonical definitions of SEC-01 and SEC-02. Do not invent the missing definitions.

| ID | What can be stated | Status |
|---|---|---|
| **SEC-01** | Canonical issue definition/closure criterion not supplied in the available handover. | `UNKNOWN — EVIDENCE REQUIRED` |
| **SEC-02** | Canonical issue definition/closure criterion not supplied in the available handover. | `UNKNOWN — EVIDENCE REQUIRED` |
| **SEC-03** | Reported approver identity is unauthenticated local-operator string; current inspected policy source uses caller-provided plain string defaults. | `OPEN — source concern independently observed; auth proof absent` |
| **SEC-04** | Reported local SHA-256 chain susceptible to privileged rewrite; current inspected audit-ledger source explicitly acknowledges rewrite by privileged writer. | `OPEN — source limitation independently observed` |

## 5. PR-09 follow-up worktree/branch reconciliation

User handover identifies:

```text
Worktree: D:/aoswork-pr09-followup
Branch:   fix/pr09-security-containment-followup
HEAD:     23fb2733549d8c84d8d58817cd0586ac3047fdcc
```

Read-only remote checks during this investigation:

- Remote branch search did not return `fix/pr09-security-containment-followup`.
- GitHub lookup for commit `23fb2733549d8c84d8d58817cd0586ac3047fdcc` returned no commit for that SHA.

**Interpretation:** the referenced local branch/commit is not verified on the accessible GitHub remote. It may still exist locally. Do not delete, reset, rename, rebase or overwrite it. Obtain read-only `git status`, `git branch -vv`, `git log`, exact HEAD, `git diff` vs base, untracked inventory and patch/export before deciding whether to integrate anything.

## 6. Runtime implementation is not runtime assurance

PR #8 added actual source files and tests to AI-OS. The merge included compiled `__pycache__` artifacts, a demo task, local approval record, consumed-nonce file, audit log and sandbox example outputs. These files are evidence of repository contents/demo state, not proof that a clean independent run passed.

An October 21 PowerShell transcript showed nine earlier local tests passing (`Ran 9 tests`, exit code 0) on Python 3.14.3. At that time, `runtime/` and `tests/` were untracked in that local worktree. This test result is not for the later 48-file PR #8 change or current main. No current-main runtime test report, container isolation result or mutation-suite run was available.

The standalone `runtime/argon_runtime.py` contains a separate `APPROVE <SHA-256>` text challenge with ten-minute expiry and sandbox writes. That mechanism must be reconciled with `runtime/core/policy.py`'s ApprovalRecord path. Multiple approval surfaces without a single clearly enforced authority boundary create integration and test obligations; they are not automatically equivalent.

## 7. C7 and governance record

| Artifact | Date / baseline | Verdict or status | What it actually covers |
|---|---|---|---|
| C7-FFA-003 | 2026-10-07; research package | `CLEAN WITH OPEN EXPERIMENTS` | C1–C6 research package in scope; not runtime security. |
| C7-FFA-004 Revision 5 | Audit date 2026-10-19; synthesis v2.1.1 candidate | `NOT ISSUED — no clean verdict` | Gate 1 partial/blocked; structural completeness pass; source-to-claim partial; cross-Cloud partial/open; decision/gate sequence partial; dependency sequence blocked/partial; no runtime authorization. |
| User-supplied PR-09 audit summary | Reported date 2026-11-02 | `C7-FFA-004 OPEN` | Full original audit report not supplied; treat as reported and unresolved. |
| Current `main` C7-FFA-004 file | Checked 2026-11-04 | Not found at `assurance/audits/C7-FFA-004.md` | Absence from checked path does not prove no local/staging report exists. |

Governance blockers must remain:

- C1 synthesis v2 integrated as draft, not clean C7-approved.
- C6 accepted design-only; its evaluation packs are not runtime implementation.
- OQ-03/H-09 Plan/Act taxonomy decision remains open. Five C1/C2 requirements, a six-route possible union and seven concrete C4 PAM test cases are different counting units; do not collapse them into a chosen count without source mapping and human acceptance.
- C2 RP-13 remains `NEEDS EXPERIMENT` / human decision.
- C3 context isolation, freshness and resumption remain unimplemented/untested.
- C4 mutation matrix/rollback behavior remains unexecuted.
- C5 operator control tests remain specifications; original v1 lineage not recovered.
- Wave 4/ACT flow remains unauthorized by current evidence.

## 8. Public repository privacy and data handling

The Phase Zero review (2026-10-17) flagged a screenshot in `archive/external-health/` that appeared to contain administrative domain/DNS validation material. Its live validity was **UNKNOWN**. Do not repeat the value or assume it is a credential. The prior intake PR's reported zero-finding scan does not resolve whether that datum is current or whether all archive/binary contents were reviewed.

C7's 2026-10-14 prompt pack required offline inspection of archives, PDFs, DOCX, XLSX hidden sheets/comments/properties/embedded objects, HTML, images, and history, with redacted reporting. It required a privacy triage outcome. No completed privacy-triage report was located in the checked main path or available Library inventory. Status is `UNKNOWN — EVIDENCE REQUIRED`, not “no sensitive data.”

If an owner confirms a live DNS/token value is exposed, containment/revocation and history cleanup must be owner-approved, with evidence preserved. No such action was performed here.

## 9. Non-negotiable security gates before any future ACT

1. Pin a clean source baseline and reconcile the PR-09 follow-up branch against main.
2. Establish authenticated approver identity and a trustable authorization boundary; caller-supplied display strings do not qualify.
3. Bind approval to exact action, repository, immutable ref, paths, payload/diff, expiry, nonce and revocation semantics; decide RP-13 cryptographic investment before implementation.
4. Prove no mutation-capable path exists in PLAN/REVIEW, across direct tools, shell/interpreter, wrapper/composite tools, nested calls and side effects caused by arguments. Keep the source-defined vectors separately mapped until H-09/OQ-03 closes.
5. Execute ACT only inside a pinned, least-privilege, digest-pinned isolated environment with network/file/process controls; runtime verify daemon, image digest, seccomp, user, capabilities and resource limits.
6. Make missing verification dependencies and corrupted replay state fail-closed; make nonce consume atomic under concurrent attempts.
7. Seal audit evidence outside the same privileged rewrite boundary; use an independent append-only/WORM or signed record mechanism selected by an approved design, not a self-referential hash chain alone.
8. Bound and redact stdout/stderr; verify no secrets/patient data are copied into model context or logs.
9. Run adversarial tests and independent verification bound to exact source/image/test fixture hashes.
10. Keep merge, release and all ARGON-HEALTH production writes human-controlled and separately authorized.

**Until every applicable gate has independent evidence and the human authority explicitly approves, posture stays HOLD.**
