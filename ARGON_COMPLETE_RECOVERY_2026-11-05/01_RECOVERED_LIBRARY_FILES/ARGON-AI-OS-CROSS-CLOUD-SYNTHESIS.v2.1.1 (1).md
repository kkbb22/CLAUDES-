# ARGON AI-OS — CROSS-CLOUD SYNTHESIS v2.1.1 (CANDIDATE)

Phase D · surgical correction of v2 (v2.1, then v2.1.1) against C7-FFA-004 · author: C1 · scope: ARGON AI-OS (`system_scope: ai_engineering_os`, `repository_target: none`, `execution_target: deliverable_output`)

This document consolidates the six canonical Cloud Evolution artifacts (C1–C6) as pinned at repository commit `71a3fa6d1fb1eed0e694886263710d4020e10341`. It adds no research and no sources. It is architecture synthesis only: nothing here is implemented, approved, or verified beyond what the source artifacts themselves establish. The prior audit C7-FFA-003 (verdict `CLEAN WITH OPEN EXPERIMENTS`) audited the C1–C6 package; it is not a verdict on this document. The audit of the v2 candidate, C7-FFA-004 revision 3 (2026-10-18), issued **no** clean verdict. v2.1 applied that audit's correction register. This v2.1.1 candidate adds a narrow metadata and crosswalk correction pass requested after a later revision (revision 4) of the C7-FFA-004 audit; the text of revision 4 was not supplied to C1, so the corrections here follow the request and not that text `[ATT]`. v2.1.1 has **not** been re-audited.

**Revision lineage.** v2 (`ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.md`, 31,924 bytes, SHA-256 `eb679f0d88f82a7ba73724b01eeb660e6bad1ed8a75568b0a516382fab215109`) and v2.1 (`ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.1.md`, 55,345 bytes, SHA-256 `60cfae54f0a339d6c9251dda61ad79c473210ce5e1ce6a628b550b97fa1ffee1`) are each preserved unchanged and are not modified by this revision. v2.1.1 changes only the items named in the updated correction matrix, which is delivered as a separate document and is not part of this document's hashed bytes.

Labels used throughout: **[SRC]** supported by a cited source in the named Cloud artifact · **[PROP]** ARGON proposal · **[INF]** inference by this synthesis · **[EXP]** NEEDS EXPERIMENT · **[UNK]** UNKNOWN · **[HUMAN]** human decision · **[ATT]** author attestation, not independently verified · **[OBS]** observation made by the author at the stated time. **Experiment IDs** are namespaced by owning Cloud (`C1-E2`, `C3-E1`, `C5-E1` are different experiments); synthesis-originated items use `XC-`. The six proposed mutation surfaces are `MV-01`–`MV-06` (§11.1). Approval layers are `A0`–`A4` (§6). Gates are `G-0`–`G-12` (§15). Human decisions are `H-01`–`H-09` (§14).

---

## 1. Executive Synthesis

The six artifacts describe one coherent engineering model for an ARGON AI Engineering OS. A model-independent **Kernel** holds the invariants (identity, state, mode, approval boundary, escalation, checkpoint, execution boundary, verification handoff, evidence hooks). A thin per-model **Adapter** absorbs vendor and model differences. A **Runtime** carries out Kernel rules mechanically. Around that stack sit six functional planes: Orchestration/Kernel (C1), Security/Authorization (C2), Context/Knowledge (C3), Surgical Engineering (C4), Human Control (C5) and Evaluation/Learning (C6).

Three conclusions carry the most weight:

1. **The control model shows requirement-level convergence across Clouds, not demonstrated enforcement.** C1, C2, C4 and C5 each state, as a design requirement, that planning must have no mutation-capable path (C1 P2 and `C1-E2`, C2 RP-1, C4 Pattern F, C5 P1). That is adoption of a requirement. Whether any Runtime can enforce it is untested: C4 Pattern F is `NEEDS EXPERIMENT` and the full mutation test has never been run (§11, `C1-E2`). C1 and C2 define the same five test surfaces; C4 defines a different fifth surface; this document proposes a six-surface test taxonomy (`MV-01`–`MV-06`, §11.1) that is not yet accepted. The Clouds also separate approval into related but **non-identical** layers (C2: category, exact action, exact payload, cryptographic binding; C5 P4: display, prefix/category rule matching, an ARGON proposal, cryptographic binding). The common five-layer vocabulary in §6 is a C1 synthesis proposal. Exact-payload binding rests only on weak or emerging sources (C2 RP-13) and cryptographic binding is `NEEDS EXPERIMENT` (`C2-RP13`).
2. **Almost every mechanism is a design, not a fact.** All six artifacts record `status: DESIGNED` and `implementation_status: NOT_IMPLEMENTED`. Their recorded evidence statuses differ: C1 `PARTIAL`, C2 `DOCUMENTATION_ONLY`, C3 `mixed`, C4 `PARTIAL`, C5 `PARTIAL`, C6 `PARTIAL` (§18). Enforcement exists today only as policy, except where an artifact states otherwise. Wave 4 has not started.
3. **The open list is explicit and bounded.** Ten primary experiments (§13) and nine human decisions (§14) hold everything the sources leave unresolved. None blocks documentary synthesis; each blocks specific implementation steps, expressed as gates in §15.

### 1.1 Distinctions this document keeps separate

- Proposal vs. observed precedent.
- Design vs. implementation.
- Test specified vs. test executed.
- Human approval vs. UI display.
- Category/prefix rule matching vs. exact-action authorization.
- Proposed payload binding vs. cryptographic enforcement.
- Reversibility vs. authorization vs. rollback.
- An audit verdict vs. program readiness.
- Documentary completeness vs. empirical security proof.

### 1.2 Program-status separation

These seven conditions are independent. None implies another.

| # | Condition | State at this document |
|---|---|---|
| 1 | Candidate content corrected | Corrected per the C7-FFA-004 rev 3 register; items still OPEN or PARTIALLY FIXED are listed in the delivered correction matrix |
| 2 | Candidate ready for C7 re-audit | Submitted for re-audit; readiness is C7's determination, not this document's |
| 3 | Candidate accepted for repository intake | **NO.** Not in the pinned tree; no intake-manifest entry exists |
| 4 | ACTION-02 / DEP-07 (C6 Future Capability Packs) closed | **NO — PENDING.** The pinned tree holds future packs for C2–C5 only |
| 5 | Wave 4 design authorized | **NO.** Not authorized by this document or by any recorded decision |
| 6 | Runtime implementation authorized | **NO** |
| 7 | Runtime security empirically demonstrated | **NO.** No test has been executed |

## 2. Canonical Architecture

```
MODEL        reasoning only; no enforcement authority                         (C1)
  ↓
ADAPTER      per-model tool-call syntax, verbosity tuning, context-window use (C1)
  ↓
KERNEL       invariant authority + policy/control boundary, model-independent (C1; C2, C5, C6 constrain it)
  ↓
RUNTIME      tool registration per state, sandbox, checkpoints, trajectory    (C1, C2, C3, C6)
  ↓
TOOLS / ENVIRONMENT   filesystem, shell, git, network, MCP                    (C2)
```

| # | Plane | Primary artifact | Status of the plane (manifest `status`; `evidence_status`) |
|---|---|---|---|
| 1 | Orchestration / Kernel | C1 | `DESIGNED`; evidence `PARTIAL`; ten responsibilities specified |
| 2 | Security / Authorization | C2 | `DESIGNED`; evidence status `DOCUMENTATION_ONLY` |
| 3 | Context / Knowledge | C3 | `DESIGNED`; evidence `mixed`; pipeline is an ARGON proposal |
| 4 | Surgical Engineering | C4 | `DESIGNED`; evidence `PARTIAL`; deferred, no source code to act on |
| 5 | Human Control | C5 | `DESIGNED`; evidence `PARTIAL` |
| 6 | Evaluation / Learning | C6 | `DESIGNED`; evidence `PARTIAL`; every ARGON-side mechanism is `PROPOSAL` |

