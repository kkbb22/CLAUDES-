# C4 — PR #8 Runtime Mutation-Surface Map (static analysis only)

**Baseline:** `kkbb22/ARGON-AI-OS` `main` = `1458a7f54f5d190ff84fce66cb2568960ff73559` (merge of PR #8, `708142c…`); VERIFIED by `git ls-remote` this session. **Method:** source reading from a read-only bare clone; no code, test or command from the repository was executed; no Docker. A finding here is source-observed behaviour, not an exploit demonstration. Labels: VERIFIED · SOURCE-ASSERTED · INFERRED · UNKNOWN · NOT RECOVERED. State separation: SPECIFIED ≠ IMPLEMENTED ≠ EXECUTED ≠ PASSED WITH EVIDENCE — nothing below is EXECUTED.

## 1. Module map

All paths `runtime/core/`; blob = git blob ID on `main`; lines from the same blob.

| Module (blob, lines) | Mutation capability (VERIFIED, static) | Trust boundary it claims | Observed controls | Observed gaps (attack ref in `C4_PLAN_ACT_ATTACK_MATRIX.csv`, 2026-11-04) |
|---|---|---|---|---|
| `orchestrator.py` (`a3ccb875`, 343 L) | Writes `.argon/tasks/<id>.json` (`_persist_task` L98–113) and ledger events on every state transition (`_transition` L115–128, `create_task` L149–156); drives sandbox writes in `execute_task` L201–336; invokes verification | State machine DRAFT→…→COMPLETED/FAILED; approval consumed before effects | Approval consumed before writes; only `write_text` writes performed; failure → FAILED | Non-`write_text` actions silently skipped (AP-09); no rollback on mid-loop failure (AP-10); persisted `state` trusted on load and load errors swallowed (AP-08); `ToolRegistry` constructed (L78) but never dispatched from here |
| `workspace.py` (`01afdbc1`, 292 L) | Writes under `<root>/sandbox` via tmp file then `unlink`+`rename` (L170–209); artifact index (L93–115); `cleanup_task` unlinks temporary artifacts (L257) | Path confinement, size and file-count caps | `validate_path` L118: rejects backslash, `..`, symlink in path chain; `check_capacity` L152 | Hardlinks, Unicode/case normalization, swap between check and write not shown handled (AP-15); non-atomic replace; no snapshot/rollback |
| `verifier.py` (`c186331a`, 214 L) | `subprocess.run` on the host (L129), cwd=sandbox, `shell=False`, env inherited, output captured | Allowlisted verification commands | Basename allowlist (`python`, `python.exe`, `pytest`, `git`) + chaining-character filter (L76–97); empty command list fails; timeout → failure | Arguments unconstrained → arbitrary code (AP-02); exit 0 = pass, `required_exit_code` unused, criteria only logged (AP-04); no containment, env, network, descendants, output cap (AP-05/06); can write `../.argon/*` (AP-07) |
| `tools.py` (`b59487f7`, 222 L) | `_handle_write_file` L158–167 writes directly; `_handle_run_command` L171–215 `subprocess.run` | Tool registry with permissions | `list_tools` L70 only; handlers have **no call site** in `runtime/` (grep) | Handlers bypass Workspace (no symlink/size checks; `allow_overwrite` ignored; `sandbox_root` overridable); `run_verification_command` registered `read_only=True`, `requires_approval=False`; stricter `SAFE_EXECUTABLE_ALLOWLIST` defined but unused (AP-14) — **latent** until a dispatcher exists |
| `policy.py` (`8a969a64`, 404 L) | Writes approval JSON (L312, L337) and nonce file (L196) under `.argon/approvals` | Contract policy, approval, replay prevention | `FORBIDDEN_PATTERNS`/`FORBIDDEN_COMMANDS` checks in `validate_contract` L201; digest/expiry/nonce/decision in `check_approval` L236; `requires_approval` L343 | Forbidden commands apply to `action.command` only, not `verification.commands` (AP-03); `requires_approval` ignores verification commands (**AP-01**); patterns case-sensitive (AP-15); nonce store fail-open on parse error, non-atomic, no lock (AP-11); approver is a caller string (AP-12); approval JSON unsigned (AP-08); `check_path_safety` L353 and `check_execution_preconditions` L378 not called by `execute_task` (grep) |
| `evidence.py` (`fc52c6ef`, 307 L) | Appends JSONL to `.argon/ledger` (`record` L137–163) | Hash-chained audit trail; secret redaction | `verify_chain` L182; `redact_secrets` L36 | In-memory counters, no lock; code states privileged rewrite is possible (AP-13); chain is a ledger, not an execution journal |
| `providers.py` (`9b8b42c8`, 340 L) | None to the filesystem or network by static reading: imports are `enum`, `json`, `time`, `abc`, `dataclasses`, `typing`; `MockProvider` is deterministic; `ProviderGateway(offline_mode=True)` is the default in `orchestrator.py` L77 and `cli.py` L37 | Model-axis adapter, cost budget | Offline mode restricts to mock providers (L289–290) | `infer` has no call site in the orchestrator execute path (grep) — providers cannot cause mutation today; this is a **model** adapter, outside the tool/environment adapter contract (see adapter document) |
| `contracts.py` (`1d4dece0`, 347 L) | None (data model) | Contract shape and `digest()` | Digest covers actions and `verification` (`to_dict` L214–252); path/size/timeouts validated in `ActionSpec.validate` | `validate()` mutates risk/approval/read_only (AP-18, hypothesis) |
| `runtime/argon_runtime.py` (`65d30f23`) | Writes `runtime/sandbox/**` and `runtime/.approval.json` | Standalone plan digest + typed `APPROVE <sha256>` | Digest binding, 10-minute expiry, approval unlinked before writes, `resolve()`+`is_relative_to` | No identity or nonce, no symlink rejection or size caps, partial writes on mid-loop error; second approval surface not reconciled with core policy (AP-17) |

## 2. Path from plan to effect (as implemented)

`create_task → validate_plan (validate_contract) → plan_task → [requires_approval?] → approve_task → execute_task (consume_approval → Workspace.write_file per write_text action → VerificationEngine.run_verification → ledger/state)`. Effects outside the sandbox directory are reachable only through the verification subprocess (host, unconfined). Control-plane files (`.argon/…`) are written by the runtime itself at every stage including PLAN.

## 3. Static-analysis conclusions and their limits

1. The "no write path in PLAN" property in the sources is about the tool registry; PR #8 has no per-state registry, so that oracle cannot be evaluated as written. Control-plane persistence is a by-design write at PLAN — whether it counts as a mutation for the oracle is an **owner question (C1/C2)**.
2. The strongest observed weakness is the composition **AP-01 + AP-02 + AP-07**: a read-only-classified contract with an allowed interpreter command can run without approval and, being unconfined, can touch the files that implement approval, replay-prevention and audit. This is a static trace (INFERRED composition of VERIFIED parts); it was not demonstrated.
3. Providers and `ToolRegistry` handlers contribute **no reachable** mutation today (no call sites) — their risk is latent and will change when a dispatcher or real provider is added.
4. Tests exist by name for several controls (see `C4_CONTROL_TO_CODE_TO_TEST_TRACEABILITY.md`), but no test log exists for the current head; test bodies were not read.

## 4. PR-09 reconciliation (reported changes vs exact source evidence)

**Exact evidence supplied: none.** The bundle `ARGON_COMPLETE_RECOVERY_2026-11-05.zip` contains no PR-09 export, no branch bundle, no diff, and no 2026-11-02 audit report (its own `00_README_AR.md` lists them as not recovered). The branch `fix/pr09-security-containment-followup` / commit `23fb2733…` is absent from the remote (9 refs; PR heads 1–8 only). Therefore every reported change stays:

| Reported item (2026-11-02, SOURCE-ASSERTED) | Evidence on `main` | Status |
|---|---|---|
| Host subprocess removed/rerouted | `subprocess.run` present in `verifier.py` L129 and `tools.py` L195 | NOT VERIFIED for the branch; **not present on `main`** |
| Docker isolation (network none, non-root, cap-drop, no-new-privileges, limits, workspace mount) | no Docker/seccomp/cap-drop text in `runtime/` or `tests/` | NOT VERIFIED; absent on `main` |
| Fail-closed verification | empty command list, non-zero exit, timeout fail; vacuous pass exists | NOT VERIFIED for the branch |
| Docker not runtime-verified; mutable image tag; image lacks Git/pytest; no custom seccomp | no image/Docker config on `main` | SOURCE-ASSERTED only |
| SEC-03 unauthenticated `local-operator` | observed (`policy.py`, `orchestrator.py` approver strings) | VERIFIED on `main` |
| SEC-04 rewritable SHA-256 ledger | admitted in `evidence.py` | VERIFIED on `main` |
| stdout/stderr memory buffering | `capture_output` in both subprocess sites | VERIFIED on `main` |
| Nonce synchronization race | non-atomic, unlocked nonce store | INFERRED (concurrency not executed) |

Evidence needed to close: the read-only export (bundle/diff/Docker files/logs/image digest/audit report) listed in `C4_PR09_FOLLOWUP_DIFF_AND_ASSURANCE_REVIEW.md` (2026-11-04); owner: human operator (local worktree `D:/aoswork-pr09-followup`); independent reviewer: C7.

## 5. Not authorized by this document

Running any test or command against the runtime, Docker execution, any repository write, Wave 4, machine writes to ARGON-HEALTH, any change to Legacy ARGON, autonomous execution.
