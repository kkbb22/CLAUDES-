# C2_00 — Identity, Input Inventory and Verification Findings (2026-11-05)

## 1. Identity charter (restated)
- **Identity:** C2 — ARGON Security, Trust & Authorization Architect.
- **Original role:** examine identity, trust, authentication, authorization, cryptographic binding, replay resistance, revocation, key custody and approval integrity; design and evaluate security controls and experiments.
- **Boundaries:** read-only; no edits to source/governance/manifests/registers; no commits, PRs, pushes, merges, deployments, runtime actions or mutation harnesses; no access to real health data; no autonomous execution; **no Wave 4**; no writes to ARGON-HEALTH; Legacy ARGON not inspected; C2 does not issue C7's independent verdict and does not choose human policy.
- **Persistence:** **SESSION-ONLY.** The platform did not confirm any persistent save of this charter and C2 did not save it. This charter must be repeated in any handover (it is, in `C2_07_HANDOVER_TO_NEXT_CLOUD.md`).
- **Repository separation preserved:** ARGON-AI-OS only. ARGON-HEALTH and Legacy ARGON were not opened.

## 2. Evidence vocabulary used in this continuation
VERIFIED (reproduced by C2 from a named source) · SOURCE-ASSERTED · INFERRED (labelled) · UNKNOWN · NOT RECOVERED. And always: SPECIFIED ≠ IMPLEMENTED ≠ EXECUTED ≠ PASSED WITH EVIDENCE.

## 3. Verification findings that change the picture
| # | Finding | Label | Evidence |
|---|---|---|---|
| V-1 | The recovery zip and all 43 files listed in its `SHA256SUMS.txt` match byte-for-byte. | VERIFIED | section A below |
| V-2 | **The "RP-13 candidate v3" file is NOT in this bundle.** Its hash appears only as a truncated string `3efe555f0b1f96f4…36e47aa6` in the 2026-10-16 review (`ARGON_C2_C6_LATEST_RESULTS_REVIEW_2026-10-16.md`, line 56). C2 searched every file, every nested zip (C1 starter pack, prompts pack, C3 bundle, files (50)) and both rar archives for `3efe555f`: only that review line matches. Its manifest and review artifacts are likewise absent. | NOT RECOVERED (v3 file + manifest) / SOURCE-ASSERTED (hash, "55 tests/12 scenarios") |
| V-3 | **An earlier RP-13 plan IS recoverable as text**: `c2-c6.TXT` lines 2–565 (file begins `# C2-RP13-CRYPTOGRAPHIC-BINDING-EXPERIMENT-PLAN.md`, prepared 2026-10-13) followed by an embedded manifest block declaring `report_sha256: 635a2f836afcb7fa1318e6477f6136aa3723911d21e4d0b640f5572a5da6dc3e`. C2 reproduced that hash exactly: the C2 segment, CRLF→LF normalized, from line 2 to the line before `artifact_id:` (the manifest block), plus one trailing newline, hashes to `635a2f83…da6dc3e`. The 10-16 review says the C2 segment's hash "does not equal candidate-v2"; that statement is about a different comparison and does not contradict this match. | VERIFIED (self-consistency of the Oct-13 plan with its own embedded manifest) |
| V-4 | That recovered Oct-13 plan contains **55 test IDs** (T1-01…T1-08, T2-01…T2-08, T3-01…T3-09, T4-01…T4-08, T5-01…T5-09, T6-01…T6-13) and **12 scenarios** (X-01…X-12). So the "55 tests / 12 scenarios" counts are reproducible for the Oct-13 plan; whether v3 (3efe555f…) has identical content is UNKNOWN. | VERIFIED for Oct-13 text / UNKNOWN for v3 |
| V-5 | All 55 + 12 are `TEST SPECIFIED`; the plan itself says none executed and that status vocabulary caps at `DESIGNED / NOT_IMPLEMENTED / TEST SPECIFIED`. No execution evidence exists anywhere in the bundle. | VERIFIED (statement in text); EXECUTED=0 is SOURCE-ASSERTED |
| V-6 | `G-5` and `G-11` are **not in the C6 files**. They are gates in the C1 synthesis `§15 Wave 4 Preconditions`: `ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.1.1 (1).md` lines 353, 359 and `…v2.1.2.md` (in the second rar) lines 354, 361; both NOT MET. (Written `G-5`, not `G-05`.) The C6 pack's RP-13-related dependency statements are at `C6-FUTURE-EVALUATION-CAPABILITY-PACKS.md` lines 98, 155, 352 (consumes C2 TV-002-A…I; adds a "binding disabled" mutant; human decision whether to build binding). | VERIFIED (locations) — directive's attribution of G-05/G-11 to the C6 report is a labelling discrepancy for the owner |
| V-7 | The repo `main` C6 pack (`dab7060e…`) differs from the rar/bundle C6 candidate (`213f25a5…`) — expected after the repo's post-merge provenance fix (PR #6); C2 did not diff them. | VERIFIED (hashes differ) / cause INFERRED |
| V-8 | PR-09 branch/logs/Docker evidence: **not in the bundle** (README item 1 says so; `PR-09`/`PR #9`/`follow-up` yields 0 hits in C7 rev5 candidate, C7 rev6 draft, and the v2.1.2 unresolved register). | NOT RECOVERED |
| V-9 | C7 for the C1 candidate: `C7-FFA-004-revision6-review-draft.md` states **NOT ISSUED — no clean verdict** (review date 2026-10-20). | VERIFIED (text) |