No seventh plane is created. C7 is an independent audit function, not a plane.

## 3. Kernel

Model-independent responsibilities, as specified by C1 and constrained by the other Clouds [SRC C1; PROP]:

| # | Responsibility | Cross-Cloud anchor |
|---|---|---|
| 1 | Cloud identity (fixed role and domain, independent of model) | C2 trust model; C5 routing transparency |
| 2 | Task/session state (`task_id`, `processing_state`: PLAN → REVIEW → APPROVAL → ACT → VERIFY) | C5 always-visible state |
| 3 | Mode enforcement: PLAN exposes no mutation-capable path | C1 P2, C2 RP-1, C4 F, C5 P1 (§6) |
| 4 | Tool availability governed by state and identity | C2 RP-2 tiered allow/deny/ask |
| 5 | Approval boundary: Git write, ADR/ACR change, destructive operation and live repository write require a human-granted approval record | C2 approval model; C5 P3, P4 |
| 6 | Escalation: contradictions are never auto-resolved and never settled by voting; they route to C1, then to the human | C3 P8b rejects majority-vote selection |
| 7 | Checkpoint semantics: a snapshot must exist before elevated-trust action | C1 P5; C4 D; C3 P9 |
| 8 | Execution boundary: ACT performs only the approved action | C2 RP-13 (binding level `[EXP]`); `[PROP]`, not enforceable until gates `G-2` and `G-4` (§15) |
| 9 | Verification handoff: no Cloud marks its own claim `VERIFIED` | C6 (evaluation independence); C7 |
| 10 | Audit/evidence hooks: every claim resolves to a source reference | C2 evidence store, RP-14; C6 trajectory |

Restated for self-containment: the **approval record** is a proposed object tying a task to an exact action, an approver, a scope and an expiry. C1 attributes its content-hash binding to earlier internal work (Wave 3.5 Convergence Patch §4) that is not one of the six canonical artifacts, so it is treated here as `[PROP]`, not as evidence; C1 also records that adding a checkpoint-reference field to it is an open schema gap. **A designed record is not an enforced authorization**: until the gates in §15 pass it is non-executable design material (§6). The **checkpoint** questions C1 answers (what is checkpointed, what authority changes, what evidence is needed) leave two items `[UNK]`: whether stale state may be resumed, and what invalidates a checkpoint (`XC-RESUME`, §13).

## 4. Adapter Layer

Everything model-specific stays behind the Adapter [SRC C1 Model Portability Boundary]:

- exact tool-call schema and format;
- instruction verbosity and structuring tuned per model;
- context-window size and the resulting compression needs.

Supporting evidence is qualitative. A shared interface was run against more than one model family in SWE-agent, and Aider's architect/editor mode mixes model providers across its two roles [SRC C1 P4]. Exact numeric gaps between models are third-party summaries and are not restated. C1 records that only one model/session existed at the time of its research, so **adapter sufficiency is untested** (`C1-E3`); this is a time-bound statement of C1's and is not re-verified here. Vendor-specific observations, such as Claude Code subagent behavior, remain vendor observations and are never promoted to Kernel rules. C2 RP-9 adds a boundary condition: enforcement is a property of the deployment, not of the agent or the model; whether ARGON can provide that deployment is `[UNK]`.

## 5. Runtime

No mechanism in this table is implemented.

| Mechanism | Source | Status |
|---|---|---|
| Tool registration per `processing_state` (implements Kernel item 3) | C1 P2, C2 RP-1, C5 P1 | `[PROP]`; enforcement **not demonstrated**; test `[EXP]` (`C1-E2`, surfaces `MV-01`–`MV-06`) |
| Sandbox independent of model judgment | C2 RP-3 | `ADOPT`; fail-open-on-missing-dependency flagged |
| Container isolation and structured trajectory recording | C2 RP-6, C6 P3 | trajectory `ADOPT`/`ADAPT`; isolation feasibility `[UNK]` |
| Checkpoint capture and rollback; atomic revertible commits | C1 P5, C4 D, C3 P9 | `ADAPT` (C1, C3), `ADOPT` (C4) |
| Bounded history collapse; durable evidence store is never compressed | C3 P5/P6, C6 P4 | `ADOPT` structure; window and thresholds `[UNK]` |
| Two-tier memory (structure only; no self-editing memory) | C3 P12 | `ADAPT` |
| Consecutive-auto-approval circuit breaker | C2 RP-4 | `ADOPT` as **partial** mitigation only |
| Sandbox-configuration injection treated as its own attack class | C2 RP-10 | `[EXP]` / `[UNK]` |
| Commit identity attribution | C2 RP-8 | `ADOPT`; plain git authorship is weak attribution |
| Auto-commit and dirty-commit defaults | C2 RP-7 | `REJECT` the defaults for ARGON |

## 6. Security / Authorization

**Approval layers — crosswalk and synthesis proposal.** C2 (Common Approval Position vocabulary) and C5 (P4) each separate what an approval does, but their layers are related, **not identical**. The five-layer vocabulary `A0`–`A4` below is a **C1 synthesis proposal** `[PROP]`: neither Cloud adopts it, and it is not an independently established taxonomy.

| Layer (proposal) | C2 term | C5 P4 term | Source status | What it does **not** establish |
|---|---|---|---|---|
| A0 Display | no corresponding C2 level | Display level — confirmed (the prompt shows tool name and exact parameters; Claude Code docs) | observed precedent | not authorization; not binding |
| A1 Category/prefix rule matching | Category Approval | Enforcement/matching level — partial (prefix/category-based) | observed precedent, partial (C2 RP-2/RP-5; C5 P4) | does not tie approval to one invocation; a different invocation matching the same rule could reuse it; segmentation bypass is an open question for C2 (C5 P4 test) |
| A2 Exact-action approval | Exact Action Approval (RP-13 exact-action authorization, `PROPOSAL`, weak-sourced) | ARGON exact-action model (`approved_plan_ref` content-hash binding), `PROPOSAL` | ARGON proposal; no vendor precedent at the enforcement level (C5 P4) | not cryptographic; not shown to resist substitution |
| A3 Exact-payload binding | Exact Payload Binding (RP-13 `artifactHash` concept) | not separated from A2: C5's content-hash binding spans A2 and A3 `[INF]`; exact-payload authorization is not demonstrated by the C5 source | `[PROP]`; the sub-mechanism with the clearest, still weak/emerging, source support (RP-13 question 6) | feasibility for non-deterministic LLM tool invocations is open (OQ-01 item 6) |
| A4 Cryptographic binding | Cryptographic Binding | Cryptographic binding, `NEEDS EXPERIMENT` / infrastructure decision | **`[EXP]`** (`C2-RP13`) | identity, freshness, expiry, revocation and replay resistance are neither designed nor verified |

Residual source wording: a row of C5's "Approval UX" table ("Is approval payload/action-bound? — Yes, per P4") is in tension with C5's own P4 correction. This document relies on the P4 correction, not on that row.

Showing the operator the parameters is **display** (A0). It is not payload binding and it is not authorization (C5 P4). A hash field is not a trust infrastructure.

