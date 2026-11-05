# C2-CLOUD-SECURITY-ADAPTER-RESEARCH.md

**Cloud:** C2 — Security Research Cloud, ARGON AI-OS
**Nature:** Research only. No ARGON-HEALTH, Legacy ARGON, ADR, ACR, Domain, or Workflow
modified. No control implemented. Wave 3.5 not reopened — this document does not restate
or re-decide anything from `C2-WAVE3.5-SECURITY-RECONCILIATION-v2.md`; where a finding
here bears on an open Wave 3.5 item, it is noted as new evidence for that item, not a
re-decision.
**Supersedes:** an earlier, less rigorous pass at this same filename
(`sha256: a09a2c66b1050fdfcef8eef5cd816f23d906c06bd25257b5fc585b8082ac2305`, produced
earlier in this conversation). This revision applies the full required structure, source
integrity discipline, and the mandatory 9-question analysis the prior pass lacked.
**Sources consulted:** Cline, Claude Code, OpenHands, SWE-agent, Aider, MCP ecosystem
(OWASP, SOC Prime, an academic MCP-security systematization paper), plus general
AI-agent-authorization/attestation literature (an IETF draft, the IETF RATS architecture,
several smaller open-source specs/tools) needed to answer the approval-authority and
evidence-integrity questions this brief requires, since none of Cline/Claude
Code/OpenHands/SWE-agent/Aider/Agentless publish a formal cryptographic approval-binding
or evidence-attestation model. **No leaked prompts were used as a source anywhere in
this document.** Access date for all web sources: 2026-09-20.
**Evidence-quality note, stated once and applied throughout:** sources vary sharply in
standing. Cline/Claude Code/OpenHands/SWE-agent/Aider official docs = `STRONG EVIDENCE`
(maintained, public, product-authoritative). The MCP-security sources = `STRONG EVIDENCE`
for OWASP; `MODERATE` for the arXiv systematization paper (peer-review status not
verified). The cryptographic-approval/attestation sources (a GitHub sample repo, a small
PyPI tool, an individual's dev.to post, an IETF *draft* — not an RFC, and one arXiv paper
whose peer-review status is unverified) = `EMERGING / LOW-ADOPTION EVIDENCE`. They are
included because they are the only sources found that address exact-action authorization
and evidence-attestation architecture at all — not because they represent established
industry consensus. This is flagged per-pattern below, not smoothed over.

**report_sha256:** recorded_in_manifest (per Hash Contract — this file never embeds its
own hash inline, to avoid a stale/self-referential value; the canonical, freshly
computed SHA-256 lives only in the sibling manifest file).

**Self-containment note on internal "Wave 3.5" references throughout this document:**
every mention of Wave 3.5 or `C2-WAVE3.5-SECURITY-RECONCILIATION-v2.md` below is
**internal ARGON continuity context** (this Cloud's own prior proposal history), never
cited as external evidence proving an `OBSERVED` claim. Every `OBSERVED` claim in this
document resolves to a public source (URL/section/access date), listed per-pattern —
the Wave 3.5 references never substitute for that.

---

## CORRECTION PASS v1 — APPLIED TO THIS ARTIFACT

**Honesty disclosure required before anything else:** the Correction Pass v1 brief
instructs using `C7-CLOUD-EVOLUTION-FINAL-AUDIT.v3` as the baseline finding list. **That
file was never produced or shown to this Cloud in this conversation.** No C7 audit of
this artifact has actually happened. Per the brief's own Section 10 (Evidence
Self-Containment) and Section 12 (No Silent Cleanup), this is stated plainly rather than
assumed or silently worked around. What follows corrects this artifact against the
**specific, self-contained C2 findings enumerated directly in the Correction Pass v1
document itself** (C2-RP1/X1, C2-X3, C2-X4, C2-D6, C2-RP13) — those are actionable
without the underlying audit file because the brief states exactly what is wrong and
what to change. Any broader "C7 findings" that might exist only inside the un-provided
`.v3` file are not addressed here, because they are not visible to this Cloud. See the
C7 Finding Matrix at the end of this document for the complete accounting.

### Shared cross-cloud vocabulary (Correction Pass v1 §4) — adopted

```yaml
system_scope: ai_engineering_os
repository_target: none
execution_target: deliverable_output
```

Replaces the prior `repo_target: n/a` field used in this artifact's original manifest.

### ARGON PROPOSED CONTROL MODEL — Plan/Act (Correction Pass v1 §5, terminology aligned
to Final Correction Pass v4 §4)

Stated once here as the canonical reference every per-pattern correction above points
back to. **This is ARGON's own proposed control model, not a claim that any studied
vendor implements it in this exact form:**

```text
PLAN:     no mutation-capable execution path
REVIEW:   read-only / analysis capabilities
APPROVAL: explicit human authorization where required
ACT:      mutation-capable execution only after required authorization
VERIFY:   independent verification / evidence collection
```

This is an `ARGON DESIGN PROPOSAL`, not a vendor fact, and any implementation of it is
`NEEDS EXPERIMENT` — restated explicitly per Final Correction Pass v4 §4, since the
prior correction pass's wording ("write-capable") is functionally the same concept but
is now aligned to the exact term ("mutation-capable") the current pass specifies.

### Common Approval Position vocabulary (Correction Pass v1 §6) — adopted

- **Category Approval** — permits a class of actions (e.g. Claude Code's
  `Bash(git push --force:*)` prefix rule; RP-2, RP-5).
