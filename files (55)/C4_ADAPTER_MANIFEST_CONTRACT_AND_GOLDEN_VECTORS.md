# C4 — Proposed Adapter-Manifest Contract and Golden-Vector Format (for C6 EVAL-002)

**Status: PROPOSAL — SPECIFIED only. NOT IMPLEMENTED, NOT EXECUTED, NOT ACCEPTED.** No adapter, registry, vector set or checker exists. Nothing here authorizes Wave 4, a runtime, or any write to ARGON-HEALTH. Trust, origin tiers, secrets and re-review policy belong to **C2**; vector run-sets, mutants and records to **C6**; operator behaviour to **C5**; manifest storage to **C3**. Manifest format and compatibility rules (this document) are C4's lane.

## 0. Inputs and constraints (evidence-labelled)

| Input | Evidence |
|---|---|
| C4 `FCP-C4-ENG-003` on AI-OS `main` (`capabilities/future/C4/C4-FUTURE-ENGINEERING-CAPABILITY-PACKS.md`, blob `edfbbcdb9624993c73e4c77b56d9e1161f901ab8`, 33,930 B, SHA-256 `483cc77e…9138`): proposed manifest fields, rules 1–7, scenarios 1–8, EXP-003-A | VERIFIED (read) |
| C6 `FCP-C6-EVAL-002` / `T6-002-01…15`: oracle `(classification, gate_fired, executed, sandbox_state_hash)` read from sandbox state independently of the gate's log; mutants M-002a/b/c | VERIFIED. The T6-002 and T6-003 rows are byte-identical between the supplied candidate v3 (`213f25a5…020e`) and the accepted canonical v4 on `main` (`capabilities/future/C6/…`, blob `ca026d893a45f979f29f5fa819a9681a3cf0a9b0`, SHA-256 `dab7060e…c5cc`); the 51 differing lines are acceptance/status text only |
| Gate **G-9** (synthesis): second model backend + `C1-E3` executed before any adapter-sufficiency claim or adapters beyond a stub — NOT MET | VERIFIED |
| ENG-003 scope: tool and environment adapters only; **model adapters excluded** until defined | VERIFIED |
| PR #8 has `ProviderAdapter`/`MockProvider` (`runtime/core/providers.py`, blob `9b8b42c8…`) — a **model-axis** adapter with `get_capabilities`, `check_readiness`, `infer`. No tool/environment adapter, manifest, registry or digest-at-approval exists. | VERIFIED (static) |

Consequences: this contract is a **tool/environment** contract; the model axis is out of scope and a model-adapter manifest submitted to the tool registry must be refused (ENG-003 scenario 7). It cannot be used to claim adapter sufficiency (G-9). The existing `ProviderCapabilities` is precedent for capability reporting only.

## 1. Manifest contract (proposed)

Serialization: UTF-8, LF, JSON (or YAML parsed to JSON), keys sorted, no insertion of fields on read. `manifest_digest` = SHA-256 of the canonical JSON of the manifest **excluding** the `manifest_digest` field, using the same canonicalization style PR #8 uses for `TaskContract.digest()` (`json.dumps(sort_keys=True, separators=(",",":"), ensure_ascii=False)`, VERIFIED in `contracts.py`). Newline/hash-label convention (raw vs LF-normalized) is an **open owner question** (C5 item) and must be fixed before any digest is recorded.

| Field | Req. | Rule |
|---|---|---|
| `schema_version` | yes | Version of this contract schema; a reader refuses a newer major it does not support (T6-003-12 / ENG-001 sc. 11 analogue) |
| `adapter_id` | yes | Stable identifier; unique within the registry |
| `contract_version` | yes | Semver. Within a major: additive changes only (ENG-003 rule 3) |
| `adapter_kind` | yes | `tool` \| `environment`. **`model` is not a valid value**; presence of model-axis fields → refuse (sc. 7) |
| `registry_id` | yes | Registry the manifest was submitted to; a mismatch → refuse |
| `capabilities[]` | yes, ≥1 | See below |
| `manifest_digest` | yes | Computed as above; recorded **at approval time** (ENG-003 rule 7); any later change → C2 re-review path, never silent continuation |
| `deprecated_after` | no | Date; the window length is a BUSINESS DECISION (open) |

Each `capabilities[]` entry:

| Field | Req. | Rule |
|---|---|---|
| `name` | yes | Unique within the adapter; discovered from the manifest, never assumed (rule 1) |
| `input_schema`, `output_schema` | yes | JSON Schema; unknown *required* input fields refused on write; unknown output fields ignored on read (rule 5) |
| `effect_class` | yes | Pack-002 effect class (value set owned by C4 ENG-002; not redefined here) |
| `reversibility` | yes | Pack-002 value set |
| `mutation_scope` | yes | Declared targets the capability may touch (path roots, none, or "none-declared" which the gate treats as **unbounded → highest classification**) |
| `network_egress` | yes | `none` or a declared allowlist |
| `env_access` | yes | `none` or declared names; secrets resolved server-side by the adapter, never passed in (C2 direction; fails scenario "adapter handed an upstream credential") |
| `idempotent` | yes | Declared; a vector probe verifies it (scenario 4) |
| `timeout_seconds`, `cancel_supported` | yes | If omitted, the capability is treated as non-cancellable and non-idempotent (rule 6) |
| `error_taxonomy[]` | yes | Closed set of error codes the gate can match |
| `golden_vectors[]` | yes | References to vector records (§2); a capability without vectors is not eligible for approval (rule 4) |