---
## Inventory (continuation 2026-11-05)

Method: unzip of `ARGON_COMPLETE_RECOVERY_2026-11-05.zip` into scratch (original never modified); `sha256sum -c` against the bundle's own `SHA256SUMS.txt`; independent re-hash by C2 of every file below.

**Container:** `/mnt/user-data/uploads/ARGON_COMPLETE_RECOVERY_2026-11-05.zip` — 12,584,992 bytes — SHA-256 `0be6f07ac8d68170a450355cd1b7abe83082d606d414e9845020d6fa8a6b5f16` (VERIFIED by C2; no external reference hash was supplied to compare).

**Bundle SHA256SUMS.txt check:** all 43 listed files `OK` (VERIFIED). `SHA256SUMS.txt` itself is not self-covered. This proves byte-integrity versus the bundle author's list only, not provenance.

## A. Files in the bundle (path relative to bundle root)

| Path | Bytes | SHA-256 | Origin class |
|---|---:|---|---|
| `00_README_AR.md` | 3992 | `424db0b8b6aa00b6c8e2ec27af50490be4500d5c17bd3cac2e55a502d9ca67c5` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.1.1 (1).md` | 58392 | `1dd2be416adb4873ad5599d70f6a0a7b56cf58b8ed9a7f7a99a84c8b77f6287b` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.md` | 31924 | `eb679f0d88f82a7ba73724b01eeb660e6bad1ed8a75568b0a516382fab215109` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/ARGON_C1_STARTER_PACK_2026-11-04.zip` | 48228 | `c29b846f6fa6f5003deb50876466f0eb0e12b737eb56f371b694fe3d60c3b6ec` | ORIGINAL ARCHIVE (not unpacked unless stated) |
| `01_RECOVERED_LIBRARY_FILES/ARGON_C1_SYNTHESIS_V2_PREFLIGHT_2026-10-18.md` | 6527 | `670ad2cc77c8c481c087c0c5e3fc4258878d2a73dbc5117531c183180e891af5` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/ARGON_C2_C6_LATEST_RESULTS_REVIEW_2026-10-16.md` | 15175 | `84ac90b063beffbea3d454f97602934d00b2f96406680288b440d7f9ed8000cb` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/ARGON_C3_REVIEW_REPORT_2026-10-17.md` | 10954 | `fd84746545bf421bfdbef2b28e3c63ca1e1de1a465da5fbb466812a34c985fdf` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/ARGON_PHASE_ZERO_FORENSIC_AUDIT_2026-10-17.md` | 42150 | `87882b20f96e6580c1c43fdb26008ebcfeaf3e36dad0761d28751b465021a5fb` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/ARGON_SEVEN_CLOUDS_INDIVIDUAL_PROMPTS_2026-11-04.zip` | 28557 | `8d8d49482820f27c3cc2540204739c619c44cc638114eb3518b2cb8053516750` | ORIGINAL ARCHIVE (not unpacked unless stated) |
| `01_RECOVERED_LIBRARY_FILES/C3-review-bundle-2026-10-17.zip` | 139937 | `0d5d6be2e4faea0fcbd4cfecc9923ef5a47e664d06e730e9535f5124175afb7e` | ORIGINAL ARCHIVE (not unpacked unless stated) |
| `01_RECOVERED_LIBRARY_FILES/C6-CAPABILITY-INDEX-ROW.proposed-snippet.md` | 1567 | `66b98dea9a98b29673864fd50fa1c1d777c7c3e6cc2c884e2b2ee98660e4ea1c` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/C6-FUTURE-EVALUATION-CAPABILITY-PACKS.manifest.yaml` | 3995 | `0a3c4c14bcade9d1bcd8173c74e04968f00373bd2d13af91bd269e499efe1050` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/C6-FUTURE-EVALUATION-CAPABILITY-PACKS.md` | 53423 | `213f25a5222a5bfa8a2c6e32df27b565403fcf4ea34d9be5af01d4086d2f020e` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/C6-RECONCILIATION-REPORT.md` | 6753 | `70b4bd3ffceb507a43e4c5f2c5882a96d64c97aba63fcc67934843fd5b2b40d5` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/C7-FFA-004-rev5-audited-v2.1.1-candidate.md` | 58856 | `170ba691066e7109b3b68f14fe19f3b78c2e69795e179cf2fddfd0d8bb548d0a` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/C7-FFA-004-revision3.md` | 28919 | `bfbfa72bf0485c508ffeab28f7d853a19992394b9d806e6bd9fee7e973edc03f` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/C7-FFA-004-revision5.md` | 22005 | `e5c4e2add55d6894af913366fbf29b0581d3242d59ad46e814a79b70d1150912` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/Pasted text(10).txt` | 13783 | `60559a2768d47763b15140ae7c45e41ccfc3c57350030a4d96e6b76dccbb92f8` | DERIVED (pasted text; not analysed in this continuation) |
| `01_RECOVERED_LIBRARY_FILES/c2-c6.TXT` | 221902 | `a542be977e7af20dfe90be08585b1a05e094351805a0d8c9dcb22301b2d0039a` | DERIVED (text concatenation of C2..C6 Cloud outputs; per 10-16 review, session export) |
| `01_RECOVERED_LIBRARY_FILES/files (50).zip` | 29359 | `e219a2ac97d437994e19f6455d57c9a05a12a751af5672e7b299b83f9c40f506` | ORIGINAL ARCHIVE (not unpacked unless stated) |
| `01_RECOVERED_LIBRARY_FILES/more/ARGON_CLOUDS_1-7_PARALLEL_PROMPT_PACK_2026-10-14.md` | 24306 | `12b8a45a32602429bb9b23b5bbfaacc3096a6c1c1aee9ed2b93191c592473ab5` | ORIGINAL prompt text |
| `01_RECOVERED_LIBRARY_FILES/more/C2-CLOUD-SECURITY-ADAPTER-RESEARCH.manifest.yaml` | 4241 | `8cc757b13a9f9277562f32f4bffc83ab588de0599593a2120ba954823017c597` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/more/C2-CLOUD-SECURITY-ADAPTER-RESEARCH.md` | 77548 | `c6e95c268aa6b065737933cbeff10761939d8f310cb11db8b9907fb03d000b99` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/more/C6_EVALUATION_VERIFICATION_PROMPT.md` | 5952 | `4677f12acff6a2c23c057bd0833351ba63dcc35273c41c66e861646eebdae4a5` | ORIGINAL prompt text |
| `01_RECOVERED_LIBRARY_FILES/more/C7_INDEPENDENT_AUDITOR_PROMPT.md` | 8142 | `cc85b77c29a1228e087e7043c48bab27d7645af9ce343c617bfc2359cc054761` | ORIGINAL prompt text |
| `01_RECOVERED_LIBRARY_FILES/more/README_AR.md` | 3555 | `a44ee5c0cb3ee9e5d07127a025148001b9105117f14b8ce6992299ab75b54286` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `01_RECOVERED_LIBRARY_FILES/more/مراجعة اخر تحديثات.rar` | 12017905 | `8fba283a89ae07593d4c2c3a6f00829f86abdda9e561fbf9717e267d5b3c5e40` | ORIGINAL ARCHIVE (extracted by C2 into scratch with bsdtar; members hashed below) |
| `01_RECOVERED_LIBRARY_FILES/prompts/C1_ORCHESTRATOR_PROMPT.md` | 8640 | `9c0ff78dd204d3c87f7e0c88e984f7f14522e1aeeb5288485be691f7580bfdb2` | ORIGINAL prompt text |
| `01_RECOVERED_LIBRARY_FILES/prompts/C2_SECURITY_TRUST_AUTHZ_PROMPT.md` | 8103 | `d1abb40dc8bbbaaf1602e6e40c8fedad0541b65a86be7d9dfff89f9cc9176e14` | ORIGINAL prompt text |
| `01_RECOVERED_LIBRARY_FILES/prompts/C3_CONTEXT_EVIDENCE_PROMPT.md` | 6627 | `9b913c9c97e1300cb58b1b49f1a3355aad413be370a5e6791b8e482767527203` | ORIGINAL prompt text |
| `01_RECOVERED_LIBRARY_FILES/prompts/C4_EXECUTION_MUTATION_BOUNDARIES_PROMPT.md` | 7388 | `ffc099b5d9be4422063aaef17ae4db6db70871f2070bb7520583eb1045d5002b` | ORIGINAL prompt text |
| `01_RECOVERED_LIBRARY_FILES/prompts/C5_OPERATOR_APPROVAL_PROMPT.md` | 6574 | `5617865f9c0bf7d97414908c039c6b9d4cc0be5a2bc741a85f669bb93ec3008d` | ORIGINAL prompt text |
| `01_RECOVERED_LIBRARY_FILES/اخر مخرجات كلاود 6.rar` | 26223 | `d7cab1d1ee90d4abec93397acc426ba9ffac0e6df268fd018c1b9ad9b388a5bb` | ORIGINAL ARCHIVE (extracted by C2 into scratch with bsdtar; members hashed below) |
| `02_INVENTORY_ARCHIVE_EXTRACTED/C1_CLAIM_TRACEABILITY_MATRIX.csv` | 15211 | `0bf6c56317ca679f3ecae5de480e34ec34bb0dd07ec63e3d2fa6af061c49c1eb` | DERIVED (inventory tables/scripts from files(50).zip, not repo copies) |
| `02_INVENTORY_ARCHIVE_EXTRACTED/annex_A1_inventory_ARGON-AI-OS_main_1458a7f.csv` | 25338 | `f8af083339802d9c69b5e1c8280a94bb05c5531a1596609d47792f74dc2137d7` | DERIVED (inventory tables/scripts from files(50).zip, not repo copies) |
| `02_INVENTORY_ARCHIVE_EXTRACTED/annex_A2_inventory_ARGON-HEALTH_main_fb6e3e3.csv` | 12475 | `ae4cd7582cbbb6a68a67f35fd759b4f9fd4a2039b7c64fff01277dc622a48d43` | DERIVED (inventory tables/scripts from files(50).zip, not repo copies) |
| `02_INVENTORY_ARCHIVE_EXTRACTED/annex_A3_starter_pack_inventory.csv` | 1649 | `c91fdca8921f17fe02ec92b3c22d4d4178811c490cf56eceea286ac2113baf2a` | DERIVED (inventory tables/scripts from files(50).zip, not repo copies) |
| `02_INVENTORY_ARCHIVE_EXTRACTED/annex_A4_blobsearch.py` | 1107 | `15fd623ac8846c907624e9df1ab794076cc9aef043094073b1e707b31b4c4ef1` | DERIVED (inventory tables/scripts from files(50).zip, not repo copies) |
| `02_INVENTORY_ARCHIVE_EXTRACTED/annex_A5_zipscan.py` | 1147 | `cc926ba4421396cbc61665427ed22416fdd7e418e9e65af134f173281b2231fe` | DERIVED (inventory tables/scripts from files(50).zip, not repo copies) |
| `02_INVENTORY_ARCHIVE_EXTRACTED/annex_A6_inventory_builder.py` | 686 | `3543f97fb57ac8c76a21560bf76769f6998969020e40bb862b3eec64fc1c052f` | DERIVED (inventory tables/scripts from files(50).zip, not repo copies) |
| `02_INVENTORY_ARCHIVE_EXTRACTED/annex_A7_commands_and_access_log.txt` | 2300 | `4d442890a4a08fe5c61824b31ce3547409b8547b86665c73b2cd920d56f8def4` | DERIVED (inventory tables/scripts from files(50).zip, not repo copies) |
| `ARGON_CLOUD_DISPATCH_PACK_2026-11-04.md` | 19029 | `3a01e7a06d5d1b2c07a84cfa8a234d907e548b72fe25bf6c42b25feb18207d8e` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |
| `ARGON_MASTER_HANDOVER_2026-11-04.zip` | 39655 | `36fedd57dda2a3fe8e5df014ea571ab140d1b8ac6f74319995722b8744d69a73` | ORIGINAL ARCHIVE (not unpacked unless stated) |
| `SHA256SUMS.txt` | 5545 | `ac74682eb3af6d0775395dde2afba3dfa16e64f76be526fe61784cfc4d79398b` | ORIGINAL or recovered copy (source repo/commit NOT stated in bundle unless noted) |