- **Exact Action Approval** — tied to one specific, identified action instance.
- **Exact Payload Binding** — tied to the literal payload/action representation itself
  (RP-13's `artifactHash` concept).
- **Cryptographic Binding** — adds signature/key-custody on top of payload binding
  (RP-13, `signerKeyId`/signature fields).

Rule applied throughout this corrected artifact: `external precedent != ARGON
requirement` — no pattern above is presented as proof that ARGON must adopt it, only as
evidence informing a proposal.

---

## PATTERN INDEX (14 patterns, mapped to the 16 required topics)

| Topic requested | Covered by |
|---|---|
| tool permissions | RP-1, RP-2 |
| sandboxing | RP-3, RP-6, RP-9 |
| worktrees | RP-2 |
| path restrictions | RP-3, RP-9 |
| network restrictions | RP-3, RP-9 |
| secret handling | RP-7, RP-12 |
| approval boundaries | RP-1, RP-2, RP-13 |
| human authorization | RP-1, RP-9, RP-13 |
| tool-result trust | RP-11 |
| destructive operations | RP-3, RP-5 |
| commit/push controls | RP-2, RP-7, RP-8 |
| merge controls | RP-2 |
| MCP/write-capable integrations | RP-11 |
| approval laundering | RP-4, RP-13 |
| evidence-store trust | RP-14 |
| command-vs-content separation | RP-3, RP-5 |

---

## RP-1 — Plan/Act as a hard capability split

**SOURCE:** Cline documentation. URL: `docs.cline.bot/core-workflows/plan-and-act` and
`docs.cline.bot/getting-started/your-first-project.md` (via search excerpt). Section:
"Plan and Act Modes." Exact claim supported: in Plan mode Cline "does not create or
modify any files"; switching to Act mode is a manual, human-toggled action, not something
Cline can do on its own. Accessed 2026-09-20. Evidence quality: `STRONG` (official docs).

**OBSERVED PATTERN:** the read/write boundary is implemented as a *mode* with different
available capabilities, not as an instruction the model is asked to follow while
retaining the same capabilities throughout.

**WHY IT WORKS:** removes the failure mode of a model reasoning about a plan and then,
in the same turn, silently starting to mutate files — because the write capability does
not exist while the mode is Plan.

**ARGON ADAPTATION:** `PROPOSAL` — the AI-OS `PLAN` state should mean no write-capable
tool is registered/callable, not that the Cloud is told not to write.

**REJECT IF:** ARGON's runtime cannot actually deregister tools per state — then this
degrades to a prompt-only rule, i.e. exactly the same status every ARGON rule already
has.

**TEST NEEDED:** attempt a write call while Kernel state = `PLAN`; expect a hard failure
at the tool-registration layer, not a caught policy violation after the fact.

**9-question analysis:**
1. What does it prevent? Silent writes during a stated "just planning" phase.
2. Where is enforcement? Tool-registration layer (client/harness), per the source.
3. Enforcement class: `TOOL/HARNESS ENFORCED` (source does not describe OS-level
   backing for this specific mechanism).
4. Bypass path: none documented in the source; theoretically, if the harness itself has
   a bug exposing write tools in Plan mode, the mode label alone would not stop it.
5. Human approval needed? To switch modes, yes — a manual toggle.
6. Exact-action bound? N/A — this gates a *category* (write) not a specific action.
7. Approval reusable across actions? Mode stays until manually toggled back — so yes,
   once in Act mode, the "approval" to be in Act mode covers many subsequent actions
   (each of which, per Cline, still needs its own per-action approval unless
   auto-approve is separately enabled).
8. Can tool result change authority? Not described in source.
9. Rule location: `Runtime` (tool-registration/harness layer).

**CLASSIFICATION: ADOPT**

> **CORRECTION PASS v1 — C2-RP1/X1 applied; terminology aligned in Final Correction Pass
> v4 (X1).** The classification above is retained, but is now split explicitly, since
> the original phrasing risked reading as a vendor-proven universal fact rather than a
> single vendor's design choice being proposed for ARGON:
>
> - `PUBLIC PRECEDENT`: Cline's Plan mode removes file-write capability entirely while
>   in that mode (source-confirmed, one vendor, one implementation) — this remains
>   `PARTIAL/LIMITED` precedent for the broader "no mutation-capable execution path"
>   claim, since Cline's own scope is file-write specifically, not every mutation path.
> - `ARGON CONTROL REQUIREMENT` (ARGON's own proposed rule, not a claim other vendors
>   share it): the AI-OS `PLAN` state must have zero mutation-capable execution path —
>   no registered write tool, and, per the widened test scope below, no indirect route
>   to mutation either.
> - `IMPLEMENTATION`: `NEEDS EXPERIMENT`.
>
> **Widened test scope (shared C1/C2 correction, restated per Final Pass v4 §11 X1's
> exact five-item list):** the original TEST NEEDED above checked only a direct
> write-tool call — insufficient. A real test suite must also cover: (1) direct write
> tool, (2) shell write (e.g. `echo x > file` via a nominally read-only shell tool),
> (3) interpreter write (a Python/JS eval tool writing to disk indirectly),
> (4) wrapper/composite write (per RP-5's documented blind spot, applied here too), and
> (5) indirect mutation (a tool that itself invokes another tool with write access).
> Items 2-5 were not tested in the original artifact — recorded as `NEEDS EXPERIMENT`
> for the full Plan/Act boundary; only item 1 ("a direct write-tool call is blocked")
> remains `ADOPT` as a design direction.

---

## RP-2 — Tiered allow/deny/ask rules, fail-closed default, worktree-scoped persistence

**SOURCE:** Claude Code documentation, `code.claude.com/docs/en/permissions`. Section:
"Permission system." Exact claims supported: permission rules are organized as `allow`/
`deny`/`ask` lists (with a `defaultMode` for unmatched tools); a saved "don't ask again"
approval for a Bash rule is written to `.claude/settings.local.json` "resolved through
worktrees to the main checkout," and applies to "future sessions anywhere in that
repository, including sessions started in subdirectories and in worktrees." A file-edit
approval, by contrast, "lasts until the session ends" (not persisted). Accessed
2026-09-20. Evidence quality: `STRONG` (official docs).

**OBSERVED PATTERN:** (a) three-tier decision vocabulary with a configurable default for
anything unmatched; (b) different approval types have different persistence — command
approvals can be remembered repo-wide across worktrees, file-edit approvals cannot be
remembered past the session.

**WHY IT WORKS:** reduces repeated prompting for genuinely low-risk, previously-reviewed
categories, while keeping file mutation approval narrowly scoped to the session that
requested it — a deliberate asymmetry, not an oversight.

**ARGON ADAPTATION:** `PROPOSAL` — adopt the three-tier vocabulary with an explicit
default (already partly established for ARGON per the Wave 3.5 v2 reconciliation);
adopt the persistence asymmetry: git/command-level "remembered" approvals scoped to a
repo+worktree identity, file-mutation approvals never persisted past a single task.

**REJECT IF:** if ARGON's isolated-branch model does not map cleanly onto git worktrees
specifically (ARGON may use branches without literal worktrees) — the persistence
*mechanism* (tied to worktree resolution) may not transfer even if the *policy shape*
does.

**TEST NEEDED:** confirm a "remembered" approval scoped to one isolated branch does not
silently apply to a different branch/worktree for the same repo.

**9-question analysis:**
1. Prevents: repeated identical prompts for reviewed-safe actions; unbounded/implicit
   allow for anything not explicitly classified.
2. Enforcement location: client-side settings resolution (`.claude/settings.local.json`,
   also project/user/managed settings layers per the source).
3. Enforcement class: `TOOL/HARNESS ENFORCED` — this is a client-side settings file, not
   described as OS-enforced on its own (see RP-3 for the separate sandbox layer).
4. Bypass path: a settings file is just a file — if it lives in a location an untrusted
   content channel could write to (analogous to the Aider finding in RP-7), a rule could
   be silently added. The source does not discuss this risk directly; this is C2
   `INFERENCE`, not an `OBSERVED` claim from the source.
5. Human approval needed: yes, for anything in `ask` or hitting the default.
6. Exact-action bound: rules can be command-prefix-specific (see RP-5) — moderately
   exact, not fully payload-hash-bound (contrast RP-13).
7. Approval reusable across actions? Yes, by design, for the persisted command-prefix
   category — this is a deliberate, documented reusability, not a flaw, but it is
   exactly the kind of category-level reuse that (per RP-4/RP-13) needs a separate
   safeguard against laundering.
8. Can tool result change authority? Not described in source.
9. Rule location: `Runtime`/config layer, resolved per-repository.

**CLASSIFICATION: ADOPT**

---

## RP-3 — OS-level sandbox as an enforcement layer independent of the model's own judgment

**SOURCE:** Claude Code sandboxing docs, `code.claude.com/docs/en/permissions` and
`code.claude.com/docs/en/sandboxing`, plus an independent walkthrough (dev.to,
"Claude Code Safety Guide"). Exact claim supported: "Use both for defense-in-depth,
since sandbox restrictions still apply even if a prompt injection bypasses Claude's
decision-making." The sandbox (bubblewrap on Linux, Seatbelt on macOS) restricts
filesystem and network reach for Bash and child processes to a defined boundary,
independent of whether the permission layer approved the command. Accessed 2026-09-20.
Evidence quality: `STRONG` (official docs, corroborated by a third-party walkthrough).

**OBSERVED PATTERN:** two independent layers — "should this run" (permission decision,
model-influenced) and "what can it reach if it runs" (sandbox, not model-influenced) —
both mandatory, explicitly framed as defense-in-depth specifically *against* prompt
injection defeating the first layer.

**WHY IT WORKS:** this is the concrete, shipped answer to "a rule that only exists in a
prompt is not a hard control" — the sandbox is the part that is not a prompt.

**ARGON ADAPTATION:** `PROPOSAL` — ARGON's hard-gated actions (destructive shell,
destructive git, outbound transfer) should be paired with an execution-environment
restriction (path allow-list, network allow-list) enforced independent of the Cloud's
own compliance, not solely an approval-request flow.

**REJECT IF:** ARGON's Clouds only ever run inside an already-sandboxed outer harness
with no further nesting available — in that case this degrades to "trust the outer
harness," which must be stated as such rather than claimed as ARGON's own control.

**TEST NEEDED:** simulate an approval-flow bypass (fault injection) and confirm the
sandbox boundary still holds independently.

**9-question analysis:**
1. Prevents: filesystem/network reach beyond a declared boundary, even under a
   compromised or injection-defeated decision layer.
2. Enforcement location: OS kernel primitives (bubblewrap/Seatbelt).
3. Enforcement class: `OS/PLATFORM ENFORCED`.
4. Bypass path: documented in the same doc set — sandbox unavailable/dependency-missing
   falls back to *unsandboxed* execution with only a warning, unless
   `sandbox.failIfUnavailable` is set true. This is an important, source-stated bypass:
   the safe path is opt-in, not default-fail-closed, unless separately configured.
5. Human approval needed: independent axis — sandboxing does not replace the permission
   layer's approval requirement, it bounds what an approved (or auto-approved) action can
   reach.
6. Exact-action bound: no — this bounds a whole session/process, not one action.
7. Approval reusable? N/A — this is not an approval mechanism.
8. Can tool result change authority? No — this is precisely designed so it cannot.
9. Rule location: `Platform` (OS-level), configured via project/user/managed settings.

**CLASSIFICATION: ADOPT** — with the fail-open-on-missing-dependency behavior flagged
as a specific configuration ARGON must not inherit by default (`sandbox.failIfUnavailable`
equivalent must default to fail-closed for ARGON, which is the opposite of this source's
own default).

---

## RP-4 — Consecutive-auto-approval circuit breaker

**SOURCE:** Cline, via DataCamp tutorial (`datacamp.com/tutorial/cline-ai`) and Cline's
own CLI docs. Exact claim supported: "The maximum requests setting acts as a safety net,
requiring your input after a certain number of consecutive automated actions." Accessed
2026-09-20. Evidence quality: `STRONG` for the feature's existence (corroborated across
two independent sources); the *exact* default threshold value was not found in the
excerpts retrieved, so that number is `UNKNOWN`.

**OBSERVED PATTERN:** a counter tracks cumulative auto-approved actions per session,
independent of each action's individual risk classification, forcing a stop when
exceeded.

**WHY IT WORKS:** it is the closest found real-world precedent for exactly the gap the
Wave 3.5 v2 reconciliation left open (approval laundering via many small steps) — a
blunt but *working, shipped* session-scoped counter.