**RP-13 split.** Of RP-13's six unresolved questions, five are cryptographic or infrastructure questions: key custody, identity binding, replay prevention, expiry, revocation. They are `[EXP]` (`C2-RP13`; OQ-01 items 1–5). The sixth, exact-payload binding (OQ-01 item 6), is the *proposal to bind approval to a payload* (A3): `[PROP]`, with its own open feasibility question. The proposal and the cryptographic experiment are distinct, and passing one does not close the other. RP-13 stays unresolved (`NEEDS EXPERIMENT`); no cryptographic protocol is specified or implied here.

**The approval record is non-executable design material.** Displaying an invocation, matching a category or command prefix, authorizing a particular action, binding approval to an exact payload, and cryptographically verifying identity, freshness, expiry, revocation and replay resistance are five different properties, and none follows from another. Until gate `G-2` (Plan/Act enforcement test passed), `G-4` (approval baseline recorded by the human, `H-04`) and, if a signed level is chosen, `G-5` (`C2-RP13`) are satisfied (§15), no Runtime may treat the record, or any hash or signature field in it, as authorization.

**Plan/Act control position.** `PLAN` has no mutation-capable path; `REVIEW` is read-only; `APPROVAL` is explicit human authorization where required; `ACT` exposes mutation tools only after authorization; `VERIFY` is independent. This is an **ARGON design proposal**: the adoption of a *design requirement*, not an implemented or empirically enforced property. Public vendor precedent is partial and limited (named-tool level; C1 P2, C4 Pattern F), so no source is cited as proving universal enforcement. The enforcement test (`C1-E2`) is `[EXP]`: specified, not executed, and no Runtime harness exists. A description of a read-only `PLAN` phase must not be read as evidence that mutation is blocked.

**Other positions retained from the sources.** Secrets never enter agent context (C2 RP-12, `ADOPT`). MCP trust distinguishes connect-time from runtime, with tool poisoning and confused-deputy risks named (C2 RP-11, `ADOPT`). Evidence carries trust tiers and self-attestation is not accepted (C2 RP-14, `ADOPT` as principle; specific mechanisms `[EXP]`). The circuit breaker (RP-4) does not prevent segmentation of a high-risk action into low-risk steps (C5 raises this as an open question for C2). Reversibility is not authorization: C5 P5 rejects it as a default, with a narrow carve-out left `[EXP]`. Reversibility (C5 P5), authorization (the approval record) and rollback (a checkpoint, C1 P5) are three distinct properties: C1 states that a checkpoint addresses recoverability after the fact and does not replace binding approval to the intended action. Sandbox-only autonomy that removes human authority is rejected (C5 P6). Whether third-party MCP is in ARGON's scope at all is `[HUMAN]` (C2).

**Human authority.** Approval, ADR/ACR status changes and any live repository write stay human-authorized; no Cloud approves its own ADR; the human is the sole governance authority [SRC C1 Kernel; C2 non-claims].

## 7. Context / Knowledge

**Pipeline** [PROP; C3 states provenance per stage]: `TASK → REPOSITORY SNAPSHOT → REPO MAP → RELEVANCE → CONTEXT PROJECTION → CONTEXT PACKET`.

| Stage | Provenance |
|---|---|
| Repository snapshot, context projection, context packet | ARGON-internal, proposed |
| Repo map | external-derived (Aider), adapted to a document graph for a docs-only repository (C3 P3 `ADOPT`; literal symbol graph P1 `ADAPT`/`REJECT` in literal form) |
| Relevance | external-derived (hierarchical localization, C3 P7 `ADOPT`) |

No per-tier token ceiling is defined anywhere in the package; any such number is `[UNK]`/`[EXP]`.

**Token economics: RETRIEVE → RANK → COMPRESS → VERIFY** [INF, assembled from C1, C3, C6]:

| Step | What the sources support | Status |
|---|---|---|
| RETRIEVE | hierarchical localization (C3 P7); document-reference graph (C3 P3); retrieve-then-rerank (C3 P14) | P7, P3 `ADOPT`; P14 `ADAPT`, payoff at this scale `[UNK]` |
| RANK | ranked graph (C3 P1); personalized ranking with adaptive budget (C3 P2) | P1 `ADAPT`; P2 `[UNK]` (audit-versus-efficiency tension) |
| COMPRESS | bounded history collapse and event-sourced condensation (C3 P5, P6); truncate versus summarize (C3 P13); observation compression (C6 P4) | structure `ADOPT`; window and thresholds `[UNK]/[EXP]`; counter-evidence below |
| VERIFY | grounding and evidence-integrity metrics (C6); provenance per stage (C3); freshness (C3 §4) | metrics `PROPOSAL`; freshness `[UNK]/[EXP]` |

**Counter-evidence kept in view:** a no-compression, minimal design (mini-swe-agent, C3 P15) works in the cited setting, so whether ARGON needs compression at all is `[UNK]`. Compression must never discard authority: claim, source, owner, status and snapshot reference survive; only prose is compressible (C6 P4 keeps the durable evidence store uncompressed). Caching strategy, information-gain gating and cost-aware escalation are not covered by any of the six artifacts and are not extended here. Per-role baseline sizing is experiment `C1-E1`. **Task isolation** has no external precedent in C3's sources and is `[EXP]` (`C3-E4`); **freshness triggers** are `[UNK]/[EXP]`.

## 8. Surgical Engineering

`Problem → Localization → Hypothesis → Exact Edit Location → Minimal Patch → Validation` [SRC C4; PROP for ARGON].

Failure taxonomy: **Localization Failure**, **Repair Failure**, **Validation Failure** (C4 §3, built from the phase boundaries; C6 reuses the same three axes in failure analysis).

| Pattern (C4) | Verdict |
|---|---|
| A hierarchical localization; B structured diff-style edits; C lint/syntax gate; D atomic revertible commits | `ADOPT` |
| E purpose-built, bounded tool interface over a raw shell (C4 classification `ADOPT`; C1 P3 classification `ADOPT (deferred — no code to apply it to yet)`) | `ADOPT` as a **principle** (bound what tools return; restricting capabilities a task does not need is a synthesis `[PROP]`); **application deferred**; **concrete interface form NOT SELECTED** (see H, `C4-EXP7`) |
| F Plan/Act | `NEEDS EXPERIMENT` (downgraded) |
| G granular category-scoped approval | `ADAPT` |
| H CodeAct unified action space vs. bounded ACI vs. minimal interface (candidate, counter-evidence and third position; none adopted) | **`NEEDS EXPERIMENT`** |

The **structured ACI versus bash-only minimal interface** question (C1 P3, C3 P15, C4 H) is unresolved and stays `NEEDS EXPERIMENT` (`C4-EXP7`, C4 Experiment 7; not executed). The principle is adopted; the concrete interface is not selected. Validation uses a dual gate: regression plus issue-specific reproduction (C4, C6 P6). C4's applicability note holds: ARGON-HEALTH has no source code, so this plane is deferred to a real implementation repository. Seven C4 experiments are defined and not executed (§13).

## 9. Human Control

`PLAN → REVIEW → APPROVAL → ACT → VERIFY` is always visibly staged [SRC C5; PROP]. C5 patterns: P1 runtime-enforced mode (`ADOPT`), P2 `ADAPT`, P3 `ADOPT`, P4 approval display versus binding (corrected, see §6), P5 `REJECT` as default, P6 `REJECT`, P7 `ADOPT`, P8 unattended-run behavior (`ADOPT` if unattended runs exist, otherwise `[UNK]`).

Required properties: visible state; visible scope; visible approval; stop; audit; resumption. Display is not authorization and is not payload binding. Conflicts are shown as claims with evidence and authority, never as a vote count. A success mark is reserved for `VERIFIED`; `PROPOSED` and `DESIGNED` never earn one. **Resumption after a stop is not designed** (checkpoint staleness and invalidation are `[UNK]`; `XC-RESUME`, §13). Whether ARGON will run unattended at all is open (C5 P8).

