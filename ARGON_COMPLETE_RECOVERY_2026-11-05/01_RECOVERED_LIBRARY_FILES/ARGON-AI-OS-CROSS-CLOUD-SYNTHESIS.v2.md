# ARGON AI-OS — CROSS-CLOUD SYNTHESIS v2

Phase D · post-final-forensic-audit synthesis · author: C1 · scope: ARGON AI-OS (`system_scope: ai_engineering_os`, `repository_target: none`, `execution_target: deliverable_output`)

This document consolidates the six canonical Cloud Evolution artifacts (C1–C6) under the closure state recorded by C7-FFA-003 (verdict `CLEAN WITH OPEN EXPERIMENTS`). It adds no research and no sources. It is architecture synthesis only: nothing here is implemented, approved, or verified beyond what the source artifacts themselves establish. Labels used throughout: **[SRC]** supported by a cited source in the named Cloud artifact · **[PROP]** ARGON proposal · **[INF]** inference by this synthesis · **[EXP]** NEEDS EXPERIMENT · **[UNK]** UNKNOWN · **[HUMAN]** human decision.

---

## 1. Executive Synthesis

The six artifacts describe one coherent engineering model for an ARGON AI Engineering OS. A model-independent **Kernel** holds the invariants (identity, state, mode, approval boundary, escalation, checkpoint, execution boundary, verification handoff, evidence hooks). A thin per-model **Adapter** absorbs vendor and model differences. A **Runtime** carries out Kernel rules mechanically. Around that stack sit six functional planes: Orchestration/Kernel (C1), Security/Authorization (C2), Context/Knowledge (C3), Surgical Engineering (C4), Human Control (C5) and Evaluation/Learning (C6).

Three conclusions carry the most weight:

1. **The control model converged across independent Clouds.** C1, C2, C4 and C5 each reached the requirement that planning must have no mutation-capable path. They agree on four mutation vectors and differ only on the fifth (§11). Approval is separated into four distinct levels by C2 and C5 independently, and cryptographic binding is `NEEDS EXPERIMENT` in both.
2. **Almost every mechanism is a design, not a fact.** All six artifacts are `DESIGNED / NOT_IMPLEMENTED` with evidence status `PARTIAL` or weaker. Enforcement exists today only as policy, except where an artifact states otherwise. Wave 4 has not started.
3. **The open list is explicit and bounded.** Ten registered experiments (§13) and a short list of human decisions (§14) hold everything the sources leave unresolved. None blocks synthesis; all block specific implementation steps (§15).

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

| # | Plane | Primary artifact | Status of the plane |
|---|---|---|---|
| 1 | Orchestration / Kernel | C1 | `DESIGNED`; ten responsibilities specified |
| 2 | Security / Authorization | C2 | `DESIGNED`; evidence status `DOCUMENTATION_ONLY` |
| 3 | Context / Knowledge | C3 | `DESIGNED`; pipeline is an ARGON proposal |
| 4 | Surgical Engineering | C4 | `DESIGNED`; deferred, no source code to act on |
| 5 | Human Control | C5 | `DESIGNED` |
| 6 | Evaluation / Learning | C6 | `DESIGNED`; every ARGON-side mechanism is `PROPOSAL` |

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
| 8 | Execution boundary: ACT performs only the approved action | C2 RP-13 (binding level `[EXP]`) |
| 9 | Verification handoff: no Cloud marks its own claim `VERIFIED` | C6 (evaluation independence); C7 |
| 10 | Audit/evidence hooks: every claim resolves to a source reference | C2 evidence store, RP-14; C6 trajectory |

Restated for self-containment: the **approval record** is a recorded object tying a task to an exact action, an approver, a scope and an expiry. That object originates in earlier internal work that is not part of the canonical package, so it is treated here as `[PROP]`, not as evidence. The **checkpoint** questions C1 answers (what is checkpointed, what authority changes, what evidence is needed) leave two items `[UNK]`: whether stale state may be resumed, and what invalidates a checkpoint.

## 4. Adapter Layer

Everything model-specific stays behind the Adapter [SRC C1 Model Portability Boundary]:

