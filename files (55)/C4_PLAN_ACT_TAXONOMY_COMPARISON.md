# C4 — Plan/Act Mutation Taxonomy Comparison (2026-11-05)

**Identity:** C4 (session-only charter; not persisted to memory). **Mode:** read-only. **This document does not choose 5, 6 or 7 and does not close H-09 / OQ-03 / G-1.** Labels: VERIFIED · SOURCE-ASSERTED · INFERRED · UNKNOWN · NOT RECOVERED.

## 1. Sources, each with its own count and its own unit

| # | Source (artifact, location) | Count as the source states it | Unit the source uses | Class |
|---|---|---|---|---|
| S1 | C1 Experiment E2 (C1 file not supplied; known via C4 reading, `c2-c6.TXT` L1019–L1030, and synthesis §11) | **five** "attack vectors"; "expanded from four to five" (C4 recorded as C1 L293–L294) | vector | SOURCE-ASSERTED (C1 original not supplied) |
| S2 | C2 RP-1 (C4 recorded L188–L196; C2 pack L289) | **five** "items"/"routes", same list as S1 | item / route | SOURCE-ASSERTED |
| S3 | C2 consolidated test-matrix row for RP-1 (`c2-c6.TXT` L1003, L1059) | **one** (only the direct-write negative test) — C2's own internal inconsistency, recorded not fixed | test row | VERIFIED (text in the supplied TXT) |
| S4 | C4 Pattern F (C4 research; C4 L312–L329 per C4 matrix) | **five** lettered attempts (a)–(e); prose list has a different order (shell, interpreter, indirect file mutation, wrapper) | attempt / bullet | SOURCE-ASSERTED (C4 research file not re-read this run) |
| S5 | C7-FFA-003 Gate 4 | "identical **five** vectors" for C1 E2 and C2 RP-1; C4's "fifth" differs | vector | SOURCE-ASSERTED; C4's check of it VERIFIED in `c2-c6.TXT` L1021–L1027 (divergence is C4 items (d) and (e), not one swapped fifth) |
| S6 | Synthesis v2.1.1/v2.1.2, §11: `MV-01…MV-06` | **six** surfaces — a **proposal**; H-09 asks whether to accept six or keep five plus a C4 supplement; G-1 NOT MET | surface | VERIFIED (text read in `rar2/…v2.1.2.md` L233–L256, L338, L350) |
| S7 | C6 FCP-C6-EVAL-002, T6-002-01 | **six-route union** (direct tool, shell, interpreter, wrapper, nested-tool indirect, argument-injection into a read-only tool), run "as a superset until C1 harmonizes" | route | VERIFIED (identical row in the supplied v3 candidate and the accepted v4 on `main`) |
| S8 | C4 PAM-01…PAM-07 (C4 matrix v3, 2026-10-15) | **seven** concrete **test scenarios**; C4 states they are working labels, "not canonical categories", adopted by no Cloud | scenario | VERIFIED (C4 matrix text read) |
| S9 | C4 grouping analysis (C4 mapping §5, A–E) | the same scenarios regroup into **four, five, six or seven** groups depending on criterion | group | SOURCE-ASSERTED (C4's own earlier output; mapping file not re-derived) |

No source gives a normative total that all others accept. The number five in S1, S2, S4 and S5 cites one upstream requirement ("X1" per C4's reading); **its text was not located** in `c2-c6.TXT` or any file supplied (the only "X1" there, L2082, is a different C6 item). → open question **A3: UNKNOWN**.

## 2. Definitions preserved side by side (original wording class, not merged)

| Concrete case | C1 (S1) | C2 (S2) | C4 (S4) | Synthesis MV (S6) | C6 route (S7) | PAM (S8) |
|---|---|---|---|---|---|---|
| Named write tool | (1) direct write tool | (1) | (a) direct write | MV-01 | direct tool | PAM-01 |
| Shell writes | (2) shell write | (2) | (b) shell | MV-02 | shell | PAM-02 |
| Interpreter writes | (3) interpreter write | (3) | (c) interpreter | MV-03 | interpreter | PAM-03 |
| Wrapper / composite | (4) wrapper/composite commands "not themselves named as a write operation" | (4) wrapper/composite (RP-5 blind spot) | (e) a permitted tool wrapping a write-capable subprocess (overlap with MV-05 unresolved, INFERRED) | MV-04 | wrapper | PAM-04 (C1 breadth; includes RP-5 exec wrappers, `find -exec`); PAM-05 is C4-(e) primary |
| Indirect via nested tool call | (5), distinct from (4) per C1 | (5) | no distinct item | MV-05 | nested-tool indirect (C1/C2) | PAM-06 (C1-5/C2-5 primary) |
| Read-only tool whose arguments cause a side effect | not listed | not listed | (d) "indirect file mutation" (fixture path outside the test directory) | MV-06 | argument-injection (C4) | PAM-07 |
| Permitted tool spawns an OS subprocess | partly "second tool" (open) | partly | (e) primary | overlaps MV-04/MV-05 (unresolved) | not separately named | PAM-05 |

Reading rules kept from the sources: (i) crosswalk rows are **not** claims of equivalence; (ii) the PAM-05/PAM-06 question (one mechanism or two) is open item **A4**, owner C1; (iii) C1/C2 lists cover PAM-01–04 and PAM-06, PAM-05 only if "second tool" includes a subprocess, and **nothing in C1/C2 covers PAM-07** (C4 matrix coverage observation) — so a pass on the C1/C2 five would not exercise PAM-07.

## 3. What each candidate decision would change (consequences only; no choice made)

| If the owner accepts… | Effect on T6-002-01 and on `C1-E2` | Effect on PR #8 evidence |
|---|---|---|
| five-vector plan (S1/S2) as acceptance list, C4 (d) as supplement | argument-injection is run as a recorded supplement; coverage of PAM-07 is explicit but non-gating | none; AP-02/AP-14 stay open regardless |
| six surfaces (MV-01…06, S6) | T6-002-01's six routes become the acceptance list; PAM-05 stays unassigned until A4 | none |
| seven PAM scenarios as a list | would convert test cases into categories; C4's own labels disclaim this | none |
| a different grouping (S9 A–E) | needs a stated criterion first (A1: category vs mechanism) | none |

Decision order recorded by the sources: **A1** (level: category or mechanism) → **A2** (which list governs acceptance) → H-09 / G-1. **Owner: C1 / integration owner / human (H-09).** Closure evidence: a definition stated in the canonical file that owns the acceptance list, plus the X1 originating text (A3).

## 4. Inputs named in the directive that could not be located

| Item | Finding |
|---|---|
| C6 "G-07", "G-09" | The IDs exist as **gates `G-7` and `G-9` of the C1 synthesis** (VERIFIED in `rar2/…v2.1.2.md` L356, L358), not as C6 findings: **G-7** = `C1-E1b` executed (blocks fixing the Kernel delegation rule; any delegation deeper than one level) — NOT MET; **G-9** = a second model backend exists and `C1-E3` executed (blocks any adapter-sufficiency claim and adapters beyond a stub) — NOT MET. Whether these are the items the owner meant is **UNKNOWN**. |
| C6 "G-13" | No `G-13` (or `G13`) in any supplied file; the synthesis gate table ends at G-12. **UNKNOWN.** |
| C6 "P-01…P-06" | No such ID series in any supplied file or in `clouds/C6` on `main`. In the sources "P1…P6" are other Clouds' principle numbers (e.g. C1 P2, C5 P1, C5 P4) and "C6 P3/P4" cite C6 research principles. **UNKNOWN — not mapped, not assumed.** |

How G-7 and G-9 are used here anyway: G-9 means any adapter contract is a **proposal limited to tool/environment adapters** (ENG-003's own scope) and cannot support an "adapter-sufficiency" claim; G-7 means the nested-call/delegation boundary (PAM-06) is described as a mutation path only, with no delegation-depth rule proposed.