Source repository/commit: the bundle states none per file. Files that exist in `kkbb22/ARGON-AI-OS` carry the commit shown in section C.

## B. RAR members extracted by C2 (scratch only)

**`01_RECOVERED_LIBRARY_FILES/اخر مخرجات كلاود 6.rar`** (extraction by libarchive `bsdtar`; success = VERIFIED)

| Member | Bytes | SHA-256 |
|---|---:|---|
| `C6-CAPABILITY-INDEX-ROW.proposed-snippet.md` | 1567 | `66b98dea9a98b29673864fd50fa1c1d777c7c3e6cc2c884e2b2ee98660e4ea1c` |
| `C6-FUTURE-EVALUATION-CAPABILITY-PACKS.manifest.yaml` | 3995 | `0a3c4c14bcade9d1bcd8173c74e04968f00373bd2d13af91bd269e499efe1050` |
| `C6-FUTURE-EVALUATION-CAPABILITY-PACKS.md` | 53423 | `213f25a5222a5bfa8a2c6e32df27b565403fcf4ea34d9be5af01d4086d2f020e` |
| `C6-RECONCILIATION-REPORT.md` | 6753 | `70b4bd3ffceb507a43e4c5f2c5882a96d64c97aba63fcc67934843fd5b2b40d5` |