## 10. Evaluation / Learning

Rebuilt from C6 [SRC C6; every ARGON-side mechanism is `PROPOSAL`, `NOT_IMPLEMENTED`].

```
TASK → EXECUTION / TRAJECTORY → METRICS → FAILURE ANALYSIS → EVALUATION → REGRESSION → PROMOTION / REJECTION → FEEDBACK
```

| Step | Content |
|---|---|
| Benchmark | fixed, versioned task set; train / validation / held-out split; a fourth partition for tasks with no meaningful localization step |
| Trajectory | per-step response, thought, action, observation, state; older observations compress in-context past a recency window (size `[UNK]`); the durable evidence store never compresses |
| Metrics | every metric returns (score, reason), never a bare number; ten metrics, none with an invented threshold (below) |
| Failure analysis | three axes: localization; repair given correct localization; validation |
| Evaluation | training set is the source of proposed changes; validation set is used for selection only |
| Regression | fixed set of previously fixed failures, plus the dual gate (regression-equivalent and reproduction-equivalent) |
| Promotion / rejection | promote only if the training set improves, the validation set generalizes, and both regression gates pass; logged, versioned, reversible. C6 states that no promotion has occurred because no implementation exists (C6 §2, PROMOTION) `[SRC C6]`; this document does not independently verify system state |
| Feedback | rejection reasons return to failure analysis and to candidate generation |

**Metrics (C6):** correctness · grounding · evidence integrity · scope adherence · token efficiency · tool efficiency · test completeness · minimality · false completion (canary) · security violations. Each carries a definition, unit, measurement method, cost and expected failure signal.

**Benchmark validity discipline.** A benchmark score is not general agent quality. C6's validity limits: flawed tests and annotation errors (per C6, citing UTBoost, arXiv:2506.09289: a corrected test-case parser changed the annotation data for about 54.7% of SWE-bench Lite and 54.2% of SWE-bench Verified instances); patch correctness is not the same as test pass; contamination; version drift (SWE-bench, Lite and Verified are not interchangeable); held-out validity decays with reuse. Any score cited must name its benchmark, version, model and metric.

**Unified failure model** [PROP; anchors in the sources, recovery steps are proposals]. Each class follows detect → classify → recover or escalate → record, and records go to the evidence store and trajectory.

| Failure | Detect (source anchor) | Recover / escalate | Anchor |
|---|---|---|---|
| Localization | wrong location found (C4 §3, C6 axis 1) | re-localize with different narrowing; do not generate more patches at the wrong place | C4, C6 |
| Repair | correct location, wrong fix (C6 axis 2) | regenerate from the same hypothesis | C4, C6 |
| Validation | gate fails (C4/C6 dual gate) | reject the patch; log | C4, C6 |
| False completion | claim marked done without evidence; canary metric | revert to `INCOMPLETE`; escalate to C1 | C1 Kernel, C6 |
| Evidence | unresolvable source or self-attestation (C2 RP-14) | downgrade the claim; require resolvable evidence | C2, C6 |
| Authorization | action outside approved scope or level (C2) | block and escalate to the human | C2, C5 |
| Context | stale, leaked or over-compressed context (C3) | refresh the snapshot; rebuild context | C3 (mechanism `[EXP]`) |
| Routing | wrong Cloud selected | escalate to C1 | **no anchor in the six canonical artifacts [UNK]** |

C6 leaves open: optimizer choice, trajectory step granularity, compression window size, held-out reuse limit, judge-call cost for non-exact-match correctness, and whether the existing evidence vocabulary captures the localization/repair/validation split or needs an explicit localization-correct field. C6 also flags that its dual gate may overlap an unattached C3 chain-resolution/content-review artifact; the overlap is `[UNK]`.

## 11. Cross-Cloud Consistency

| # | Item | Clouds | Finding | Status |
|---|---|---|---|---|
| a | Plan/Act mutation test | C1, C2, C4 (test owners per `STATUS.md`); C5 P1 supplies the related control principle, not a test | C1 and C2 list the same five surfaces (direct write tool, shell write, interpreter write, wrapper/composite write, indirect write via a nested tool call). C4 Pattern F lists (a) direct write, (b) shell, (c) interpreter, (d) a nominally read-only tool whose arguments cause a side effect, (e) a permitted tool wrapping a write-capable subprocess; `STATUS.md` and OQ-03 shorthand (d) as C4's "fifth vector", although it is item (d) in C4's own list. Both families describe real attack surfaces. **Proposed unified test taxonomy** `[PROP]`: six surfaces `MV-01`–`MV-06` with stable IDs and a per-source crosswalk (§11.1). It is a proposal, not an accepted policy and not an executed suite. Classifications also differ (C2 RP-1 and C5 P1 `ADOPT` as a principle, C4 F `NEEDS EXPERIMENT`); position: requirement adopted at design level, implementation `[EXP]` | divergence **OPEN**: OQ-03 stays open until the taxonomy is formally accepted (`H-09`); the repository's five-vector plan (OQ-02, ACTION-05) is unchanged |
| b | Approval layers | C2, C5 | related but **not identical** layers: C2 separates category, exact action, exact payload and cryptographic binding; C5 P4 separates display, prefix/category rule matching, ARGON `approved_plan_ref` (proposal) and cryptographic binding. The five-layer vocabulary in §6 is a C1 synthesis proposal; neither Cloud independently establishes exact-payload or cryptographic enforcement | related, non-identical; common vocabulary `[PROP]` |
| c | Failure axes | C4, C6 | C6 failure analysis reuses C4's three axes | consistent |
| d | Compression | C3, C6 | both adopt bounded compression with the window `[UNK]`; both keep the durable evidence store uncompressed; C3 P15 holds counter-evidence | consistent, open |
| e | Interface shape | C1, C3, C4 | structured ACI versus minimal: all three record the tension | open (`C4-EXP7`) |
| f | Delegation depth | C1 only | no other Cloud addresses it; vendor evidence is contested | single-Cloud `[PROP]`, E1b |
| g | Benchmark discipline | C1, C4, C6 | source-verified, third-party and conflicting figures kept apart | consistent |
| h | Metadata vocabulary | C1–C6 | identical `system_scope` / `repository_target` / `execution_target` triple | confirmed by C7 |
| i | Self-containment | C1–C6 | internal earlier-wave dependencies are labeled as such, not as external evidence | acceptable |

### 11.1 Proposed mutation-surface taxonomy (crosswalk)

`[PROP]` — a unified test taxonomy proposed by this synthesis. Each surface has a stable ID independent of its position in any source's list. The set is not accepted policy and no test in it has been executed.

| ID | Proposed surface | `C1-E2` (C1) | C2 RP-1 widened scope | C4 Pattern F | Note |
|---|---|---|---|---|---|
| MV-01 | Direct write-capable tool | (1) | (1) | (a) | consistent across sources |
| MV-02 | Shell command that writes | (2) | (2) | (b) | consistent |
| MV-03 | Interpreter execution that writes | (3) | (3) | (c) | consistent |
| MV-04 | Wrapper or composite tool that reaches a write-capable subprocess | (4) wrapper/composite commands not themselves named as a write operation | (4) wrapper/composite write (RP-5 blind spot) | (e) a permitted tool wrapping a write-capable subprocess | C4 (e) may also overlap MV-05; the overlap is unresolved `[INF]` |
| MV-05 | Indirect mutation through a nested tool call from an outwardly read-only tool | (5), defined by C1 as distinct from (4) | (5) | no distinct item | no explicit C4 counterpart |
| MV-06 | Side effect caused by arguments supplied to an ostensibly read-only tool | not listed | not listed | (d); C4's prose list calls it "indirect file mutation" (a test tool accepting a fixture path outside the test directory) | the surface `STATUS.md` and OQ-03 call C4's "fifth vector"; no explicit C1/C2 counterpart |