- exact tool-call schema and format;
- instruction verbosity and structuring tuned per model;
- context-window size and the resulting compression needs.

Supporting evidence is qualitative. A shared interface was run against more than one model family in SWE-agent, and Aider's architect/editor mode mixes model providers across its two roles [SRC C1 P4]. Exact numeric gaps between models are third-party summaries and are not restated. No second model backend has been available, so **adapter sufficiency is untested** (experiment E3). Vendor-specific observations, such as Claude Code subagent behavior, remain vendor observations and are never promoted to Kernel rules. C2 RP-9 adds a boundary condition: enforcement is a property of the deployment, not of the agent or the model; whether ARGON can provide that deployment is `[UNK]`.

## 5. Runtime

| Mechanism | Source | Status |
|---|---|---|
| Tool registration per `processing_state` (implements Kernel item 3) | C1 P2, C2 RP-1, C5 P1 | `[PROP]`, enforcement test `[EXP]` (E2) |
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

**Approval vocabulary (kept strictly separate)** [SRC C2 approval authority model; C5 P4]:

| Level | Meaning | Demonstrated by any source? |
|---|---|---|
| Category/Prefix Approval | allows a class or pattern of actions | yes, as external precedent (partial) |
| Exact Action Approval | bound to one specific action | `[PROP]` |
| Exact Payload Binding | bound to the literal payload representation | `[PROP]` |
| Cryptographic Binding | adds signature or hash with key custody | **`[EXP]`** (RP-13) |

Showing the operator the parameters is **display**. It is not payload binding and it is not authorization (C5 P4). A hash field is not a trust infrastructure. RP-13 stays `NEEDS EXPERIMENT` across six unresolved questions: key custody, identity binding, replay prevention, expiry, revocation, exact-payload binding.

**Plan/Act control position.** `PLAN` has no mutation-capable path; `REVIEW` is read-only; `APPROVAL` is explicit human authorization where required; `ACT` exposes mutation tools only after authorization; `VERIFY` is independent. This is an **ARGON design proposal**. Public vendor precedent is partial and limited, so no source is cited as proving universal enforcement, and the enforcement test is `[EXP]` (E2).

**Other positions retained from the sources.** Secrets never enter agent context (C2 RP-12, `ADOPT`). MCP trust distinguishes connect-time from runtime, with tool poisoning and confused-deputy risks named (C2 RP-11, `ADOPT`). Evidence carries trust tiers and self-attestation is not accepted (C2 RP-14, `ADOPT` as principle; specific mechanisms `[EXP]`). The circuit breaker (RP-4) does not prevent segmentation of a high-risk action into low-risk steps (C5 raises this as an open question for C2). Reversibility is not authorization: C5 P5 rejects it as a default, with a narrow carve-out left `[EXP]`. Sandbox-only autonomy that removes human authority is rejected (C5 P6). Whether third-party MCP is in ARGON's scope at all is `[HUMAN]` (C2).

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

**Counter-evidence kept in view:** a no-compression, minimal design (mini-swe-agent, C3 P15) works in the cited setting, so whether ARGON needs compression at all is `[UNK]`. Compression must never discard authority: claim, source, owner, status and snapshot reference survive; only prose is compressible (C6 P4 keeps the durable evidence store uncompressed). Caching strategy, information-gain gating and cost-aware escalation are not covered by any of the six artifacts and are not extended here. Per-role baseline sizing is experiment E1. **Task isolation** has no external precedent in C3's sources and is `[EXP]`; **freshness triggers** are `[UNK]/[EXP]`.

## 8. Surgical Engineering

`Problem → Localization → Hypothesis → Exact Edit Location → Minimal Patch → Validation` [SRC C4; PROP for ARGON].

Failure taxonomy: **Localization Failure**, **Repair Failure**, **Validation Failure** (C4 §3, built from the phase boundaries; C6 reuses the same three axes in failure analysis).