**ARGON ADAPTATION:** `PROPOSAL` (already flagged as a candidate mechanism, not decided,
in the reconciliation document) — a Kernel-level counter of consecutive auto-approved
actions per task/task-chain; once a human-set threshold is hit, the next action is
downgraded to `REQUIRE HUMAN APPROVAL` regardless of its own tier.

**REJECT IF:** if the counter can be reset by starting a nominally "new" task that is
really a continuation, the control is defeated the same way it's meant to prevent —
laundering by segmentation, applied one level up (segmenting into separate *tasks*
instead of separate *actions*).

**TEST NEEDED:** exactly RT-13 from the prior reconciliation test list.

**9-question analysis:**
1. Prevents: unbounded runs of auto-approved actions without any human check-in.
2. Enforcement location: harness/session layer.
3. Enforcement class: `TOOL/HARNESS ENFORCED`.
4. Bypass path: task/session segmentation (C2 `INFERENCE`, not source-stated).
5. Human approval needed: yes, once threshold is hit.
6. Exact-action bound: no — this is a count, not a hash-bound approval.
7. Approval reusable across actions: this pattern exists specifically to *limit* that
   reuse, not to enable it.
8. Can tool result change authority: not described.
9. Rule location: `Runtime`/session layer.

**CLASSIFICATION: ADOPT**, explicitly as a *partial* mitigation only — it does not
solve cross-task laundering, per REJECT IF above.

> **CORRECTION PASS v1 — C2-X4 applied.** Confirmed already correct in the original
> artifact and restated explicitly, with no change in substance: this is `EXTERNAL
> PRECEDENT = PARTIAL` (one vendor, one shipped counter). It is **not** presented as a
> complete solution to approval laundering, does **not** prevent segmentation attacks
> that split across separate *tasks* rather than separate *actions within one task*
> (stated plainly in REJECT IF above), and does **not** substitute for exact-action-bound
> approval (RP-13) — it is a session-scoped circuit breaker only.

---

## RP-5 — Command-prefix precision with a documented wrapper-command blind spot

**SOURCE:** Claude Code permissions docs, same URL as RP-2/RP-3. Exact claim: rules like
`Bash(git push --force:*)` can gate specific command shapes; the same doc states plainly
that "Exec wrappers such as watch, setsid, ionice, and flock can't be auto-approved by a
prefix rule like Bash(watch *)" and that `find` with `-exec`/`-delete` is not covered by
a `Bash(find *)` rule. Accessed 2026-09-20. Evidence quality: `STRONG` (official docs,
self-disclosed limitation).

**OBSERVED PATTERN:** fine-grained prefix rules are more precise than category rules,
but the same official source documents their own blind spot for composite/wrapper
commands.

**ARGON ADAPTATION:** `PROPOSAL` — adopt prefix-style rules for Git/Shell, but never as
the sole control; must be paired with RP-3 (the sandbox layer is the actual backstop for
whatever a prefix rule misses).

**REJECT IF:** treated as sufficient alone — the source itself says it is not.

**TEST NEEDED:** a wrapper/composite command that functionally performs a denied action
must still be caught (expected to require RP-3, not RP-5, to catch it).

**9-question analysis:**
1. Prevents: broad categories of dangerous commands via named, specific patterns.
2. Enforcement location: permission-rule matcher (string/prefix matching).
3. Enforcement class: `TOOL/HARNESS ENFORCED`.
4. Bypass path: source-documented — wrapper commands, `find -exec`/`-delete`.
5. Human approval: yes, for `ask`-tier matches.
6. Exact-action bound: pattern-level, not payload-hash-level.
7. Reusable: yes, a saved prefix rule applies to every future matching command.
8. Tool result changing authority: not described.
9. Rule location: `Runtime` config.

**CLASSIFICATION: ADAPT** — adopt the shape, explicitly do not adopt reliance on it alone.