**Preflight (proposed order; each failure refuses before any mutation):** (1) manifest parses and matches schema; (2) `adapter_kind` and `registry_id` valid; (3) recorded major version equals runtime major version; (4) every declared capability present at runtime; (5) `manifest_digest` equals the digest recorded at approval; (6) every capability has vectors and declarations for timeout/cancel/idempotency; (7) vector set hash equals the recorded vector-set hash.

## 2. Golden-vector record (proposed format)

One JSON object per vector, canonicalized as above; a vector **set** is a sorted list with a `vector_set_hash` (SHA-256 of the canonical set). The record separates what is **specified** from what was **observed**; the observed block is empty until a real run exists and must never be pre-filled.

```json
{
  "vector_id": "GV-ADP-<ordinal>",
  "contract_version": "<semver>",
  "capability": "<name | null for manifest-level vectors>",
  "kind": "positive | negative | adversarial | boundary | failure",
  "c6_test_ref": ["T6-002-12"],
  "source_refs": ["C4 ENG-003 sc.<n>", "C2 TV-003-<x>"],
  "preconditions": { "sandbox_profile": "<id>", "fixtures": ["<fixture-id>"], "registry_state": "<id>" },
  "input": { },
  "expected": {
    "classification": "ALLOW | REQUIRE HUMAN APPROVAL | BLOCK",
    "gate_fired": "<gate id or null>",
    "executed": false,
    "error_code": "<code from error_taxonomy or PREFLIGHT_*>",
    "sandbox_state_hash_after": "<hash of sandbox state read independently of the gate log>"
  },
  "control_vector_id": "<positive vector that must succeed under the same fixture>",
  "mutants_expected_to_fail": ["M-002a"],
  "status": "SPECIFIED",
  "observed": null
}
```

Format rules: (a) the oracle fields mirror C6's `(classification, gate_fired, executed, sandbox_state_hash)`; `classification` values follow the canonical C6 label set (three action labels; C2 uses four — divergence **D-03** is open, so the value set is a placeholder until C1/C2 harmonize it); (b) every negative or adversarial vector names a **control** vector that creates the effect, so a failure caused by an unrelated error cannot pass (the "false pass" guard C4 uses in PAM); (c) a vector is invalid if it cannot fail: it must list the mutant that disables the checked gate; (d) `sandbox_state_hash_after` is computed by the harness from the sandbox, never copied from adapter output; (e) `observed` is populated only by a real run and carries `run_id`, commit, image digest, log hash — none exists today; (f) no thresholds are set (`THRESHOLD NOT SET` stays).

## 3. Scenario-to-vector map (ENG-003 failure-injection scenarios → C6 T6-002)

| Vector (proposed) | ENG-003 scenario | Expected behaviour | C6 test / mutant |
|---|---|---|---|
| GV-ADP-001 | 1 output field type changed | refused at preflight or by the vector | T6-002-12 / M-002c |
| GV-ADP-002 | 2 declared capability absent at runtime | refused; no mutation | T6-002-12 |
| GV-ADP-003 | 3 major-version mismatch | refused at preflight | T6-002-12 |
| GV-ADP-004 | 4 adapter declares idempotent but duplicates effects | caught by a probe vector; capability treated non-idempotent | T6-002-12 (probe) |
| GV-ADP-005 | 5 unknown input/output fields | unknown required input refused on write; unknown output ignored | T6-002-12 |
| GV-ADP-006 | 6 manifest missing or malformed | refused | T6-002-12 |
| GV-ADP-007 | 7 model-adapter manifest to tool/environment registry | rejected | T6-002-12 |
| GV-ADP-008 | 8 manifest changes after approval | `manifest_digest` mismatch → C2 re-review, approval not inherited; **run once, shared with T6-002-02 (C2 TV-003-B)** | T6-002-02 / M-002a |

T6-002-01 (PLAN write via six routes), -03…-10, -13…-15 are consumed from C2/C5 and are not redefined by this contract; they can reference a capability's `mutation_scope`, `network_egress` and `env_access` declarations but their oracles remain C6's.

## 4. What this proposal does not establish

It does not show any adapter honours its manifest, that preflight is enforceable in PR #8 (no preflight, registry or manifest code exists there), that the declared fields are sufficient (G-9), that the value sets for `effect_class`/`reversibility`/classification are settled, or that C2 accepts `manifest_digest`-at-approval as the re-review trigger. EXP-003-A (two stub adapters, one deliberate breaking change) remains `TEST SPECIFIED`, not run.

## 5. Decisions and closure evidence (owners)

| # | Question | Owner | Closure evidence |
|---|---|---|---|
| AD-1 | Accept this field set / preflight order | C4 → C2 (trust fields), C6 (vectors) | Reviewed manifest schema file in a canonical location + EXP-003-A run log |
| AD-2 | Registry location and storage | C3 | Named registry path and schema |
| AD-3 | `effect_class`/`reversibility` value sets | C4 ENG-002 | Accepted Pack-002 value sets |
| AD-4 | Classification label set (3 vs 4) | C1 / C2 | Harmonized set recorded in a canonical file (closes D-03) |
| AD-5 | Hash convention (raw vs LF) | Human owner / C5 | Stated convention applied to manifests |
| AD-6 | Whether a second adapter or backend is planned (G-9 / ENG-003 "reject if one adapter, no change") | Human owner | Decision record |