C4's prose list (shell, interpreter, indirect file mutation, wrapper) and its numbered test list (a)–(e) are ordered differently, which is why the ordinal "fifth" is not used here. OQ-03 and OQ-02 remain open. Decision needed: `H-09` (accept six surfaces as the basis for `C1-E2` and ACTION-05, or keep the five-vector plan with C4's surface as a recorded supplement). The tests stay unexecuted until a Runtime harness exists.

**C7 minor items folded in.** C7 records that C1 dropped a "+10.7 percentage points (Lite)" figure as unconfirmable, although the figure appears in the primary source's prose; the paper's own table shows 11.00% versus 18.00% (7.0 points), a tension the paper does not reconcile (OQ-04). Net effect per C7: a true, cautious claim was dropped, not a false one asserted. **Status here:** the discrepancy is recorded because it is a documented source tension. Neither figure is adopted as an ARGON performance claim or used as evidence for any ARGON design decision, and no benchmark figure in this document is an ARGON result.

## 12. Adopt / Adapt / Reject

| Item | Source | Verdict |
|---|---|---|
| Context isolation per delegated Cloud | C1 P1 | `ADOPT` (isolation); delegation depth `ARGON ORIGINAL` / `NEEDS EXPERIMENT` |
| PLAN has no mutation path | C1, C2, C4, C5 | `ADOPT` as a design requirement only; enforcement not demonstrated; implementation `NEEDS EXPERIMENT` (`C1-E2`; C4 Pattern F is `NEEDS EXPERIMENT`) |
| Bounded, purpose-built interface over raw shell — the **principle** | C1 P3, C4 E | `ADOPT` (principle); application deferred; concrete form NOT SELECTED (`C4-EXP7`) |
| CodeAct vs bounded ACI vs minimal — the concrete interface form | C4 H | `NEEDS EXPERIMENT` (`C4-EXP7`) |
| Interface/role portability across models | C1 P4 | `ADOPT` (qualitative) |
| Checkpoint before elevated trust | C1 P5, C4 D, C3 P9 | `ADAPT` / `ADOPT` |
| Feedback-rich evaluation | C1 P6, C6 P1 | `ADOPT` (shape); optimizer `UNKNOWN` |
| Train / validation / held-out discipline | C6 P2 | `ADOPT` (pattern) |
| Structured trajectory | C6 P3, C2 RP-6 | `ADAPT` / `ADOPT` |
| Dual-gate validation | C4, C6 P6 | `ADOPT` / `ADAPT` |
| Category/prefix approval (layer A1) | C2 | `ADOPT` (external precedent partial; does not authorize an exact action) |
| Exact-action and exact-payload binding (layers A2, A3) | C2 RP-13, C5 P4 | `PROPOSAL`; feasibility open (OQ-01 item 6) |
| Cryptographic binding and key custody (layer A4) | C2 RP-13 | `NEEDS EXPERIMENT` (`C2-RP13`) |
| Six-surface mutation-test taxonomy (`MV-01`–`MV-06`) | `C1-E2`, C2 RP-1, C4 F | `PROPOSAL` (this synthesis); OQ-03 open |
| Circuit breaker | C2 RP-4 | `ADOPT` (partial mitigation only) |
| Sandbox independent of model | C2 RP-3 | `ADOPT` |
| Secrets out of context | C2 RP-12 | `ADOPT` |
| Auto-commit / dirty-commit defaults | C2 RP-7 | `REJECT` |
| Majority-vote final selection | C3 P8b | `REJECT` |
| Reversibility as a substitute for authorization | C5 P5 | `REJECT` (narrow carve-out `NEEDS EXPERIMENT`) |
| Sandbox-only autonomy overriding human authority | C5 P6 | `REJECT` |
| Hierarchical localization | C3 P7, C4 A | `ADOPT` |
| Document-reference graph | C3 P3 | `ADOPT` |
| Personalized ranking / adaptive budget | C3 P2 | `UNKNOWN` |
| Task isolation mechanism; freshness triggers | C3 | `NEEDS EXPERIMENT` |
| Failure taxonomy (3 axes) | C4 §3, C6 P5 | `ADOPT` |
| Benchmark-score-as-quality | C6 | `REJECT` |

## 13. Open Experiments

Primary register. Success measurements restate the source artifacts' own specifications and invent no thresholds. **No experiment below has been executed.** IDs are namespaced by owning Cloud because several Clouds number their own experiments `E1`, `E2` and so on; `XC-` marks an item originated by this synthesis. Earlier v2 identifiers: `E1`→`C1-E1`, `E1b`→`C1-E1b`, `E2`→`C1-E2`, `E3`→`C1-E3`, `E4`→`C1-E4`, `E5`→`C1-E5`, `RP13`→`C2-RP13`, `C4-INTERFACE`→`C4-EXP7`, `RESUME`→`XC-RESUME`, `ISOLATION-ENFORCEMENT`→`C3-E4`.