> **CORRECTION PASS v1 — C2-X3 applied.** RP-2/RP-5 (Claude Code's prefix rules) and
> RP-13 (HARP/AgentAck's exact-payload hash binding) must not be treated as the same
> mechanism at different rigor levels — they are two *different categories* per §6 of
> the Correction Pass shared vocabulary, and the source evidence for each is different
> strength. Stated explicitly, once, here (governs both RP-2/RP-5 and RP-13):
> - `EXTERNAL PRECEDENT = PARTIAL` — the sources reviewed (Cline, Claude Code) document
>   **Category/Prefix Approval** (a rule matches a *shape* of command, e.g.
>   `Bash(git push --force:*)`) with strong evidence. **They do not demonstrate Exact
>   Payload Binding** (approval cryptographically tied to the literal executable
>   payload) or Cryptographic Binding (signature/key-custody) at all — no claim to the
>   contrary appears anywhere in this document, and this line makes that boundary
>   explicit rather than implicit.
> - `ARGON EXACT-ACTION MODEL = PROPOSAL` — ARGON adopting exact-payload approval is a
>   design choice this research supports as worth proposing, not a conclusion the
>   external sources force.
> - `CRYPTOGRAPHIC HASH/SIGNATURE = NEEDS EXPERIMENT / INFRASTRUCTURE DECISION` — see
>   RP-13's corrected classification below, which this line is consistent with.

---

## RP-6 — Mandatory container isolation and structured trajectory recording

**SOURCE:** SWE-agent GitHub FAQ/docs (`github.com/princeton-nlp/SWE-agent`) and a
third-party technical summary (Vantaige, `vantaige.io/ai-tool/swe-agent`). Exact claims:
SWE-agent requires Docker for its execution environment ("Your only limitation might be
the availability of the docker containers"); parallel execution via SWE-ReX routes to
sandboxed backends (Docker/AWS/Modal/Fargate); "every run produces a structured
trajectory file suitable for research replay, fine-tuning, or auditing." Accessed
2026-09-20. Evidence quality: `STRONG` (official repo + independent technical summary).

**OBSERVED PATTERN:** (a) isolation is not optional/configurable-away for the agent's
main execution path; (b) every run's full action sequence is captured as a structured,
replayable artifact by default, not as an opt-in logging feature.

**ARGON ADAPTATION:** `PROPOSAL` — (a) reinforces RP-3/RP-9's "isolation must be
structural, not a Cloud choice"; (b) is directly adoptable for ARGON's Evidence layer —
every Cloud task should produce a structured, complete trajectory record by default
(tool calls, decisions, outcomes, in order), not a summary written after the fact by the
Cloud itself.

**REJECT IF:** n/a for the principle; feasibility of full trajectory capture at ARGON's
current stage is `UNKNOWN` (no runtime exists yet).

**TEST NEEDED:** confirm a trajectory file exists and is complete (no gaps) for a task
that included at least one denied/approval-gated action, not only for fully-successful
runs.

**9-question analysis:**
1. Prevents: unrecorded or selectively-recorded agent actions; environment escape into
   production.
2. Enforcement location: harness (mandatory Docker requirement) + trajectory-writer.
3. Enforcement class: `TOOL/HARNESS ENFORCED` for isolation; trajectory recording is
   also harness-level, not "OS/platform."
4. Bypass path: not discussed in sources reviewed (no reported vulnerability found for
   SWE-agent's own isolation, unlike OpenClaw in RP-10).
5. Human approval: SWE-agent's documented design is autonomous-by-default for its
   benchmark use case — no approval gate is described in the sources found. This is
   worth flagging: the source `does not` model human-in-the-loop approval at all, which
   is a gap relative to ARGON's Global Rule 18, not a pattern to adopt as-is.
6. Exact-action bound: trajectory records are per-action by construction.
7. Reusable: n/a.
8. Tool result changing authority: not described.
9. Rule location: `Runtime`/harness.

**CLASSIFICATION: ADOPT** (trajectory recording); **UNKNOWN** for isolation feasibility
in ARGON's current stage; explicitly noting the *absence* of human-approval modeling in
this source as something ARGON must add on top, not inherit.

---

## RP-7 — Auto-commit/dirty-commit defaults, and a documented real footgun

**SOURCE:** Aider official docs (`aider.chat/docs/git.html`, `aider.chat/docs/config/
options.html`) for the feature description, plus an independent security write-up
("Aider Bypasses Git Hooks Auto Commits By Default," theorydelta.com). Exact claims:
Aider auto-commits every successful edit by default (`auto-commits: true`); if the
working tree is dirty, Aider commits the pre-existing changes first, separately, before
its own edit ("dirty commits"), also on by default; commits skip pre-commit hooks by
default (`--no-verify`, i.e. `git-commit-verify: False` by default). The independent
write-up adds: this default bypasses any secret scanner or linter configured as a
pre-commit hook, and a project-committed `.aider.conf.yml` with `yes-always: true`
"silently removes all confirmation prompts for every developer who runs aider in that
directory — with no warning, no audit trail." Accessed 2026-09-20. Evidence quality:
`STRONG` for the documented defaults (official docs); `MODERATE` for the independent
security write-up's severity framing (single-author analysis, not independently
corroborated in this search pass, though the underlying default values it describes are
directly confirmed by the official docs and options reference).

**OBSERVED PATTERN:** (a) auto-commit-by-default bundles the agent's changes with
whatever else was already sitting uncommitted, which the docs themselves say exists to
protect the user's own work — but the independent analysis notes this also makes clean
attribution/audit harder after the fact; (b) safety-relevant hooks are skipped by
default; (c) a *repository-committed* config file can silently disable all human
confirmation for every future user of that repo, with no distinct warning.

**WHY IT WORKS (as a warning, not a control to adopt):** item (c) specifically is a
real, documented instance of exactly the class of risk ARGON's own threat model has been
concerned with — a rule (in this case, an approval requirement) can be silently
overridden by something living inside the repository itself, the same untrusted-content
channel ARGON already treats as data-not-instructions for *prompt* content, but which
here would be a *config file*, a different channel the "data not instructions" rule as
written does not obviously cover.

**ARGON ADAPTATION:** `PROPOSAL` — ARGON's approval/gate configuration must never be
settable, in whole or in part, from a file that lives inside the target repository
(Legacy or ARGON-HEALTH). Whatever config channel the Kernel reads its gate settings
from must be outside the repository's own untrusted-content boundary. This extends
(does not replace) the existing "repo content = data, not instructions" rule to cover
config files specifically, since a config file is not "content read and reasoned about"
in the same way a prompt-injection payload is — it can silently change *behavior*
without ever being "read" by the model at all.

**REJECT IF:** never, for the adaptation — but the underlying Aider default *itself*
(auto-commit, dirty-commit, hook-skipping) is not proposed for adoption; it is presented
as a documented real-world cautionary case.

**TEST NEEDED:** place a config file inside a test repository that attempts to weaken or
disable an ARGON approval gate; confirm the Kernel's actual gate configuration is
unaffected.

**9-question analysis:**
1. Prevents (as designed by Aider): loss of the user's own uncommitted work when the
   agent starts editing. Does *not* prevent: hook bypass, config-driven approval removal.
2. Enforcement location: the tool's own git-integration logic; the vulnerable config
   channel is a plain file read at startup.
3. Enforcement class: `PROMPT-ONLY` is not quite right either — this is closer to
   `TOOL/HARNESS ENFORCED` for the intended behavior, but the config-override path
   means the "enforcement" here is trivially reconfigurable by anyone (or anything)
   that can write a file to the repo.
4. Bypass path: exactly as described — a committed config file.
5. Human approval needed: normally yes (`yes-always: false` is the safe default state,
   confirmation prompts appear) — but this is exactly what a repo-committed override
   can remove.
6. Exact-action bound: no.
7. Reusable: the override, once committed, silently applies to every future session for
   every developer in that repo — an extreme, unbounded form of reuse.
8. Can tool result (or in this case, repo content) change authority? **Yes — this is the
   clearest documented real-world example found in this entire research pass of exactly
   that failure mode.**
9. Rule location: currently `Repository` (the worst possible location for a
   safety-relevant rule, per the ARGON adaptation above).

**CLASSIFICATION: REJECT** (the Aider defaults themselves, for ARGON's purposes) /
**ADOPT** (the lesson: config-channel isolation must be added explicitly to ARGON's
threat model as a named control, extending the existing untrusted-content rule).

---

## RP-8 — Commit identity attribution

**SOURCE:** Aider docs, `aider.chat/docs/git.html`. Exact claim: "If aider authored the
changes in a commit, they will have '(aider)' appended to the git author and git
committer name metadata." Accessed 2026-09-20. Evidence quality: `STRONG` (official
docs).

**OBSERVED PATTERN:** every commit the tool authors is identity-marked in standard git
metadata, distinguishing tool-authored from human-authored changes at the VCS level
itself, not in a separate log.

**ARGON ADAPTATION:** `PROPOSAL` — any commit an ARGON Cloud makes (on an isolated
branch, per the Wave 3.5 v2 tiering) should be similarly identity-marked (which Cloud,
which task ID) directly in commit metadata, not only in a separate Evidence Record — so
the two can be cross-checked against each other (an Evidence Record claiming a commit
happened should be verifiable against the commit's own attribution, not merely trusted).

**REJECT IF:** n/a.

**TEST NEEDED:** confirm a commit's git-metadata attribution and its corresponding
Evidence Record's claimed authorship match; flag a mismatch as evidence-integrity
failure (ties to RP-14).

**9-question analysis:**
1. Prevents: ambiguity about whether a human or the tool authored a given change.
2. Enforcement location: the tool's own commit-construction logic.
3. Enforcement class: `TOOL/HARNESS ENFORCED`.
4. Bypass path: not discussed in source; in principle, if the tool's commit logic is
   itself compromised, attribution could be forged the same way any git metadata can be
   forged (git metadata is not cryptographically signed by default).
5. Human approval: not directly related to this specific pattern.
6. Exact-action bound: yes, per-commit.
7. Reusable: n/a.
8. Tool result changing authority: not applicable.
9. Rule location: `Runtime`/tool logic.

**CLASSIFICATION: ADOPT**, with the noted caveat that plain git author/committer
metadata is not cryptographically verified — for anything higher-stakes than
attribution-for-review, RP-13's signed-approval pattern is the stronger version of this
same idea.

---

## RP-9 — Enforcement as a property of the deployment, not of the agent

**SOURCE:** OpenHands Enterprise documentation (`docs.openhands.dev/enterprise/
docker-in-sandbox.md`). Exact claim: the isolation runtime is selected by the platform
operator via a Kubernetes `RuntimeClass`; "the security boundary is a property of the
deployment—not something an agent or an end user can turn off." Network-access isolation
is likewise "built into the deployment and are not something you configure or manage"
at the agent level. Accessed 2026-09-20. Evidence quality: `STRONG` (official
enterprise docs).

**OBSERVED PATTERN:** the agent (and even the operator's own runtime request) has no
code path to alter the isolation configuration — it is fixed by infrastructure the
agent never touches.

**ARGON ADAPTATION:** `PROPOSAL` — any ARGON hard gate should be designed so the Cloud
issuing a request has zero path to self-approve or reconfigure the gate; gate
configuration should live in infrastructure the Kernel's own reasoning loop cannot
write to.

**REJECT IF:** feasibility depends on infrastructure ARGON does not yet have (Wave 4 not
started) — `REQUIRES HUMAN DECISION`/`UNKNOWN`, not something C2 can confirm is
achievable.

**TEST NEEDED:** confirm no Cloud has any tool call, config file, or code path available
to it that changes its own gate configuration.

**9-question analysis:**
1. Prevents: agent self-reconfiguration of its own security boundary.
2. Enforcement location: platform/orchestration layer (Kubernetes `RuntimeClass`),
   outside the agent process entirely.
3. Enforcement class: `OS/PLATFORM ENFORCED`.
4. Bypass path: none described in source for this specific guarantee (contrast RP-10,
   which is a *different* project's vulnerability, not OpenHands').
5. Human approval: this is an infrastructure-level guarantee, not a per-action approval
   flow — separate axis from human-in-the-loop approval.
6. Exact-action bound: no — this is boundary-level, not action-level.
7. Reusable/tool-result-changing authority: not applicable — that is precisely what this
   pattern is designed to make impossible.
8. (merged with 7 above per source's framing)
9. Rule location: `Platform`.

**CLASSIFICATION: ADOPT** as a design principle; implementation feasibility `UNKNOWN`.

---

## RP-10 — Sandbox-configuration injection as its own attack class

**SOURCE:** a published security analysis of the OpenClaw agent framework (arXiv,
`arxiv.org/pdf/2603.27517`), Section 5.7 ("Container Boundary & Host OS Interface").
Exact claim: sandbox configuration fields (Docker bind-mount paths, network mode,
seccomp/AppArmor profile) were passed through to the container runtime without
validation, so agent-controlled or config-store-writable input could mount the host's
Docker socket (`/var/run/docker.sock`) or set `network: "host"`, defeating the sandbox
and granting effective host control. Accessed 2026-09-20. Evidence quality: `STRONG`
(a specific, cited, published vulnerability analysis with source-code line references) —
but scoped to OpenClaw specifically, not a claim about Cline/Claude Code/OpenHands/
SWE-agent/Aider, none of which this vulnerability was found to apply to in sources
reviewed.

**OBSERVED PATTERN:** a sandbox is only as strong as the trust placed in *how it is
configured*; if the configuration path is reachable by the same untrusted channels the
sandbox exists to defend against, the sandbox is not a real boundary.

**ARGON ADAPTATION:** none proposed as a control — this is a **new candidate attack
class** for ARGON's threat model (raised, not adopted into the existing 16-class list
by C2 unilaterally — that decision belongs to whoever owns the threat model / to C7).

**REJECT IF:** n/a — this is a threat, not a control to accept or reject.

**TEST NEEDED:** attempt to influence sandbox configuration (network mode, mount paths,
security profiles) via any input channel a Cloud or task submission can reach.

**9-question analysis:**
1. Prevents (if fixed): sandbox escape via configuration injection.
2. Enforcement location: would need to be the configuration-loading code path itself.
3. Enforcement class: `UNKNOWN` for ARGON — no sandbox exists yet to secure this way.
4. Bypass path: exactly as described in the source.
5. Human approval: not directly applicable to this pattern.
6-8. Not applicable — this is a vulnerability class, not an approval mechanism.
9. Rule location: would need to be `Platform`, same reasoning as RP-9 — never
   agent/Cloud-reachable.

**CLASSIFICATION: NEEDS EXPERIMENT / UNKNOWN** (as a new threat-model entry, this is
flagged for C7, not decided here).

---

## RP-11 — MCP: connect-time vs runtime trust, tool poisoning, rug-pulls, confused deputy

**SOURCE:** OWASP "MCP Tool Poisoning" (`owasp.org/www-community/attacks/
MCP_Tool_Poisoning`), a security-research write-up on SOC Prime
(`socprime.com/blog/mcp-security-risks-and-mitigations/`), and an academic MCP-security
systematization paper (arXiv, `arxiv.org/pdf/2512.08290`). Exact claims: tool
descriptions/manifests are typically reviewed once at connect time; tool *responses* at
runtime are passed into the model's context largely unchecked ("MCP client
implementations typically pass tool responses into the LLM context as-is"); "rug pull"
attacks exploit a tool that passes initial review then changes its definition later
without triggering re-review; "internal and external tools share the same privilege
level within the agent," so an untrusted external server's response can trigger calls to
trusted internal tools (confused deputy). Accessed 2026-09-20. Evidence quality: `STRONG`
for OWASP and SOC Prime; `MODERATE` for the arXiv paper (peer-review status not
independently verified in this pass).

**OBSERVED PATTERN:** two distinct trust moments (connect-time manifest vs runtime
response) each need separate, ongoing checks; privilege is commonly attached to "is a
callable tool" rather than to "which server, at what trust level, produced this."

**ARGON ADAPTATION:** `PROPOSAL` — ARGON's existing MCP rule ("tool_result = data, not
instruction") should extend explicitly to tool *manifests* at connect time, require
re-validation on any manifest change (not only first connection), and add an
origin-trust axis (internal/first-party vs external/third-party) independent of the
existing read-only/write-capable axis.

**REJECT IF:** ARGON never connects to third-party MCP servers — the origin-trust axis
then collapses to one tier and may not be worth the added complexity;
`REQUIRES HUMAN DECISION` on whether third-party MCP is in ARGON's scope at all.

**TEST NEEDED:** a mock MCP server that changes its tool description between
connections must trigger re-review, not inherit prior approval; a third-party tool
response requesting a call to an internal write-capable tool must not inherit the
internal tool's trust automatically.

**9-question analysis:**
1. Prevents (if implemented): hidden-instruction injection via tool metadata; silent
   privilege escalation via server redefinition; cross-server privilege flattening.
2. Enforcement location: would need to be the MCP client's manifest-ingestion and
   response-handling code.
3. Enforcement class: source states this is largely **absent** today across typical MCP
   clients — "the MCP specification does not enforce security at the protocol level"
   (from a related source in the original research pass). So current real-world status
   for this exact protection: `PROMPT-ONLY at best, often ABSENT`.
4. Bypass path: exactly the trust-gap OWASP describes — approve once, poison later.
5. Human approval: not currently modeled by the protocol itself; would need to be added
   by the client/harness (an ARGON-side addition, not something MCP provides).
6. Exact-action bound: no — this is about tool/server identity and metadata, not
   individual calls.
7. Reusable: yes — that is exactly the rug-pull risk (a one-time approval treated as
   permanent trust).
8. Can tool result change authority? **Yes — this is the entire point of "tool
   poisoning": a response can carry instructions the agent then acts on with elevated
   effective authority.**
9. Rule location: would need to be `Adapter` (MCP-specific integration layer) plus
   `Kernel` (for the origin-trust policy itself).

**CLASSIFICATION: ADOPT**

---

## RP-12 — Secrets must never enter the agent's own context

**SOURCE:** SuperTokens engineering blog, "Secure AI agents with scoped tokens, DPoP,
tool-level policies, and human approvals" (`supertokens.com/blog/auth-for-ai-agents`).
Exact claim: "API keys, database credentials, and tokens must never appear in the
agent's context window. The correct pattern is: the agent calls a tool; the tool server
fetches the secret from a vault and uses it server-side. The agent receives only the
result." Accessed 2026-09-20. Evidence quality: `MODERATE` — a single vendor engineering
blog, not a standards body or widely-cited paper; the underlying principle (secrets
should not be model-visible) is broadly consistent with general secrets-management
practice but this specific source is not independently corroborated in this pass.

**OBSERVED PATTERN:** a proactive architecture (secrets never enter the context at all)
rather than a reactive one (scan outputs for secret-shaped strings before they're
written anywhere, which is what ARGON's own prior design proposed).

**ARGON ADAPTATION:** `PROPOSAL` — where ARGON tasks require credentialed access to
anything, the credential should be resolved and used server-side by the tool/adapter,
never placed in the Cloud's own context/prompt. This is a stronger, structurally
different control than ARGON's existing "don't write secrets to logs" rule (which
assumes the secret is already in context and tries to stop it leaking *out* — this
pattern stops it entering in the *first place*).

**REJECT IF:** a task genuinely requires the Cloud to reason *about* a secret's
existence or rotation status (not its value) — the adaptation should distinguish
"secret value" from "metadata about a secret," which this source does not address.

**TEST NEEDED:** confirm no credential value ever appears in a Cloud's context/prompt
log, even transiently, for any tool call requiring authenticated access.

**9-question analysis:**
1. Prevents: secret exposure via model context, logs, or Evidence Records.
2. Enforcement location: tool/adapter layer, server-side vault resolution.
3. Enforcement class: `TOOL/HARNESS ENFORCED` (would need to be, for ARGON — not
   currently designed this way).
4. Bypass path: not discussed in source; in principle, a tool that fetches a secret and
   then *echoes* it back in its result to the agent would defeat this pattern — the
   source does not address result-sanitization on the way back.
5. Human approval: not directly addressed.
6-7. Not directly applicable.
8. Tool result changing authority: not the focus of this source, but the bypass path
   above (echoing a secret in a result) would be exactly this failure mode.
9. Rule location: `Adapter`.

**CLASSIFICATION: ADOPT**

---

## RP-13 — Cryptographic action-binding: hash, scope, expiry, nonce, and audit schema

**SOURCE (mixed, all `EMERGING/LOW-ADOPTION EVIDENCE` — stated once, applies to this
whole pattern):** (a) a GitHub sample repo for a small protocol called HARP
(`github.com/harp-protocol/samples`) showing an approval object with fields
`artifactHash`, `scope: "once"`, `expiresAt`, `nonce`, `signerKeyId`, `signature`, and a
documented test scenario "Replay detection — Run enforcer twice; nonce journal blocks
reuse." (b) SuperTokens blog (same as RP-12), which additionally states: "Every approval
or denial must be stored with: agent ID, tenant ID, action, resource, a hash of the
input parameters, the approver identity, and a timestamp." (c) a PyPI tool, AgentAck
(`pypi.org/project/agentack/`), whose stated purpose is testing whether "agent actions
remain bound to what a human approved" — its demo output includes a specific detected
case: "Action changed after approval DETECTED (ACK003)." Accessed 2026-09-20. **None of
these three sources are an established standard; they are included because no stronger
source addressing exact-action authorization was found across the assigned research
scope (OpenHands/Cline/SWE-agent/Aider/Agentless do not publish this kind of model).**

**OBSERVED PATTERN:** an approval is cryptographically bound to a hash of the *exact*
proposed action (not a category), carries a scope (e.g. single-use), an expiry, a nonce
to block replay, and a signed approver identity — and independent tooling exists whose
specific purpose is detecting the case where an approved action is silently swapped for
a different one before execution.

**WHY IT WORKS:** this is the direct, structural answer to "can approval be reused for a
different action" (question 7 in this brief's own required analysis) — by construction,
a hash mismatch invalidates the approval.

**ARGON ADAPTATION:** `PROPOSAL`, explicitly the strongest and most specific answer
found in this research pass to ARGON's own open question (carried from Wave 3.5 v2, §4)
of "what satisfies REQUIRE_REVIEW/REQUIRE_HUMAN_APPROVAL, and can it be laundered" —
propose that any ARGON `REQUIRE HUMAN APPROVAL` decision be bound to a hash of the exact
action payload, scoped to single-use, time-bounded, and that the Evidence/Audit record
store the approver identity and parameter hash together (matching the SuperTokens field
list almost exactly).

**REJECT IF:** ARGON's Wave 4 Kernel cannot support cryptographic signing/verification
at all — in which case this degrades to "approval is recorded but not cryptographically
bound," which is a materially weaker (though still better than nothing) position that
must be stated honestly, not silently assumed away.

**TEST NEEDED:** the AgentAck-style test directly: approve action A, substitute action B
before execution, confirm the mismatch is detected and execution is blocked — not merely
logged after the fact.

**9-question analysis:**
1. Prevents: approval reuse across a different action than the one actually approved;
   replay of a captured approval token.
2. Enforcement location: would need to be the execution layer, checking the hash
   immediately before running the action.
3. Enforcement class: if implemented as described, `RUNTIME ENFORCED` (the verification
   happens at the moment of execution, not only at approval time).
4. Bypass path: none described for the core mechanism in these sources; a real
   implementation risk not addressed by any of the three sources is *where* the signing
   key is held (see RP-14 — this is exactly the self-attestation-vs-independent-verifier
   question, applied to the approval act itself, not just the evidence-of-completion
   act).
5. Human approval: this entire pattern exists to make human approval exact-action-bound.
6. Exact-action bound: **yes — this is the pattern's entire purpose.**
7. Reusable across a different action: **no, by design** — hash mismatch invalidates it.
8. Can tool result change authority: not directly addressed by these sources (they
   address the approval-to-execution gap, not the tool-output-to-context gap, which is
   RP-11's territory).
9. Rule location: `Runtime` for verification, `Kernel` for policy (what requires this
   binding), possibly `Platform` for key custody (unresolved, see RP-14).

**CLASSIFICATION (CORRECTED, Correction Pass v1, C2-RP13): `NEEDS EXPERIMENT`** — the
original artifact classified this `ADOPT`, which overstated it. `ADOPT` is withdrawn.
The underlying sources (HARP samples, AgentAck, one vendor blog) are
`weak/emerging evidence`, not established industry practice, and this document must not
present the *architectural direction* as more settled than that evidence supports. Six
specific sub-questions remain open and are listed explicitly, per the correction, rather
than folded into a single vague "infrastructure decision" line:
1. **Key custody** — who/what holds the signing key; RP-14's self-attestation question
   applies directly here (does the approver's own process hold its own key?).
2. **Identity binding** — plain metadata (RP-8, weak) vs signed `signerKeyId` (RP-13,
   stronger but unproven at ARGON's scale).
3. **Replay prevention** — nonce-journal mechanism described in the source sample; never
   verified against ARGON's own task/session model.
4. **Expiry** — source TTL figures (seconds-scale, token-oriented) do not obviously map
   to ARGON task durations (likely much longer); unresolved, not merely undecided.
5. **Revocation** — the AIP source itself discloses "no revocation infrastructure" in
   its current version; this is an open problem in the field, not just for ARGON.
6. **Exact payload binding** — the one sub-mechanism with the clearest source support
   (`artifactHash` matching), still `PROPOSAL`-level for ARGON, not `CONFIRMED`.

`REQUIRES HUMAN DECISION`: whether ARGON invests in building this level of rigor at all,
versus a simpler (and weaker) approval-record model — this was already flagged in the
original artifact and remains unresolved, now explicitly tied to the six points above
rather than stated as one general caveat.

---

## RP-14 — Evidence trust tiers and the self-attestation problem

**SOURCE (three, of differing standing — stated per-source):** (a) a dev.to post,
"Mediator Receipts: The Question to Ask About Agent Attestation"
(`dev.to/luckypipewrench/...`), evidence quality `LOW/EMERGING` (individual blog post),
which proposes a three-tier taxonomy: self-attestation (agent process holds the signing
key — "in-process is fine" for internal debugging only), deployment-internal attestation
(the runtime, separate from the agent process but inside the same operator's trust
boundary, holds the key — "stronger than self-attestation, weaker than independent"),
and independent third-party witness (an entity outside the operator's deployment
entirely holds the key). (b) an arXiv paper on hardware-rooted attestation composing
IETF RATS with agent evidence (`arxiv.org/html/2608.00801v1`), evidence quality
`MODERATE` (arXiv, peer-review status unverified, but it cites and correctly describes
the real IETF RATS architecture, which is itself a standards-track effort), stating: "In
a self-report, [Verifier and Relying Party] collapse into the same software stack. RATS
pulls them apart" — the Attester (holds the claim), Verifier (decides whether to
believe it), and Relying Party (acts on the verdict) are architecturally distinct roles.
(c) an arXiv paper on an "Agent Identity Protocol" (`arxiv.org/pdf/2603.24775`), evidence
quality `MODERATE` (arXiv, unverified peer-review), which cites the authors' own prior
work: "self-claimed quality systematically selects the worst delegates, reinforcing the
need for independent verification" (the "Provenance Paradox"), and separately discloses
its own protocol's limitation: "A dishonest agent can misrepresent its result hash or
cost without detection by the cryptographic layer alone" when counter-signing/third-party
attestation is not enforced. Accessed 2026-09-20.

**OBSERVED PATTERN:** across all three sources, independently, the same structural point
recurs — a system where the party making a claim and the party verifying it are the same
software stack cannot be trusted to the same degree as one where they are architecturally
separated, and at least one source presents this not as a theoretical concern but as an
empirical finding (self-claimed quality favoring the *worst* delegates, not merely being
unreliable).

**ARGON ADAPTATION:** `PROPOSAL` — this maps directly onto ARGON's own confirmed gap
(threat model Attack Class 12, "Evidence Spoofing," and the Wave-3.5-v2-carried open
question on whether Evidence-Store `VERIFIED` claims need a formal hard gate). The
adaptation: a Cloud writing its own Evidence Record claiming `VERIFIED`/`COMPLETE`
status is structurally a self-attestation (weakest tier, per source (a)) — ARGON's
existing design already has a partial answer to this in the "C6 does not self-certify,
C7 is independent" rule from Wave 3.5 C1/C6 work, which is architecturally the same
Verifier/Relying-Party split RATS describes, applied without having cited RATS
explicitly. This document surfaces that ARGON's own prior design already independently
arrived at a version of this pattern — worth noting to C1/C7 as convergent validation,
not a new idea to bolt on.

**REJECT IF:** none of the three sources' specific cryptographic mechanisms (TPM-based
attestation, the specific AIP token format) are proposed for adoption — only the
architectural *principle* (claim-maker ≠ verifier ≠ relying party) is proposed, at the
evidence quality these sources actually support, which is `MODERATE` at best.

**TEST NEEDED:** confirm no Cloud's own Evidence Record, unaccompanied by an independent
(C6/C7) verification record, is ever sufficient on its own to change a task's status to
`VERIFIED` or `COMPLETE`.

**9-question analysis (for the evidence-store trust model generally):**
1. Prevents: a Cloud's self-report being mistaken for independent confirmation.
2. Enforcement location: would need to be wherever ARGON's Kernel/Router reads status —
   it must distinguish claim-source from verification-source.
3. Enforcement class: currently `UNKNOWN` for ARGON (per the Wave 3.5 self-audit, this
   entire area was a confirmed gap before this document).
4. Bypass path: exactly the Provenance Paradox finding — if self-report is ever treated
   as sufficient, the system structurally favors whichever Cloud/agent is least honest
   about its own quality.
5. Human approval: relevant for the `VERIFIED`/`PRODUCTION` transition specifically,
   per the still-open Wave 3.5 v2 question.
6-7. Not directly applicable at this level (this is about record trust, not action
   approval).
8. Can tool result change authority: adjacent concern, not the same mechanism — a
   forged/self-authored Evidence Record is the analogous risk one layer up from a
   poisoned tool result.
9. Rule location: `Kernel` (the status-transition logic must enforce the separation) and
   `Runtime` (Evidence Store itself must record claim-source distinctly from
   verification-source).

**CLASSIFICATION: ADOPT** (the architectural principle); specific cryptographic
mechanisms from sources (a)-(c) = `UNKNOWN/NEEDS EXPERIMENT` given their evidence
quality.

---

## APPROVAL AUTHORITY MODEL (independent section, per requirement — no final decision made)

Extracted patterns only, not a decision:

- **Exact-action authorization:** RP-13 — approval bound to a hash of the specific
  action/payload, not a category. `PROPOSAL`, weak-sourced.
- **Approval scope:** RP-13's sample shows `"scope": "once"` as one option; RP-2 shows
  Claude Code's opposite choice (a category-level rule that persists and covers many
  future matching commands). **These are two different, both-real, competing patterns**
  — ARGON has not chosen between "narrow, single-use approval" and "broad, persisted,
  category approval," and this document does not choose for it. `REQUIRES HUMAN
  DECISION`.
- **Approval expiry:** RP-13 shows `expiresAt` timestamps and short TTLs recommended
  generally (60–300 seconds, per the SuperTokens source, for *token* expiry
  specifically — not necessarily the same as an approval-decision expiry, which these
  sources do not clearly distinguish). `UNKNOWN` how this maps to ARGON's task
  timescales, which may be much longer than a token TTL.
- **Revocation:** the AIP source (RP-14's source (c)) discloses its own protocol has
  "no revocation infrastructure" in its current version, relying on short-lived tokens
  instead — i.e., even a source proposing strong cryptographic binding admits
  revocation is unsolved in practice. This is presented as a known limitation across the
  field, not something ARGON should assume is easy.
- **Identity binding:** RP-8 (plain git attribution, weak) vs RP-13 (signed
  `signerKeyId`, strong) — two different strengths of the same underlying idea, at very
  different implementation cost.
- **Action hash/payload binding:** RP-13, core mechanism.
- **Human-in-the-loop controls:** SuperTokens source (RP-12/13) additionally describes
  "inline approve/deny" (push notification, single-click decision) and "time-boxed
  holds" (if no approval arrives within N minutes, the agent abandons the task) as
  UX-level patterns — relevant to C5's territory, noted here only because they appeared
  in a security-focused source, not proposed as C2's own design.

**What needs experiment or governance decision (explicit, not resolved here):**
1. Narrow single-use vs broad persisted approval scope — a real, unresolved tradeoff.
2. Whether ARGON's Kernel can support cryptographic action-hash binding at all (Wave 4
   feasibility question).
3. Approval expiry timescale appropriate to ARGON's task durations (likely much longer
   than the 60–300s token-TTL figures found, which are for a different kind of token).
4. Revocation mechanism — genuinely unsolved even in the sources reviewed here.
5. Where signing keys (if adopted) would be held — this is precisely the RP-14
   self-attestation-vs-independent-verifier question, applied to the *approval* act.

---

## POLICY PRECEDENCE — what sources actually show vs what is proposed

**No source reviewed defines a named four-way `ALLOW`/`REQUIRE REVIEW`/
`REQUIRE HUMAN APPROVAL`/`DENY` precedence model exactly as ARGON uses those four labels.**
What sources actually show:

- Cline and Claude Code both use a **three**-way vocabulary (roughly: allow/auto-approve,
  ask, deny), not four — `REQUIRE REVIEW` as ARGON defines it (a *different* tier from
  `REQUIRE HUMAN APPROVAL`) does not appear as a distinct concept in either source. This
  is `OBSERVED`, not `INFERENCE`: ARGON's four-tier model is more granular than either
  reference system's actual shipped design.
- Claude Code (RP-3) shows a real, sourced **precedence relationship between two
  different kinds of rule**: sandbox boundary restrictions "still apply even if" the
  permission-layer decision is compromised — i.e., sourced evidence that an
  environment-level restriction should be evaluated as *always active*, independent of
  and not overridable by, whatever the permission/approval layer decides. This is the
  one genuine, sourced precedence fact found: **environment-level restriction >
  permission-layer decision**, in the specific sense that the former bounds the latter's
  blast radius regardless of outcome.
- Beyond that one fact, any four-way precedence table for ARGON specifically —
  including the one already drafted in `C2-WAVE3.5-SECURITY-RECONCILIATION-v2.md`
  (outbound-content rule beats inbound-allowlist rule, etc.) — remains exactly what it
  was labeled there: `PROPOSAL`, not something derived from these sources. This document
  does not add new precedence claims beyond the one sourced fact stated above.

---

## EVIDENCE STORE — patterns found, explicitly not claimed to exist in ARGON

Per instruction, restated plainly: **none of the patterns below exist in ARGON today.**
ARGON's own Wave 3.5 self-audit already confirmed this area was a total gap before this
document. What follows are patterns *found in research*, offered for future
consideration:

- Verifier/Attester/Relying-Party architectural separation (RP-14, source (b), IETF
  RATS-derived).
- Self-attestation / deployment-internal / independent-witness trust tiers (RP-14,
  source (a)).
- The empirical Provenance Paradox finding — self-claimed quality selects for the worst
  delegates (RP-14, source (c)).
- Action-hash-bound, signed, nonce-replay-resistant approval records as a *component*
  of evidence integrity, extended from RP-13 to evidence-of-completion, not only
  evidence-of-approval.
- Structured, complete trajectory recording as a default, not opt-in, artifact (RP-6).

None of these are claimed to be "the ARGON evidence model." They are candidate inputs
for whoever (C1, C3, C6, or the human owner) next revises ARGON's Evidence Record design.

---

## MANDATORY SECURITY TEST MATRIX (consolidated across all 14 patterns)

| Pattern | Attack/Failure Case | Enforcement Point | Negative Test | Bypass Test | Human-Authority Implication | Portability Implication |
|---|---|---|---|---|---|---|
| RP-1 | Write occurs while nominally in Plan state | Tool registration | Attempt write call in PLAN; expect hard failure | Check for any harness bug exposing write tools in PLAN | None — mode toggle stays human-controlled | Model-agnostic; depends on harness, not model |
| RP-2 | Persisted rule silently misapplies across worktrees | Config resolution | Verify a worktree-A rule doesn't leak to worktree-B | Modify/inject the settings file directly | Persistence reduces re-prompting; risk if persistence itself is compromised | Model-agnostic |
| RP-3 | Approval-flow bypass still allows unrestricted reach | OS kernel (bubblewrap/Seatbelt-equivalent) | Simulate approval bypass, confirm sandbox still holds | Sandbox-dependency-missing fail-open path | Independent of human approval — a floor beneath it | Depends on OS-level primitives; least portable pattern found |
| RP-4 | Many small approved actions reconstruct one denied action | Session/task counter | RT-13 (carried) | Split across multiple nominal "tasks" | Forces a check-in; does not eliminate laundering | Model-agnostic |
| RP-5 | Wrapper/composite command evades prefix rule | Rule matcher | Test `find -exec`-equivalent evasion | Any command shape not covered by existing prefixes | None directly — feeds into RP-3 as backstop | Model-agnostic |
| RP-6 | Task with a denied action produces an incomplete trajectory | Harness trajectory writer | Confirm trajectory completeness including denied/gated actions | Compare trajectory to Kernel's own decision log for gaps | Trajectory ≠ approval; source has no approval gate to test | Model-agnostic |
| RP-7 | Repo-committed config disables approval prompts | Config file read at startup | Place adversarial config in test repo, confirm no effect on Kernel gates | Confirm config channel is fully outside repo trust boundary | Direct — this is the exact failure mode of authority being silently removed | Model-agnostic |
| RP-8 | Commit attribution forged | Commit-construction logic | Cross-check commit metadata against Evidence Record | Attempt a commit bypassing the tool's own attribution logic | Attribution supports, doesn't replace, review | Model-agnostic |
| RP-9 | Agent alters its own isolation config | Platform/orchestration layer | Confirm zero Cloud-reachable config path exists | Attempt any indirect reconfiguration route | Strongest — removes agent's own lever entirely | Least portable; depends on ARGON's own infrastructure choice |
| RP-10 | Sandbox config injected via untrusted input | Config-loading code | Attempt to set network/mount params via task input | Any indirect channel (env var, file, MCP param) | Would defeat every other control in this document if unaddressed | Model-agnostic (infrastructure-layer risk) |
| RP-11 | Tool manifest changes post-approval (rug pull) | MCP client ingestion | Mock server redefinition test | Response-embedded instruction test | MCP provides none of this by default — must be added | Depends on ARGON's own MCP client/adapter, not the model |
| RP-12 | Secret value echoed back in a tool result | Tool/adapter response path | Confirm no credential value in any context/log | Attempt to induce a tool to return a fetched secret | Not directly approval-related | Model-agnostic |
| RP-13 | Approved action A swapped for action B before execution | Execution-time hash check | AgentAck-style substitution test | Key-custody compromise (who holds the signing key) | Core mechanism is entirely about exact human-authority binding | Model-agnostic; weak-evidence pattern |
| RP-14 | Cloud's self-report accepted as independent verification | Status-transition logic | Confirm no `VERIFIED` transition from a single Cloud's own claim alone | Attempt to have C6/C7 roles collapse into the reporting Cloud | Central to the entire multi-Cloud evidence model's integrity | Model-agnostic |

---

## EXPLICIT NON-CLAIMS

- No claim ARGON is secure, production-ready, fully secure, or zero-risk anywhere in
  this document.
- No claim any pattern above currently exists in ARGON.
- No final human/governance decision made — all `REQUIRES HUMAN DECISION` items are
  listed, not resolved.
- Wave 3.5 is not reopened; open items from it are referenced, not re-decided.
- Every `OBSERVED PATTERN` above traces to a stated public source, URL, section, and
  access date; where a source's evidence quality is weak, that is stated explicitly
  rather than presented at face value.

---

# APPENDIX — CLOUD CAPABILITY UPGRADE

Added per the Common Cloud Evolution Super-Prompt, applied retroactively to this
already-delivered artifact rather than producing a needless second file. This appendix
is an honest self-audit against that document's §28 challenge, not a restatement of the
body above.

## 1. Sources Studied (actually opened, not assumed)

Cline, Claude Code, OpenHands (incl. Enterprise docs), SWE-agent, Aider, OWASP MCP Tool
Poisoning, SOC Prime MCP write-up, one MCP-security arXiv paper, HARP protocol samples,
AgentAck, SuperTokens auth-for-agents blog, one Mediator-Receipts dev.to post, one IETF
RATS-composition arXiv paper, one AIP arXiv paper, one OpenClaw security analysis.

**Honest gap against this Super-Prompt's own §19 C2 priority list:** Roo Code (tool
groups/modes), OpenAI Agents SDK (guardrails), Goose (extensions/tools), SWE-ReX
(sandbox specifically), PydanticAI (tool boundaries), and LangGraph
(human-interruption/durability) are all named as C2-priority sources and **none of them
were opened in this research pass.** Per this same document's own rule ("لا تقل studied
إذا لم تُفتح المصدر فعليًا"), they are not claimed as studied and are not represented
anywhere in the body above. This is a scope gap for the next C2 research pass, not
something silently patched over here.

## 2. High-Value Patterns

RP-3 (OS-level sandbox independent of model judgment) and RP-9 (enforcement as a
deployment property the agent cannot reach) are the two strongest — both directly
answer the "policy vs enforcement" gap that persisted across every earlier C2 document
in this conversation. RP-13 (action-hash binding) and RP-14 (Verifier/Attester/Relying-
Party separation) are the most *structurally* important, despite weaker sourcing,
because they name the exact mechanism ARGON's own evidence model needs.

## 3. Patterns Rejected

Full autonomous/headless auto-approval (Cline's YOLO mode) and host-Docker-socket/
privileged-sandbox mounting — both rejected outright, both with a named source and a
stated reason (contradicts Global Rule 18; documented severe attack vector,
respectively) — carried from the earlier version of this artifact.

## 4. Token Efficiency Gains

**Honest self-audit finding, stated plainly rather than smoothed over:** this research
pass did **not** apply the Retrieve→Rank→Compress→Verify discipline this Super-Prompt
now mandates. Searches were run roughly one-per-topic without an explicit
information-gain gate (§22) deciding in advance whether each one was worth its cost, and
without an early-stopping check (§7.8) before moving to the next topic. No token ledger
(§7.1) was tracked. This is a real gap against the new standard, not a claim that the
prior process already met it. Going forward, C2's research should scout (README/docs
level) before committing to a full search, and should stop adding sources once
additional evidence stops changing the classification of a given pattern.

## 5. Model Portability

Nearly every adopted mechanism (RP-1, RP-2, RP-3's *principle*, RP-4, RP-5's principle,
RP-6, RP-7's lesson, RP-8, RP-9's principle, RP-11, RP-12, RP-14) is model-independent
by construction — each lives at the harness/OS/protocol layer, not in model-specific
prompting. RP-13 is excluded from this "adopted" list after Correction Pass v1
(downgraded `ADOPT` → `NEEDS EXPERIMENT`, §RP-13 above); the *architectural principle*
it proposes would still be model-independent if pursued, but it is no longer listed here
as something already classified for adoption. The one place a vendor-specific *implementation* was cited
alongside a portable *mechanism* is RP-3: bubblewrap/Seatbelt are Claude Code's own
tooling choices, not the general principle. This document already distinguished the two
in RP-3's own text; flagged here explicitly per this Super-Prompt's Section 14
(Model-Independent vs Model Adapter) — the sandbox *principle* is Kernel-level, the
specific *sandboxing technology* is Adapter/infrastructure-level and must not leak into
ARGON's Kernel design as if it were universal.

## 6. Failure Modes

Already documented per-pattern in the body: RP-3's fail-open-on-missing-dependency
default, RP-5's wrapper-command blind spot, RP-7's config-channel override (the
strongest real-world failure mode found in the whole document), RP-10's
sandbox-configuration-injection class, RP-11's connect-time/runtime trust gap, RP-13's
unresolved key-custody question, RP-14's self-attestation/Provenance-Paradox finding.

## 7. Experiments

Consolidated in the Mandatory Security Test Matrix table above; no new experiments added
in this appendix beyond what the body already specifies, per the anti-duplication rule
in this Super-Prompt (§7.6/§28).

## 8. Transferable Principles

(a) A permission decision and an environment-level restriction are two different layers
and must both exist independently. (b) Enforcement configuration must live outside any
path the enforced party can reach. (c) An approval is only as strong as its binding to
the exact action it covers. (d) A claim of completion/verification is structurally
weaker when the claimant and the verifier are the same process. (e) A sandbox's own
configuration channel is itself an attack surface, not a neutral setup step. (f) A
repository's untrusted-content boundary must extend to configuration files, not only to
content the model reasons over.

**Self-challenge record (§28), answered honestly rather than assumed passing:**
EVIDENCE — mostly yes, with evidence-quality tiers stated. TRANSFER — yes for RP-3, not
rigorously separated for every other pattern. TOKEN — **no, this is the weakest area**,
per §4 above. DUPLICATION — this artifact explicitly supersedes a weaker prior version
rather than sitting alongside it. QUALITY — density increased over the superseded
version. FAILURE — stated per-pattern. TEST — yes, per pattern and consolidated.
PORTABILITY — addressed in §5 above. SECURITY — bypass paths stated where sources
disclosed them. HUMAN — no human decision was made on C2's behalf anywhere. HONESTY —
`UNKNOWN`/evidence-quality caveats used throughout rather than upgraded to fact. SCOPE —
stayed within security research; did not decide architecture, data, or product
questions belonging to other Clouds.

---

## C7 v3 FINDING MATRIX

**Caveat repeated once more, not to be missed:** `C7-CLOUD-EVOLUTION-FINAL-AUDIT.v3`
was never produced or shown to this Cloud in this conversation, across either
correction pass. The finding IDs below are the C2 items enumerated directly inside the
Correction Pass v1 / Final Correction Pass v4 documents themselves — the only findings
this Cloud has actually seen. Status values are restricted to the Final Pass v4 §2
vocabulary: `FIXED` / `REFRAMED` / `DOWNGRADED` / `UNKNOWN` / `NEEDS EXPERIMENT` /
`DISPUTED — EVIDENCE PROVIDED`. No finding was disputed — none of the five required a
factual disagreement, only a correction.

| Finding | Status | What changed | Evidence |
|---|---|---|---|
| C2-RP1/X1 | REFRAMED | RP-1 split into `PUBLIC PRECEDENT` (Cline-specific, file-write only) vs `ARGON CONTROL REQUIREMENT` (ARGON's own "no mutation-capable path" proposal, terminology aligned to v4 §4); test scope widened to the exact 5-item list in v4 §11 X1 | Cline docs (unchanged citation, RP-1 header); the widened test list itself is `ARGON PROPOSAL`, not sourced from a vendor |
| C2-X3 | FIXED | Explicit three-way classification added and applied consistently to RP-2/RP-5 vs RP-13: `EXTERNAL PRECEDENT = PARTIAL`, `ARGON EXACT-ACTION MODEL = PROPOSAL`, `CRYPTOGRAPHIC HASH/SIGNATURE = NEEDS EXPERIMENT` | Claude Code prefix-rule docs (RP-2/RP-5, unchanged) vs HARP/AgentAck (RP-13, unchanged) — the fix is the added separation, not new sourcing |
| C2-X4 | FIXED | Confirmed the original RP-4 text already stated the laundering/segmentation limitation correctly; restated in the exact wording this correction specifies ("partial mitigation only") rather than left as looser prose | Cline auto-approve docs (unchanged citation) |
| C2-D6 | FIXED | Manifest rewritten to the exact required schema; `report_sha256` is a real, freshly computed value in both passes, never `TO_BE_COMPUTED`; the `.md` body now carries `report_sha256: recorded_in_manifest` per the v4 Hash Contract instead of any inline value | Computed via `sha256sum` on the final file bytes, recorded in the sibling manifest |
| C2-RP13 | DOWNGRADED | Classification changed from `ADOPT` to `NEEDS EXPERIMENT`; six sub-questions (key custody, identity binding, replay prevention, expiry, revocation, exact payload binding) enumerated individually instead of one general caveat; the capability-upgrade appendix's model-portability list corrected to remove RP-13 from the "adopted" set | HARP samples, AgentAck, one vendor blog — all still `EMERGING/LOW-ADOPTION EVIDENCE`, unchanged; only the classification changed |
| (`C7-CLOUD-EVOLUTION-FINAL-AUDIT.v3` itself) | `UNKNOWN` | Not addressed — the file does not exist in this Cloud's context in either correction pass | No evidence available; disclosed at the top of this document rather than assumed resolved |

### Deliverable #5 — short list of what remains UNKNOWN / NEEDS EXPERIMENT

- Full Plan/Act structural enforcement across all 5 test-scope items (RP-1) —
  `NEEDS EXPERIMENT`
- Cryptographic action-binding: all six sub-questions (RP-13) — `NEEDS EXPERIMENT`
- Sandbox-configuration-injection as a new threat-model entry (RP-10) — `NEEDS
  EXPERIMENT` (not yet adopted into the canonical 16-class threat model by anyone)
- Whether third-party MCP servers are in ARGON's scope (RP-11 adoption gate) —
  `UNKNOWN`
- Approval-scope tradeoff, narrow single-use vs broad persisted (RP-2 vs RP-13) —
  `REQUIRES HUMAN DECISION`, carried unchanged
- Six named C2-priority sources never opened (Roo Code, OpenAI Agents SDK, Goose,
  SWE-ReX, PydanticAI, LangGraph) — `UNKNOWN` / coverage gap, carried unchanged
- Token-economy research discipline (Retrieve/Rank/Compress/Verify) was not applied to
  this research pass — `UNKNOWN` whether findings would change under that discipline,
  carried unchanged
- Whether `C7-CLOUD-EVOLUTION-FINAL-AUDIT.v3` contains findings beyond the five
  addressed here — `UNKNOWN`, disclosed, not resolvable by this Cloud