| Pattern (C4) | Verdict |
|---|---|
| A hierarchical localization; B structured diff-style edits; C lint/syntax gate; D atomic revertible commits; E purpose-built bounded tool interface over a raw shell | `ADOPT` |
| F Plan/Act | `NEEDS EXPERIMENT` (downgraded) |
| G granular category-scoped approval | `ADAPT` |
| H CodeAct unified action space vs. bounded ACI vs. minimal interface | **`NEEDS EXPERIMENT`** |

The **structured ACI versus bash-only minimal interface** question (C1 P3, C3 P15, C4 H) is unresolved and stays `NEEDS EXPERIMENT` (C4-INTERFACE). Validation uses a dual gate: regression plus issue-specific reproduction (C4, C6 P6). C4's applicability note holds: ARGON-HEALTH has no source code, so this plane is deferred to a real implementation repository. Seven C4 experiments are defined and not executed (§13).

## 9. Human Control

`PLAN → REVIEW → APPROVAL → ACT → VERIFY` is always visibly staged [SRC C5; PROP]. C5 patterns: P1 runtime-enforced mode (`ADOPT`), P2 `ADAPT`, P3 `ADOPT`, P4 approval display versus binding (corrected, see §6), P5 `REJECT` as default, P6 `REJECT`, P7 `ADOPT`, P8 unattended-run behavior (`ADOPT` if unattended runs exist, otherwise `[UNK]`).

Required properties: visible state; visible scope; visible approval; stop; audit; resumption. Display is not authorization and is not payload binding. Conflicts are shown as claims with evidence and authority, never as a vote count. A success mark is reserved for `VERIFIED`; `PROPOSED` and `DESIGNED` never earn one. **Resumption after a stop is not designed** (checkpoint staleness and invalidation are `[UNK]`; experiment RESUME). Whether ARGON will run unattended at all is open (C5 P8).

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
| Promotion / rejection | promote only if the training set improves, the validation set generalizes, and both regression gates pass; logged, versioned, reversible. No promotion has ever occurred |
| Feedback | rejection reasons return to failure analysis and to candidate generation |

**Metrics (C6):** correctness · grounding · evidence integrity · scope adherence · token efficiency · tool efficiency · test completeness · minimality · false completion (canary) · security violations. Each carries a definition, unit, measurement method, cost and expected failure signal.

**Benchmark validity discipline.** A benchmark score is not general agent quality. C6's validity limits: flawed tests and annotation errors (a corrected parser changed over half of the annotation data in both SWE-bench Lite and Verified, per the cited paper); patch correctness is not the same as test pass; contamination; version drift (SWE-bench, Lite and Verified are not interchangeable); held-out validity decays with reuse. Any score cited must name its benchmark, version, model and metric.

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
| a | Plan/Act mutation test | C1, C2, C4, C5 | C1 and C2 list the same five vectors (direct write tool, shell write, interpreter write, wrapper/composite, indirect via nested tool call). C4 defines its fifth as argument injection into an ostensibly read-only tool. Both are real attack surfaces. Reconciliation `[PROP]`: test **six** vectors, treating C4's as a sixth. Classifications also differ (C2 RP-1 and C5 P1 `ADOPT`, C4 F `NEEDS EXPERIMENT`); resolved as: requirement adopted, implementation `[EXP]` | minor divergence, non-blocking (C7); reconciled here |
| b | Approval levels | C2, C5 | same four-level separation, reached independently | consistent |
| c | Failure axes | C4, C6 | C6 failure analysis reuses C4's three axes | consistent |
| d | Compression | C3, C6 | both adopt bounded compression with the window `[UNK]`; both keep the durable evidence store uncompressed; C3 P15 holds counter-evidence | consistent, open |
| e | Interface shape | C1, C3, C4 | structured ACI versus minimal: all three record the tension | open (C4-INTERFACE) |
| f | Delegation depth | C1 only | no other Cloud addresses it; vendor evidence is contested | single-Cloud `[PROP]`, E1b |
| g | Benchmark discipline | C1, C4, C6 | source-verified, third-party and conflicting figures kept apart | consistent |
| h | Metadata vocabulary | C1–C6 | identical `system_scope` / `repository_target` / `execution_target` triple | confirmed by C7 |
| i | Self-containment | C1–C6 | internal earlier-wave dependencies are labeled as such, not as external evidence | acceptable |