| experiment_id | question | owner | affected_component | why_unknown | required_environment | success_measurement | risk_if_wrong | gate (§15) | execution_status |
|---|---|---|---|---|---|---|---|---|---|
| C1-E1 | Does per-role context baseline sizing cut tokens without changing outcomes? | C1 (C3 token engine) | Context compiler, Kernel baselines | never tested; per-tier ceilings undefined | at least 10 representative tasks per role (C1 spec) | token count down with unchanged `claim_status` outcome on every task (C1 promotion condition) | silent loss of needed context | `G-3`: blocks the Wave 4 context compiler | NOT EXECUTED |
| C1-E1b | Does ARGON's bounded delegation depth match or beat deeper delegation? | C1 | Kernel delegation rule | vendor evidence is contested and version-dependent; ARGON proposal only | tasks that plausibly need a second delegation level | outcome quality (`claim_status` distribution) and token cost; depth-1 matches or exceeds depth-2 at lower or equal cost | needless restriction or runaway delegation | `G-7`: blocks fixing the Kernel delegation rule | NOT EXECUTED |
| C1-E2 | Does PLAN block mutation across all proposed surfaces `MV-01`–`MV-06`? (C1's own specification covers five surfaces; extension to six depends on `H-09`) | C1, C2, C4 | Runtime tool registration | sources document named-tool absence only; other paths untested; taxonomy not accepted (OQ-03) | implementation environment with every surface available | zero successful mutations on every surface, tested independently (C1 promotion condition); C4: all five of its listed attempts must fail structurally, and passing only (a) earns at most PARTIAL | false security if only the named tool is closed | `G-2`: blocks any APPROVAL/ACT flow and any Runtime reliance on Plan/Act enforcement | NOT EXECUTED |
| C1-E3 | Is a thin calling-convention adapter enough across two or more model backends? | C1 | Adapter boundary | C1 records only one model/session | a second model backend | zero Kernel carve-outs across providers | Kernel becomes model-coupled | `G-9`: blocks any adapter-sufficiency claim | NOT EXECUTED |
| C1-E4 | Does a checkpoint reference recorded on a write-capable approval record suffice to diagnose and either roll back or resume a deliberately interrupted ACT, without re-deriving state? | C1 | Checkpoint / approval record | never run; the reference field is an open schema gap (C1) | implementation environment, deliberately interrupted tasks | recovery succeeds from the reference alone across all interrupted cases tested (C1); failure signal: recovery needs information absent from the reference | lost progress or inconsistent state | `G-8` (with `XC-RESUME`): blocks resumable ACT flows | NOT EXECUTED |
| C1-E5 | Do structured verification records cut correction cycles versus bare pass/fail? | C1, C6 | Evaluation / verification | never tested | planted-defect artifacts verified both ways | fewer correction cycles with structured detail, replicated across the set (C1) | extra structure that does not pay | no gate; depends on an evaluation harness existing | NOT EXECUTED |
| C2-RP13 | Can cryptographic action binding be made safe? | C2 | Approval / security | six questions undesigned: key custody, identity binding, replay prevention, expiry, revocation, exact-payload binding | implementation environment with signing infrastructure | all six dimensions independently verified | false assurance from a broken scheme | `G-5`: only if `H-03` selects cryptographic binding; blocks any live write relying on it | NOT DESIGNED; NOT EXECUTED |
| C4-EXP7 | CodeAct vs bounded ACI vs minimal interface (C4 Pattern H; C4 Experiment 7) | C4 (C1, C3) | Runtime, surgical tooling | vendor evidence conflicts (performance vs simplicity) | a real implementation repository | C4 Experiment 7: one interface style shows a statistically significant lower rate of confidently wrong localizations; no difference is the failure threshold; the result decides Pattern E, H, both or neither | costly early commitment | `G-6`: blocks surgical tooling and any concrete interface commitment | NOT EXECUTED |
| XC-RESUME | What are the semantics of resuming after a stop: may stale state be resumed, what invalidates a checkpoint, must approval be re-obtained after a state change? | C1, C5 (synthesis item; OQ-06) | Human control, runtime | C1: stale-state resumption and checkpoint invalidation are undesigned; C1's no-survival-of-approval position is untested | implementation environment | **no source-specified acceptance criteria.** Proposed structure `[PROP]`: (i) invalidation rules exist as a written design before any test; (ii) a resume attempt on stale state is rejected or forces re-approval; (iii) every outcome is recorded. No numeric thresholds | silent state loss or continuation on stale state | `G-8`: blocks resumable ACT flows | NOT DESIGNED; NOT EXECUTED |
| C3-E4 | Does task-context isolation hold under a real mechanism? | C3 (C1) | Runtime | no external precedent; no mechanism exists | multi-task implementation environment | zero cross-task leakage; trial count N is `[UNK]` in C3 §7 | silent leakage | `G-12`: blocks any multi-task runtime | NOT EXECUTED |

**Source-label note on `E1a` (unresolved).** `STATUS.md` (C1 row of the Cloud table) lists the specified tests as "E1a, E1b, E2, E3". C1's research defines E1, E1b, E2, E3, E4 and E5; it defines no experiment named `E1a`. Its pattern table labels the isolated-subagent baseline-sizing pattern "1a" and gives its experiment as "E1" (and pattern "1b", delegation depth, as "E1b"). No source states that `E1a` and `E1` are the same experiment, so this document does **not** equate them: `C1-E1` means the experiment C1 defines as E1, and whether the `STATUS.md` label `E1a` is a stale alias for it is `[UNK]` pending the repository owner or the source author. `STATUS.md` also omits C1's E4 and E5 from that list; that omission is likewise not interpreted here.

**How `C1-E4` differs from `XC-RESUME`.** `C1-E4` tests whether a checkpoint reference carried on the approval record is *sufficient information* to diagnose and roll back or resume an interrupted ACT; its acceptance criterion is recovery from the reference alone (C1 specification). `XC-RESUME` concerns *policy and semantics*: whether resumption is permitted at all after a stop, what invalidates a checkpoint, and whether approval survives a state change; no source specifies acceptance criteria for it. `[INF]` The rollback/diagnosis branch of `C1-E4` can be evaluated without resumption semantics, but its resume branch depends on `XC-RESUME`'s definitions.

Secondary register (owner Cloud and pointer to the full specification):

| Group | Items | Owner | Status |
|---|---|---|---|
| C4 Experiments 1–7 (`C4-EXP1`–`C4-EXP7`; `C4-EXP7` is in the primary register) | localization accuracy; patch minimality; regression pass rate; reproduction pass rate; unrelated-file touches; repair success after correct localization; false-positive localization | C4 | defined, **not executed** |
| C3 experiments | `C3-E1` retrieval relevance (promotion threshold `[UNK]`); `C3-E2` token savings (percentage `[UNK]`); `C3-E4` isolation-trial count (primary register); further items in C3 §7 | C3 | thresholds `[UNK]` |
| C5 experiments (`C5-E1`–`C5-E8`) | approval comprehension; accidental approval; action mismatch (tests the `approved_plan_ref` binding); stop latency; recovery success; routing transparency; evidence comprehension; UI/runtime authority mismatch | C5 | defined, **not executed** |
| C6 open items | optimizer choice; trajectory step granularity; compression window; held-out reuse limit; judge-call cost; evidence-vocabulary fit; dual-gate overlap | C6 | `[UNK]` |
| C2 open items | segmentation bypass of the circuit breaker; sandbox-configuration injection (RP-10); deployment-feasibility of enforcement (RP-9) and container isolation (RP-6) | C2 | `[EXP]` / `[UNK]` |
| C5 open items | whether unattended runs exist (P8); narrow reversibility carve-out (P5) | C5 | `[UNK]` / `[EXP]` |

## 14. Human Decisions

Only decisions that the final sources themselves leave open, plus one raised by this synthesis (`H-09`). **None of them is made by this document.** Where a proposal is named, it is a proposal.

| ID | Decision | Source | Proposal on the table (not a decision) |
|---|---|---|---|
| H-01 | Delegation depth value | C1 (`C1-E1b`) | C1's depth-1 proposal; unvalidated |
| H-02 | Interface direction: structured ACI, CodeAct or minimal | C4 H; C3 P15 counter-evidence | none selected; the principle in §8 is adopted, the concrete form is open (`C4-EXP7`) |
| H-03 | Whether ARGON invests in cryptographic-binding rigor at all, versus a simpler approval-record model | C2 RP-13 | none |
| H-04 | Which approval layer ARGON adopts as its baseline, and narrow single-use vs broad persisted scope (C2 states it does not choose) | C2 approval authority model | this synthesis proposes layers A1 and A2 as a candidate baseline `[PROP]`; **not a recorded decision**, and until recorded the approval record remains design material only |
| H-05 | Whether third-party MCP is in ARGON's scope | C2 | none |
| H-06 | Whether to deepen source coverage. C1 names not studied: OpenHands, SWE-ReX, Roo Code, Goose, OpenAI Agents SDK, PydanticAI, smolagents, LangGraph. C6 names not studied: Terminal-Bench, OpenHands Benchmarks, SWE-ReX, LiteLLM spend tracking, LangGraph durability | C1, C6 | none |
| H-07 | Whether unattended runs exist at all | C5 P8 | none |
| H-08 | Whether infrastructure for deployment-level enforcement is feasible | C2 RP-9 (`[HUMAN]`/`[UNK]`) | none |
| H-09 | Whether to accept the six-surface mutation taxonomy (`MV-01`–`MV-06`) as the basis for `C1-E2` and ACTION-05, or keep the five-vector plan with C4's surface as a recorded supplement | OQ-03; this synthesis | the six-surface set, `[PROP]`; OQ-03 stays open until accepted |

Not carried: freshness triggers and any snapshot-staleness interval remain `[UNK]/[EXP]` in C3 §4. No specific interval is recorded here as a decision. (A text search of the pinned C1–C6 research documents, `C7-FFA-003.md`, the planning files, `docs/CURRENT-STATE.md` and `STATUS.md` for "15-minute" and "15 min" returned no match `[OBS 2026-10-19]`.)

## 15. Wave 4 Preconditions (Gates)

Each gate is a genuine pass/fail condition on a named component. All are **NOT MET** at this document. Documentary design work may proceed under a human design authorization (`G-0`); a gate restricts building or *relying on* the named component. Passing a gate is a repository and audit matter, not something this document asserts.

| Gate | Condition to pass | Blocks | Status |
|---|---|---|---|
| G-0 | A human governance decision authorizing Wave 4 design, and separately any implementation | everything in §16; this document grants neither | NOT MET |
| G-1 | Mutation taxonomy accepted or an alternative recorded (`H-09`, closing OQ-03) | specifying `C1-E2` as a test plan | NOT MET |
| G-2 | `C1-E2` specified over the accepted taxonomy, a runnable harness exists, and it passes: zero successful mutations on every surface, tested independently | any APPROVAL/ACT flow; any Runtime reliance on Plan/Act enforcement | NOT MET |
| G-3 | `C1-E1` executed with its promotion condition met | building the Wave 4 context compiler (this synthesis's term for the implementation of the C3 pipeline; no C3 source uses it `[INF]`) | NOT MET |
| G-4 | Human records the approval baseline (`H-04`) | finalizing the approval-record schema; building approval infrastructure | NOT MET |
| G-5 | `C2-RP13` complete: all six dimensions independently verified | any live write relying on cryptographic binding; applies only if `H-03` selects it | NOT MET |
| G-6 | `H-02` recorded and `C4-EXP7` executed | surgical tooling; any full ACI or CodeAct layer | NOT MET |
| G-7 | `C1-E1b` executed | fixing the Kernel delegation rule; any delegation deeper than one level | NOT MET |
| G-8 | `C1-E4` executed and `XC-RESUME` semantics designed and tested | resumable ACT flows; session-resumption logic | NOT MET |
| G-9 | A second model backend exists and `C1-E3` executed | any adapter-sufficiency claim; adapters beyond a stub | NOT MET |
| G-10 | Evidence and trajectory schemas fixed (C2 evidence store, C6 trajectory); the approval record formalized as a canonical schema *document* | evaluation code that depends on them | NOT MET |
| G-11 | A real implementation environment exists (the research sprint produced none) | every test above | NOT MET |
| G-12 | `C3-E4` executed | any multi-task runtime | NOT MET |

## 16. Recommended Wave 4 Design (ARGON PROPOSAL only)

An order derived from what the sources support and from the gates in §15. No item is approved, authorized or verified; every item is subject to `G-0`. Ordering changes from v2: the `C1-E1` gate now precedes the context compiler, and the Plan/Act harness now precedes any use of the approval record.

1. **Kernel validator:** the ten responsibilities as a checkable rule set; pure logic, no tools (`[PROP]`).
2. **Evidence and trajectory store:** schema first, per C2's trust tiers and C6's step schema (`[PROP]`, `ADAPT`); gate `G-10`.
3. **Gate `G-3` (`C1-E1`), then context compiler, document-graph variant:** matches a docs-only repository (C3 P3 `ADOPT`; thresholds `[UNK]`).
4. **Plan/Act enforcement test harness (`C1-E2`):** built before further Runtime; gates `G-1`, `G-2`, `G-11`.
5. **Approval record as a schema document only:** levels per `H-04` once recorded (candidate A1 and A2, `[PROP]`); cryptographic binding deferred (`[EXP]`). It is non-executable design material and is not wired to any ACT flow before `G-2` and `G-4`.
6. **Protected ACT flow:** listed only to show ordering. It is **not authorized** by this document; it requires `G-2`, `G-4`, `G-8` where resumable, `G-5` where signed, and separate human authorization for any live write or high-risk action.
7. **Evaluation harness skeleton:** benchmark fixtures, (score, reason) metric functions, regression set with the dual gate; **no automatic promotion** (C6 promotion is `PROPOSAL`).
8. **Surgical-engineering tooling:** only after `H-02` and `C4-EXP7` (`G-6`).

## 17. What Must NOT Be Built Yet

- Cryptographic approval-binding infrastructure (RP-13).
- Any approval-record enforcement, or any ACT flow that relies on an approval record, before `G-2` and `G-4`.
- Any live repository write, autonomous high-risk action or production execution.
- Any per-tier token ceiling or promotion threshold without an experiment behind it.
- Automatic prompt, router or Kernel promotion; and optimizing against the same set used to declare success.
- Any concrete interface commitment (full ACI layer, CodeAct layer or minimal interface) before `H-02` and `C4-EXP7`.
- Delegation deeper than one level before `C1-E1b`.
- Session-resumption logic (undesigned) and unattended-run machinery (unresolved).
- Third-party MCP integration before `H-05`.
- Cross-model adapters beyond a stub.
- Any ARGON-HEALTH or Legacy ARGON change, any ADR or ACR, any clinical code. This program does not touch them.

## 18. Provenance / Evidence Status

**Source baseline.** Repository `kkbb22/ARGON-AI-OS`, commit `71a3fa6d1fb1eed0e694886263710d4020e10341` (the tree holds 79 files). Paths read at that commit: the six `clouds/C1`–`C6` research documents and manifests, `assurance/audits/C7-FFA-003.md`, `planning/NEXT-ACTIONS.md`, `planning/DEPENDENCY-REGISTER.md`, `planning/OPEN-QUESTIONS.md`, `docs/CURRENT-STATE.md`, `STATUS.md`, `README.md`, `evidence/MANIFEST.json`. `[OBS]` author-observed by C1 on 2026-10-19 (time of day not recorded) with a local `git ls-remote`: `refs/heads/main` pointed at this same commit. This is not a C7 verification and no independent evidence is attached; C7-FFA-004 revision 3 records the current `main` tip as not established by that audit. Conclusions stay pinned to the commit, not to `main`. No file in the tree is a cross-cloud synthesis candidate.

**Hash bases — kept separate; do not conflate.**

- *Recorded LF-normalized hash:* each Cloud manifest's `report_sha256` / `report_sha256_value`, repeated in `STATUS.md` (column "LF-Normalized SHA-256"), in `evidence/MANIFEST.json` (`lf_normalized_sha256`) and in `C7-FFA-003.md` (a column that file labels "Actual SHA-256"; the values equal the normalized hashes).
- *Historical raw-intake hash:* `raw_sha256` in `evidence/MANIFEST.json`, the hash of the files as originally uploaded. It differs from the normalized value; `docs/CURRENT-STATE.md` §1 item 5 attributes the variance to CRLF line endings.
- *Fresh computation by C1 `[ATT]`:* SHA-256 of the six canonical `.md` files, taken (a) from a git checkout of the pinned commit and (b) from `raw.githubusercontent.com` downloads at that commit, using `sha256sum`; both agree. The pinned files contain no carriage-return bytes, so their raw SHA-256 equals the recorded LF-normalized value. This is **C1's own computation**, not a C7 verification; the reproducible method is: check out the pinned commit, run `sha256sum` on each file, and compare with the manifest `report_sha256`. Converting each pinned file to CRLF (appending a carriage return to every line) yields the recorded raw-intake hash for all six; that shows consistency with the CRLF explanation in `docs/CURRENT-STATE.md` only. **The original upload bytes were not supplied and were not recovered**, so the historical raw-intake hashes are not independently verified.

| Input | artifact_id | Recorded LF-normalized SHA-256 (manifest `report_sha256`) | SHA-256 of pinned file, C1 computation `[ATT]` | Equals recorded value | Recorded raw-intake SHA-256 (`evidence/MANIFEST.json`; original bytes not recovered) |
|---|---|---|---|---|---|
| C1 | c1-cloud-evolution-harness-v4-final | 24e8cdb1cb8a088f146ff97265a484a329544b6a13d3bdfafea00de9f5dc688f | 24e8cdb1cb8a088f146ff97265a484a329544b6a13d3bdfafea00de9f5dc688f | yes | 36f91407949a4f501ca28b8a70ae613733d5412dae5ec71dade36edaef1431d9 |
| C2 | C2-CLOUD-SECURITY-ADAPTER-RESEARCH | c6e95c268aa6b065737933cbeff10761939d8f310cb11db8b9907fb03d000b99 | c6e95c268aa6b065737933cbeff10761939d8f310cb11db8b9907fb03d000b99 | yes | 1e098296814c47eeb2a04508386ebbf2dce426d5cc19fc4473fd58be07574687 |
| C3 | C3-CONTEXT-ENGINE-RESEARCH | b48cbb0b6f1205e66eed9b738d7b5ff3fc6d4db1b10584739149577d2dc9042c | b48cbb0b6f1205e66eed9b738d7b5ff3fc6d4db1b10584739149577d2dc9042c | yes | acbea07c10b156206e15e5eb03d66fb0f5b0a4c1a2cdc24b9857933303fbde70 |
| C4 | 9a6acd86-d868-4019-aa26-6a2755e64018 | 441007bcbdce318b212d7f166fb344e18e72d92e5d0090f75718b9bc9ec01651 | 441007bcbdce318b212d7f166fb344e18e72d92e5d0090f75718b9bc9ec01651 | yes | 4bd492b56532c132246ca8f2b29481b9f125f60b25b2d6bde86269f5763fec03 |
| C5 | C5-OPERATOR-CONTROL-RESEARCH-v4 | e70ea36bcab13b1abf76dbc386a82ca114a8c86c66f689d30224f1de71c9e1a8 | e70ea36bcab13b1abf76dbc386a82ca114a8c86c66f689d30224f1de71c9e1a8 | yes | 34b99995a07745e06aa0cdf97298e89614109da91815bbdd297f3355a943c451 |
| C6 | c6-cloud-evaluation-engine-v3 | a0d762ad472f0e5fb6a891495a943ca808ac642ab5b7d3b9eab42fd0e237946a | a0d762ad472f0e5fb6a891495a943ca808ac642ab5b7d3b9eab42fd0e237946a | yes | b031787b432477af353acd21d6be130465a541c1e492744c14f2a55601650321 |
| C7-FFA-003 | C7-FFA-003 (`assurance/audits/C7-FFA-003.md`) | no manifest value compared | 6ad46d60c08c71804e5efc3081f13ab0dbd53d83860c5924e888e26ffe0ccba7 | n/a | not looked up |

**Input to this revision.** The v2 input received was `ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.md`, size 31,924 bytes, SHA-256 `eb679f0d88f82a7ba73724b01eeb660e6bad1ed8a75568b0a516382fab215109`; the size and SHA-256 match the values C7-FFA-004 recorded for its candidate. The v2.1 input to this revision is `ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.1.md`, 55,345 bytes, SHA-256 `60cfae54f0a339d6c9251dda61ad79c473210ce5e1ce6a628b550b97fa1ffee1`.

**What COMPLETE means here.** The candidate covers eighteen numbered sections built from the pinned canonical inputs. C7-FFA-004 gate 2 notes this is a structural check only, because no separate canonical checklist of the "eighteen required sections" was supplied. It does not state that any design is implemented, tested or verified. The C7-FFA-003 verdict means the C1–C6 package was clean enough to synthesize, the open experiments remain open, and implementation has not started.

**Source-ceiling notes.** `STATUS.md` records a missing C5 v1 reference file cited by a later C5 artifact (DEP-08) and a missing Wave 3.5 C4 context Markdown file although its manifest exists. No claim in this document depends on either file; the canonical C1–C6 package is the source ceiling. DEP-03 (this synthesis deliverable) and DEP-10 remain `BLOCKED / PENDING C1` at the pinned baseline, DEP-07 (C6 Future Capability Packs) remains `MISSING / PENDING C6`, and ACTION-01 names the target path `architecture/synthesis/ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.md`; the file name of this candidate (`.v2.1.md`) is an intake question for the repository owner, not settled here.

**Claims that still need C7 source-level review.** The correction matrix is C1's own self-assessment and is not independent assurance. This document does not claim to be exhaustively audited or that each sentence is certified; C7-FFA-004 revision 3 describes its own source check as targeted, and the text of revision 4 was not supplied to C1, so its stated limitations are not restated here `[ATT]`. The following remain for C7 to check against sources:

- the A0–A4 crosswalk (§6), especially that C5's content-hash binding spans A2 and A3 `[INF]`;
- the MV-01–MV-06 crosswalk (§11.1), especially the possible overlap of C4 item (e) with MV-04 and MV-05 `[INF]`;
- the `C1-E1`-before-compiler ordering in `G-3` `[INF]` and the statement that no C3 source uses the term "context compiler";
- the proposed acceptance structure for `XC-RESUME` and the "restrict unneeded capabilities" principle `[PROP]`;
- the quoted source classifications (§8, §12), the C5 "Approval UX" tension note, and the C7-FFA-003 hash-column label;
- statements about repository state (79 files, no C6 pack in the tree, absence of a synthesis file), which rest on C1's own checkout `[ATT]`.

**Earlier synthesis draft.** An earlier synthesis draft from a previous session is not in the pinned tree `[ATT]`; this document does not depend on it, and the local C2–C5 drafts that differed from the canonical bytes were not used `[ATT]`.

**Evidence ceiling (each Cloud's recorded `evidence_status`).** C1 `PARTIAL`; C2 `DOCUMENTATION_ONLY`; C3 `mixed` (every observed claim resolves to an adjacent source line, ARGON-side adaptations remain `PROPOSAL`, several items are `UNKNOWN / NEEDS EXPERIMENT`); C4 `PARTIAL`; C5 `PARTIAL`; C6 `PARTIAL`. Wherever this synthesis assembles a mechanism from several artifacts, it is labeled `[PROP]` or `[INF]`.

---

## FINAL STATUS

```text
SOURCE_BASELINE:
71a3fa6d1fb1eed0e694886263710d4020e10341

PRIOR_AUDIT_VERDICT (C7-FFA-003, applies to the C1-C6 package):
CLEAN WITH OPEN EXPERIMENTS

CURRENT_AUDIT (C7-FFA-004 rev 3, applied to v2):
NOT ISSUED (no clean verdict) on v2; later revision text not supplied to C1; v2.1.1 has not been re-audited

CANDIDATE_STATUS:
V2.1.1 CANDIDATE - metadata and crosswalk corrections, offered for C7 re-audit; NOT accepted for repository intake

SYNTHESIS_STATUS:
18 SECTIONS PRESENT (structural coverage only; not an acceptance)

ACTION-02 / DEP-07 (C6 Future Capability Packs):
PENDING

WAVE_4_DESIGN:
NOT AUTHORIZED BY THIS DOCUMENT

RUNTIME_IMPLEMENTATION_AUTHORIZED:
NO

RUNTIME_SECURITY_EMPIRICALLY_DEMONSTRATED:
NO

IMPLEMENTATION_STATUS:
NOT_STARTED
```

PROPOSED NEXT STEP (not an authorization): C7 re-audit of this candidate. Intake, ACTION-02 sequencing and any Wave 4 authorization are decisions for the human governance authority.

report_sha256: NOT EMBEDDED. The digest of these exact bytes is supplied externally as proposed intake-manifest metadata. No manifest entry for this candidate exists in the pinned repository.
