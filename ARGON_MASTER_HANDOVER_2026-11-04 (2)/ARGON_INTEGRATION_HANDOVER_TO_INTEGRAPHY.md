# ARGON Integration Handover to Integraphy

**Handover cut-off:** 2026-11-04  
**Mode:** READ-ONLY reconstruction; this document is an instruction/evidence handover, not authorization to mutate repositories.

## 1. Mission on return

Resume the existing ARGON program from its actual repository and security state. Do not restart research, replace architecture, or treat the runtime merge as authorization. Reconcile the exact PR-09 follow-up worktree and the 2026-11-02 audit against AI-OS `main`, then prepare a reviewable evidence packet for independent C7 assessment.

## 2. Canonical repository boundaries

| Repository | Current remote `main` | Responsibility | Restrictions |
|---|---|---|---|
| `kkbb22/ARGON-AI-OS` | `1458a7f54f5d190ff84fce66cb2568960ff73559` | Controlled engineering automation machine | No autonomous write, no Wave 4/ACT, no merge/implementation based on PR #8 title alone. |
| `kkbb22/ARGON-HEALTH` | `fb6e3e38a09769e434dd9a40fb6590c8903ed744` | Target medical architecture/product repository | Read-only for this handover. No machine write operations, no production/patient data, no architecture rewrite. |
| Legacy ARGON / Firebase | Not inspected | Existing legacy production context | Keep separate; no migration or modification under this handover. |

The target Health “no Firebase” constraint needs explicit reconciliation with any existing README/ADR text that still mentions a Firebase-based incremental stage. Do not run or modify Legacy or infer permission from a stale README.

## 3. Evidence-backed state Integraphy should accept as its starting point

1. AI-OS PR #1 established the research/evidence organization baseline.
2. AI-OS PRs #2–#6 added governance intake and accepted C6 future evaluation packs design-only. The C6 packs remain `DESIGNED / NOT_IMPLEMENTED`; tests executed and evidence-backed passes are zero.
3. AI-OS PR #7 integrated C1 synthesis v2 as a draft for independent audit. It is not an approval to implement Wave 4.
4. AI-OS PR #8 added initial runtime/core code and tests on 2026-10-24. The code is real source; current-head successful test evidence and independent security validation were not available.
5. `STATUS.md` predates PR #7 and PR #8 and is stale relative to main. Do not trust it as sole status authority.
6. C7-FFA-003 is an earlier research-package audit, not runtime certification.
7. C7-FFA-004 Rev5 (Library copy, audit date 2026-10-19) gave `NOT ISSUED — no clean verdict` for the v2.1.1 candidate. The 2026-11-02 PR-09 report summary says C7-FFA-004 remains OPEN.
8. PR #8 current source has direct subprocess calls in ToolRegistry and VerificationEngine, caller-provided local approver strings, a non-atomic local nonce registry, and a privileged-writer rewrite limitation in the local SHA-256 audit ledger. Reconcile these against the PR-09 follow-up branch before asserting fixes.
9. HEALTH is an architecture/assurance repository, not an implemented clinical application. No application backend/frontend/database/integrations/deployment were established in the inspected current ref.

## 4. First assignment: preserve and reconcile the PR-09 follow-up (no mutation)

User-supplied expected local details:

```text
Worktree: D:/aoswork-pr09-followup
Branch:   fix/pr09-security-containment-followup
HEAD:     23fb2733549d8c84d8d58817cd0586ac3047fdcc
```

The accessible GitHub remote lookup did not find this branch or commit. This does not prove it is absent locally.

**Required evidence export (read-only):**

- repository root and remote URLs (redact credentials);
- `git status --short --branch`;
- `git branch -avv` and `git log --oneline --decorate --graph -30`;
- exact `HEAD`, merge-base/base SHA and parent commit IDs;
- `git diff --stat` and full diff against the documented base;
- tracked and untracked file inventory with SHA-256;
- `git show --stat` and `git show` for relevant remediation commits;
- full 2026-11-02 forensic audit, exact report hash, command transcript and tool versions;
- Docker daemon status at time of audit, image reference and immutable digest, container config, effective UID/capabilities/network/seccomp/resource settings, workspace mount details and the command/run logs;
- exact tests executed, fixture hashes, exit codes and complete stdout/stderr.

Do not rename, reset, rebase, clean, stash, cherry-pick, merge, commit, push, or delete any local branch or worktree during collection. Keep a byte-preserving copy of the branch patch and evidence.

## 5. Code/security reconciliation matrix