**C7 minor items folded in.** C7 records that C1 dropped a "+10.7 percentage points (Lite)" figure as unconfirmable, although the figure appears in the primary source's prose; the paper's own table shows 11.00% versus 18.00% (7.0 points), a tension the paper does not reconcile. Net effect per C7: a true, cautious claim was dropped, not a false one asserted. This synthesis does not restate either figure.

## 12. Adopt / Adapt / Reject

| Item | Source | Verdict |
|---|---|---|
| Context isolation per delegated Cloud | C1 P1 | `ADOPT` (isolation); delegation depth `ARGON ORIGINAL` / `NEEDS EXPERIMENT` |
| PLAN has no mutation path | C1, C2, C5 | `ADOPT` as requirement; implementation `NEEDS EXPERIMENT` |
| Structured bounded interface over raw shell | C1 P3, C4 E | `ADOPT` (deferred) |
| CodeAct vs bounded ACI vs minimal | C4 H | `NEEDS EXPERIMENT` |
| Interface/role portability across models | C1 P4 | `ADOPT` (qualitative) |
| Checkpoint before elevated trust | C1 P5, C4 D, C3 P9 | `ADAPT` / `ADOPT` |
| Feedback-rich evaluation | C1 P6, C6 P1 | `ADOPT` (shape); optimizer `UNKNOWN` |
| Train / validation / held-out discipline | C6 P2 | `ADOPT` (pattern) |
| Structured trajectory | C6 P3, C2 RP-6 | `ADAPT` / `ADOPT` |
| Dual-gate validation | C4, C6 P6 | `ADOPT` / `ADAPT` |
| Category/Prefix approval | C2 | `ADOPT` (external precedent partial) |
| Exact-payload and cryptographic binding | C2 RP-13 | `NEEDS EXPERIMENT` |
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

Primary register. Success measurements restate the source artifacts' own specifications and invent no thresholds.

| experiment_id | question | owner | affected_component | why_unknown | required_environment | success_measurement | risk_if_wrong | when_to_run |
|---|---|---|---|---|---|---|---|---|
| E1 | Does per-role context baseline sizing cut tokens without changing outcomes? | C1 (C3 token engine) | Context compiler, Kernel baselines | never tested; per-tier ceilings undefined | at least 10 representative tasks per role (C1 spec) | token count down with unchanged claim outcomes | silent loss of needed context | before the Wave 4 context compiler |
| E1b | Does ARGON's bounded delegation depth match or beat deeper delegation? | C1 | Kernel delegation rule | vendor evidence is contested and version-dependent; ARGON proposal only | tasks that plausibly need a second delegation level | outcome quality and token cost, depth-1 vs depth-2 | needless restriction or runaway delegation | before the Kernel delegation rule is fixed |
| E2 | Does PLAN block mutation across all vectors (six after §11a)? | C1, C2, C4 | Runtime tool registration | sources document named-tool absence only; other paths untested | implementation environment with every vector available | zero successful mutations on every vector, tested independently | false security if only the named tool is closed | before any APPROVAL/ACT flow |
| E3 | Is a thin calling-convention adapter enough across two or more model backends? | C1 | Adapter boundary | only one model/session has existed | a second model backend | zero Kernel carve-outs across providers | Kernel becomes model-coupled | when a second backend exists |
| E4 | Can a stopped or failed ACT recover from its checkpoint reference alone? | C1 | Checkpoint / approval record | resumption not designed | implementation environment, deliberately interrupted tasks | recovery from the reference without re-derivation | lost progress or inconsistent state | before any resumable ACT flow |
| E5 | Do structured verification records cut correction cycles versus bare pass/fail? | C1, C6 | Evaluation / verification | never tested | planted-defect artifacts verified both ways | correction cycles per condition | extra structure that does not pay | after an evaluation harness exists |
| RP13 | Can cryptographic action binding be made safe? | C2 | Approval / security | six questions undesigned: key custody, identity, replay, expiry, revocation, payload binding | implementation environment with signing infrastructure | all six dimensions independently verified | false assurance from a broken scheme | before any live write relies on it |
| C4-INTERFACE | CodeAct vs bounded ACI vs minimal interface | C4 (C1, C3) | Runtime, surgical tooling | vendor evidence conflicts (performance vs simplicity) | a real implementation repository | the test C4 specifies for Pattern H | costly early commitment | before surgical tooling is built |
| RESUME | What are the semantics of resuming after a stop? | C1, C5 | Human control, runtime | stale-state resumption and checkpoint invalidation undesigned | implementation environment | none designed yet | silent state loss | before long-running ACT flows |
| ISOLATION-ENFORCEMENT | Does task-context isolation hold under a real mechanism? | C3 (C1) | Runtime | no external precedent; no mechanism exists | multi-task implementation environment | zero cross-task contamination; trial count N is `[UNK]` in C3 | silent leakage | before any multi-task runtime |