**`01_RECOVERED_LIBRARY_FILES/more/مراجعة اخر تحديثات.rar`** (extraction by libarchive `bsdtar`; success = VERIFIED)

| Member | Bytes | SHA-256 |
|---|---:|---|
| `ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.1.2.correction-matrix.md` | 10614 | `9dcd95aa5eab214188a0f70aa57c4fc105f6422febd80c6dc4a323b956dd95bd` |
| `ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.1.2.md` | 65971 | `563e72215bd2e3a8791d4aa977484eaeac285e6453d620cf8aa219040638e086` |
| `ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.1.2.proposed-intake-manifest.yaml` | 3533 | `7b0f852b8a9161c291b04a95eee23413375c529ab1d8eb5224ab682f6ec66cb4` |
| `ARGON-AI-OS-CROSS-CLOUD-SYNTHESIS.v2.1.2.unresolved-register.md` | 3248 | `2d155fddc156ae82460d2bf9063e5954a6c9f64d2e1f9baa06ddf2cfab76f9e5` |
| `C7-FFA-004-revision6-review-draft.md` | 10952 | `531c6b7edd8e7a812f1c2174f620a04ab7b855b0e1bfc1da7a2b2637ac4a6642` |
| `source/C7-FFA-004-rev5-audited-v2.1.1-candidate.md` | 58856 | `170ba691066e7109b3b68f14fe19f3b78c2e69795e179cf2fddfd0d8bb548d0a` |
| `source/C7-FFA-004-revision5.md` | 22005 | `e5c4e2add55d6894af913366fbf29b0581d3242d59ad46e814a79b70d1150912` |