| Concern | Main source path / observation | Required Integraphy action |
|---|---|---|
| Direct process execution | `runtime/core/tools.py` has a ToolRegistry `subprocess.run` path. | Compare exact PR-09 branch to main. Demonstrate where process execution actually occurs and whether it is inside a separately enforced container boundary. Avoid relying on function naming or prompt restrictions. |
| Verification execution | `runtime/core/verifier.py` calls `subprocess.run` directly. | Trace the complete call chain, executable and argument allowlist, environment inheritance, cwd, path access, timeout and output limits. Test command/argument injection and path escapes. |
| Docker containment | No Docker boundary visible in the inspected paths; November 2 summary says Docker not runtime-tested. | Provide a pinned image digest and actual daemon-run logs. Test the effective runtime properties, not only Docker config values. If daemon was unavailable, remain NOT VERIFIED. |
| Approver identity (SEC-03) | `runtime/core/policy.py` accepts a plain `approver` string with local defaults. | Define the authenticated principal boundary, identity assertion source, authorization rule and audit binding. Test spoofed/default/missing identities. |
| Replay/nonce | Local JSON file; error recovery can reset to empty set; read/check/write not atomic. | Fail closed on corrupt/missing state; lock/transactional consume; concurrent duplicate requests; crash consistency; expiry/revocation tests. |
| Audit ledger (SEC-04) | `runtime/core/evidence.py` documents that a privileged writer can rewrite the whole chain. | Do not call it tamper-proof. Propose an independently protected append-only or signed record with separate trust boundary, then test a privileged rewrite attempt. |
| Output buffering | Captured stdout/stderr returned in memory. | Establish byte/time caps, truncation policy, redaction and secret exclusion, and tests for large/hostile output. |
| seccomp/least privilege | No custom seccomp profile observed in inspected path. | Verify runtime effective profile and test denied syscalls; a configured profile alone is not a pass. |
| PLAN mutation boundary | C1/C2 five surfaces, C4's distinct argument-caused side-effect vector; C4 also has PAM-01…07 test cases. | Retain source IDs and many-to-many mapping. Do not choose 5/6/7 by convenience. The human H-09/OQ-03 decision remains required. Test absence of mutation capability at the execution boundary. |
| Verification fail-closed | User's Nov2 summary says missing/failed verification commands block execution. | Inspect exact PR-09 code and adversarial tests for missing executable, false exit, timeout, crash, incomplete output and altered verification config. |
| Approval path convergence | Separate `runtime/argon_runtime.py` SHA prompt and `runtime/core/policy.py` ApprovalRecord machinery exist. | Document one authoritative approval model and explicitly deprecate/contain any demo-only alternate path. Test expiry, one-use, payload mutation, identity and revocation. |

## 6. Cross-Cloud intake: preserve rather than repeat

- C1: v2 in main is a draft. v2.1.1 Library candidate and C7 Rev5 report are separate artifacts. Reconcile exact filenames, hashes, correction matrix and final C7 report.
- C2: RP-13 candidate v3 exists; 55 tests/12 scenarios specified, zero executed; six technical questions remain open.
- C3: r3 candidate held as staging; source extraction exists, but review found missing audit tooling/output/fixture payloads; zero executed.
- C4: mutation matrix/recovery package is partial; taxonomy unresolved; C4 Wave 3.5 manifest exists but original Markdown is not verified/recovered.
- C5: r3 specifies 18 operator tests; no runtime execution; original future-pack v1 NOT RECOVERED; AT-17 routing blocked by IC-9.
- C6: accepted into main as design-only via PR #5 and integrity correction PR #6; zero pack tests executed.
- C7: FFA-003 is not FFA-004. FFA-004 Rev5 is no-clean. Privacy triage completion was not established.

Do not rerun Cloud research from scratch. First inventory exact staging files and manifests. Preserve old candidates byte-for-byte; create a new revision only when a correction is authorized and evidenced.

## 7. Required validation work product before any implementation recommendation

Deliver one revision-pinned audit packet containing:

1. Baseline and candidate SHAs, clean/dirty worktree state and patch hashes.
2. PR-09 forensic report plus complete raw test/container logs.
3. File-by-file code review and a threat-to-control-to-test traceability matrix.
4. C1–C7 candidate inventory, manifest matches, provenance gaps and acceptance status.
5. Explicit unresolved human decisions (including H-09/OQ-03, RP-13 decision, approver model, checkpoint/resumption, threshold/STOP values).
6. Current CI/test inventory, exact tests run and outcomes. No `PASS` without logs tied to exact tested SHA/image hash.
7. Public archive/privacy triage report with redacted data and precise scan coverage.
8. A C7 independent verdict against exact immutable review inputs. C7 reviewer must not repair the candidate or certify its own work.
9. Updated status/next-action snippets **as proposals only** until human approval.

## 8. Strict prohibitions

Until separate explicit authorization and gates are satisfied, Integraphy must not:

- enable autonomous writes, unattended ACT or repository mutation;
- write to ARGON-HEALTH, production systems or patient records;
- run commands on live host paths outside an independently validated sandbox;
- deploy, publish, migrate or connect to Legacy Firebase;
- change architecture, ADRs, ACRs, security policy or human decision records;
- modify `main`, delete/overwrite history or untracked work, commit, push, merge or open PRs;
- claim PR-09, SEC-03, SEC-04, C7-FFA-004 or Wave 4 is closed without exact evidence;
- promote any design/test specification to implemented/tested/approved/production-ready.

## 9. Exact stop condition

Stop and report `BLOCKED — EVIDENCE REQUIRED` if the local PR-09 branch, original audit logs, Docker runtime, canonical candidate files, identity boundary or independent reviewer cannot be established. A precise blocker report is a successful handover outcome; guessing or silently substituting a different baseline is not.