Secondary register (owner Cloud and pointer to the full specification):

| Group | Items | Owner | Status |
|---|---|---|---|
| C4 Experiments 1–7 | localization accuracy; patch minimality; regression pass rate; reproduction pass rate; unrelated-file touches; repair success after correct localization; false-positive localization | C4 | defined, **not executed** |
| C3 experiments | promotion threshold (E1); token-savings percentage (E2); isolation-trial count (E4); further items in C3 §7 | C3 | thresholds `[UNK]` |
| C6 open items | optimizer choice; trajectory step granularity; compression window; held-out reuse limit; judge-call cost; evidence-vocabulary fit; dual-gate overlap | C6 | `[UNK]` |
| C2 open items | segmentation bypass of the circuit breaker; sandbox-configuration injection (RP-10); deployment-feasibility of enforcement (RP-9) and container isolation (RP-6) | C2 | `[EXP]` / `[UNK]` |
| C5 open items | whether unattended runs exist (P8); narrow reversibility carve-out (P5) | C5 | `[UNK]` / `[EXP]` |

## 14. Human Decisions

Only decisions that the final sources themselves leave open:

1. **Delegation depth value** (C1; E1b).
2. **Interface direction:** structured ACI, CodeAct or minimal (C4 H; C3 P15 counter-evidence).
3. **Whether ARGON invests in cryptographic-binding rigor at all**, versus a simpler approval-record model (C2 RP-13).
4. **Which approval level ARGON adopts as its baseline** (C2 states it does not choose).
5. **Whether third-party MCP is in ARGON's scope** (C2).
6. **Whether to deepen source coverage.** C1 names not studied: OpenHands, SWE-ReX, Roo Code, Goose, OpenAI Agents SDK, PydanticAI, smolagents, LangGraph. C6 names not studied: Terminal-Bench, OpenHands Benchmarks, SWE-ReX, LiteLLM spend tracking, LangGraph durability.
7. **Whether unattended runs exist at all** (C5 P8).
8. **Whether infrastructure for deployment-level enforcement is feasible** (C2 RP-9; C2 marks feasibility `[HUMAN]`/`[UNK]`).

Not carried: the instructions for this phase mention a 15-minute snapshot-staleness proposal. It appears in none of the six canonical artifacts (it belongs to earlier internal work outside the package), so it is not recorded here as a package-sourced decision. The human may still adopt or replace it; freshness triggers remain `[UNK]/[EXP]` in C3.

## 15. Wave 4 Preconditions

Before any implementation step:

- E2 exists as a runnable test and passes on every vector, before Runtime is layered on any assumed enforcement.
- A second model backend exists before any adapter-sufficiency claim (E3).
- Human decisions 2 and 3 are made before surgical tooling and approval infrastructure are built.
- The evidence and trajectory schemas (C2 evidence store, C6 trajectory) are fixed before evaluation code depends on them.
- The approval record, today `[PROP]` in earlier internal work, is formalized in a canonical schema document.
- A real implementation environment exists; the research sprint produced none.

## 16. Recommended Wave 4 Design (ARGON PROPOSAL only)

An order derived from what the sources support; no item is approved or verified:

