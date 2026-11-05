# C7 — Phase B Frozen-Input Manifest TEMPLATE (C7-FFA-004)

**Status: TEMPLATE. NOT FROZEN. NO VERDICT. Phase B is `NOT ISSUED — BLOCKED`.**
Rows marked "C7-VERIFIED 2026-11-05" were re-hashed by C7 from the supplied recovery package (`0be6f07a…b5f16`, internal SHA256SUMS 43/43 OK). Everything else is a placeholder to be filled at freeze time by the owner, then **re-hashed independently by C7**.

## A. Freeze header (owner to complete)
| Field | Value |
|---|---|
| Freeze declared by (human owner) | ______ |
| Freeze date/time UTC | ______ |
| C1 candidate filename + version | ______ (must be ONE file; v2.1.1 / v2.1.3 / later) |
| Pinned AI-OS baseline commit | ______ (C1 says `main`=`1458a7f54f5d190ff84fce66cb2568960ff73559` at 2026-11-04T12:00Z; Rev5 audited against `71a3fa6d1fb1eed0e694886263710d4020e10341`; choose one, justify) |
| Ancestry proof (`git merge-base --is-ancestor`) | ______ |
| Line-ending policy (raw vs LF-normalized) | ______ |

## B. Input table (one row per file)
Columns: `ID | role | exact path/name | bytes | SHA-256 declared | SHA-256 C7 recomputed | source repo@commit | original/derived | status`

| ID | Role | Path / name | Bytes | SHA-256 (C7-recomputed where known) | Original/derived | Status |
|---|---|---|---|---|---|---|
| IN-01 | C1 candidate (CRLF variant, the one Rev5 audited) | `C7-FFA-004-rev5-audited-v2.1.1-candidate.md` | 58,856 | `170ba691066e7109b3b68f14fe19f3b78c2e69795e179cf2fddfd0d8bb548d0a` | derived copy of C1 candidate; matches Rev5 stated hash | C7-VERIFIED 2026-11-05 (bytes match Rev5) |
| IN-02 | C1 candidate (LF variant) | `ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.1.1 (1).md` | 58,392 | `1dd2be416adb4873ad5599d70f6a0a7b56cf58b8ed9a7f7a99a84c8b77f6287b` | derived | C7-VERIFIED: differs from IN-01 only by CRLF and one trailing newline. **Owner must designate which is the frozen candidate.** |
| IN-03 | Prior C7 report | `C7-FFA-004-revision5.md` | 22,005 | `e5c4e2add55d6894af913366fbf29b0581d3242d59ad46e814a79b70d1150912` | original (C7) | C7-VERIFIED (hash only) |
| IN-04 | Prior C7 report | `C7-FFA-004-revision3.md` | 28,919 | `bfbfa72bf0485c508ffeab28f7d853a19992394b9d806e6bd9fee7e973edc03f` | original (C7) | C7-VERIFIED (hash only) |
| IN-05 | C1 v2 draft (in main via PR #7) | `ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.md` | 31,924 (CRLF copy; C1 says 31,390 B in repo) | `eb679f0d88f82a7ba73724b01eeb660e6bad1ed8a75568b0a516382fab215109` | derived copy | size differs from C1's repo size: byte-equality with repo blob UNKNOWN |
| IN-06 | Source TXT (C2–C6 research) | `c2-c6.TXT` | — (2,240 lines) | `a542be977e7af20dfe90be08585b1a05e094351805a0d8c9dcb22301b2d0039a` | original source | C7-VERIFIED: equals hash declared in C6 manifest. (C6 asked for `c2-c6(1).TXT`; the supplied name differs: name-equivalence is INFERRED from the identical hash.) |
| IN-07 | C6 pack | `C6-FUTURE-EVALUATION-CAPABILITY-PACKS.md` | 53,423 | `213f25a5222a5bfa8a2c6e32df27b565403fcf4ea34d9be5af01d4086d2f020e` | original (C6) | C7-VERIFIED against C6 reconciliation report value |
| IN-08 | C6 manifest | `C6-FUTURE-EVALUATION-CAPABILITY-PACKS.manifest.yaml` | 3,995 | `0a3c4c14bcade9d1bcd8173c74e04968f00373bd2d13af91bd269e499efe1050` | original (C6) | C7-VERIFIED against C6 report value |
| IN-09 | C6 index row snippet | `C6-CAPABILITY-INDEX-ROW.proposed-snippet.md` | 1,567 | `66b98dea9a98b29673864fd50fa1c1d777c7c3e6cc2c884e2b2ee98660e4ea1c` | original (C6) | C7-VERIFIED against C6 report value |
| IN-10 | C2 RP-13 plan v3 + manifest + provenance | NOT SUPPLIED (only C2 research + manifest present) | — | — | — | MISSING |
| IN-11 | C3 r3 candidate + checker output + `logs/input-hashes.txt` + fixtures/oracles | C3 review bundle present (`C3-review-bundle-2026-10-17.zip`); candidate r3, checker output, input-hashes log not located by name | — | — | — | PARTIAL; C7 inspection pending |
| IN-12 | C4 Plan/Act matrix v3 + manifests/diffs/logs | NOT SUPPLIED | — | — | — | MISSING |
| IN-13 | C4 Wave 3.5 original Markdown | NOT SUPPLIED; expected SHA-256 `22ca9931e0799e3285ac802f65677bc0859790acb9081b65addc340477f60a90` (from manifest only) | — | — | — | NOT RECOVERED |
| IN-14 | C5 r3 acceptance tests (18) + C5 v1 | NOT SUPPLIED (v1 NOT RECOVERED) | — | — | — | MISSING |
| IN-15 | C1 correction matrix + manifest for candidate | NOT SUPPLIED | — | — | — | MISSING |
| IN-16 | Repo exports at pinned baseline (AI-OS, read-only) | NOT SUPPLIED | — | — | — | MISSING (C7 has C1's inventory CSV only) |
| IN-17 | PR-09 branch export, diff, logs, Docker evidence | NOT SUPPLIED (CL-004: branch/commit absent from public remote) | — | — | — | MISSING |
| IN-18 | 2026-11-02 PR-09 forensic audit report | NOT SUPPLIED | — | — | — | MISSING |

## C. Gate-by-gate verdict matrix (blank; to be filled only after freeze)
| Gate | Required input IDs | Status | Evidence |
|---|---|---|---|
| 1 Baseline/candidate integrity, ancestry | IN-01/02, IN-16 | NOT STARTED | — |
| 2 Source authenticity/completeness | IN-06, IN-10..14 | NOT STARTED | — |
| 3 C1 lineage + faithful C2–C6 treatment | IN-01..15 | NOT STARTED | — |
| 4 RP-13 security questions | IN-10 | NOT STARTED | — |
| 5 Context/evidence isolation | IN-11 | NOT STARTED | — |
| 6 Mutation boundaries / Plan-Act | IN-12, IN-16 | NOT STARTED | — |
| 7 Human approval / identity / binding | IN-10, IN-14, IN-16 | NOT STARTED | — |
| 8 C6 design-only acceptance + counts | IN-07..09 | NOT STARTED | — |
| 9 Governance / decision rights | all | NOT STARTED | — |
| 10 Reproducibility of tests | all execution evidence | NOT STARTED | — |
| PR-09 independent review | IN-17, IN-18 | NOT STARTED | — |

## D. Sign-off
Owner freeze statement: ______ · C7 re-hash completed (date, tool, command): ______ · Disposition: **NOT ISSUED** until all rows above are filled and gates reviewed.