Observation (VERIFIED): the four C6 rar members are byte-identical (same size and SHA-256) to the same-named files in `01_RECOVERED_LIBRARY_FILES/` — e.g. `C6-FUTURE-EVALUATION-CAPABILITY-PACKS.md` `213f25a5…020e`, which equals `report_sha256` in its manifest. The second rar holds the C1 v2.1.2 candidate set and `C7-FFA-004-revision6-review-draft.md` (C7 status in that draft: NOT ISSUED — no clean verdict).

## C. Source code used for static mapping (read-only clone, never modified)

Repository `github.com/kkbb22/ARGON-AI-OS`, `main` = `1458a7f54f5d190ff84fce66cb2568960ff73559` (`Merge pull request #8 from kkbb22/feat/argon-health-engineering-loop`; PR #8 content commit `708142c`). VERIFIED by `git rev-parse HEAD` in the clone.

| Path in repo | Bytes | SHA-256 |
|---|---:|---|
| `runtime/core/policy.py` | 13651 | `d89cf393a8212690079235e0dc19283051f44bc8cb551f4d3b1a28b64ae2a1dc` |
| `runtime/core/contracts.py` | 14095 | `6a889d3c09f35ddb25b042503affab10d6dcfe507bce5a4afc67c15d61d71f6d` |
| `runtime/core/tools.py` | 8352 | `6866630c64fefa60a12d6127d956e133e26d9b3e32e20a76d86322268e490cb1` |
| `runtime/core/verifier.py` | 7834 | `944e41e45475d77561d6a0d9f5d1a109a273e68bf971f148ea3354150a3d0aa8` |
| `runtime/core/evidence.py` | 10850 | `4c51173f11241aed19fe71b474b04b6b07f70775854db03e12fa534ac4a8da40` |
| `runtime/core/orchestrator.py` | 14641 | `6c2907f150805187803caea5e348c7eb3c19e6b6b08bf9035d696c0ffa91150b` |
| `runtime/core/cli.py` | 9480 | `8bab050401609125041e6331c0133cc86a56c92c2cba0fbc3f2997cca1126d1c` |
| `runtime/core/workspace.py` | 9594 | `aac0e5df9236cb3814c400bc6c4c9cc2af1e19e42bfca45ef3045be196082d70` |
| `runtime/argon_runtime.py` | 4498 | `d5f91b19fea23c64ec98c85e2d08423e2800ec3e47a98b23eadeb27435863844` |
| `clouds/C2/C2-CLOUD-SECURITY-ADAPTER-RESEARCH.md` | 77548 | `c6e95c268aa6b065737933cbeff10761939d8f310cb11db8b9907fb03d000b99` |
| `capabilities/future/C2/C2-FUTURE-SECURITY-CAPABILITY-PACKS.md` | 58668 | `8d6148bfc92e8d29bdea80feb877727a84d2d214a381a849d879c7759359cc38` |
| `clouds/C5/C5-OPERATOR-CONTROL-RESEARCH.md` | 45242 | `e70ea36bcab13b1abf76dbc386a82ca114a8c86c66f689d30224f1de71c9e1a8` |
| `clouds/C6/C6-CLOUD-EVALUATION-ENGINE.md` | 51027 | `a0d762ad472f0e5fb6a891495a943ca808ac642ab5b7d3b9eab42fd0e237946a` |
| `archive/historical/wave3.5/C2-WAVE3.5-SECURITY-RECONCILIATION-v2.md` | 12057 | `7b59fcfc49d0408461717cb055f3f7e81c4faecde1f0e5cdbea47b83a2f44f51` |
| `capabilities/future/C6/C6-FUTURE-EVALUATION-CAPABILITY-PACKS.md` | 55128 | `dab7060ec1042a9ee09749fc5303b663dea961ab349e6919ede9bc52ee5cbc68` |