1. **Kernel validator:** the ten responsibilities as a checkable rule set; pure logic, no tools (`[PROP]`).
2. **Evidence and trajectory store:** schema first, per C2's trust tiers and C6's step schema (`[PROP]`, `ADAPT`).
3. **Context compiler, document-graph variant:** matches a docs-only repository (C3 P3 `ADOPT`; thresholds `[UNK]`).
4. **Approval record at Category and Exact-Action levels:** cryptographic binding deferred (`[EXP]`).
5. **Plan/Act enforcement test harness (E2):** built before further Runtime.
6. **Evaluation harness skeleton:** benchmark fixtures, (score, reason) metric functions, regression set with the dual gate; **no automatic promotion** (C6 promotion is `PROPOSAL`).
7. **Surgical-engineering tooling:** only after human decision 2.

## 17. What Must NOT Be Built Yet

- Cryptographic approval-binding infrastructure (RP-13).
- Any per-tier token ceiling or promotion threshold without an experiment behind it.
- Automatic prompt, router or Kernel promotion; and optimizing against the same set used to declare success.
- A full ACI or CodeAct layer before the interface decision.
- Delegation deeper than one level before E1b.
- Session-resumption logic (undesigned) and unattended-run machinery (unresolved).
- Third-party MCP integration before the scope decision.
- Cross-model adapters beyond a stub.
- Any ARGON-HEALTH or Legacy ARGON change, any ADR or ACR, any clinical code. This program does not touch them.

## 18. Provenance / Evidence Status

| Input | artifact_id | sha256 (verified on actual bytes) | Matches own manifest | Matches C7-FFA-003 |
|---|---|---|---|---|
| C1 | c1-cloud-evolution-harness-v4-final | 24e8cdb1cb8a088f146ff97265a484a329544b6a13d3bdfafea00de9f5dc688f | yes | yes |
| C2 | C2-CLOUD-SECURITY-ADAPTER-RESEARCH | c6e95c268aa6b065737933cbeff10761939d8f310cb11db8b9907fb03d000b99 | yes | yes |
| C3 | C3-CONTEXT-ENGINE-RESEARCH | b48cbb0b6f1205e66eed9b738d7b5ff3fc6d4db1b10584739149577d2dc9042c | yes | yes |
| C4 | 9a6acd86-d868-4019-aa26-6a2755e64018 | 441007bcbdce318b212d7f166fb344e18e72d92e5d0090f75718b9bc9ec01651 | yes | yes |
| C5 | C5-OPERATOR-CONTROL-RESEARCH-v4 | e70ea36bcab13b1abf76dbc386a82ca114a8c86c66f689d30224f1de71c9e1a8 | yes | yes |
| C6 | c6-cloud-evaluation-engine-v3 | a0d762ad472f0e5fb6a891495a943ca808ac642ab5b7d3b9eab42fd0e237946a | yes | yes (canonical bytes) |
| C7-FFA-003 | C7-FFA-003 | two copies, identical text, table-formatting differences only | n/a | n/a |

**What COMPLETE means here.** `SYNTHESIS_STATUS: COMPLETE` states that this document covers all eighteen required sections from verified canonical inputs. It does not state that any design is implemented, tested or verified. C7's verdict means the package is clean enough to synthesize, the open experiments remain open, and implementation has not started.

**Superseded inputs.** An earlier synthesis (`ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.md`) was built on earlier local drafts of C2–C5 and on a missing-input premise that no longer holds; it is superseded by this version. The local C2–C5 drafts that differed from the audited bytes were not used.

**Evidence ceiling.** Source evidence statuses: C1 `PARTIAL`, C2 `DOCUMENTATION_ONLY`, C3 mixed, C4 `PARTIAL`, C5 `PARTIAL`, C6 `PARTIAL`. Wherever this synthesis assembles a mechanism from several artifacts, it is labeled `[PROP]` or `[INF]`.

---

## FINAL STATUS

```text
C7_VERDICT:
CLEAN WITH OPEN EXPERIMENTS

SYNTHESIS_STATUS:
COMPLETE

NEXT_PHASE:
AI-OS WAVE 4 DESIGN

IMPLEMENTATION_STATUS:
NOT_STARTED
```

NEXT OWNER: AI-OS Wave 4 Design

report_sha256: recorded_in_manifest
