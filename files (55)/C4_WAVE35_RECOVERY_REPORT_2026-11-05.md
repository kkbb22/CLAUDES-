# C4 — Wave 3.5 Historical Recovery Report (continuation, 2026-11-05)

**Result: `NOT RECOVERED`.** Not `RECOVERED-AND-HASH-VERIFIED`; not `FOUND-BUT-HASH-MISMATCH`. Nothing was reconstructed. No file was created under `C4-WAVE3.5-CONTEXT-v2.md` or `C4-WAVE3.5-ARGON-CONTEXT-MODEL.md`. Read-only; HEALTH and AI-OS were not modified.

## 1. What the manifest declares (VERIFIED, read from `main`)

`archive/historical/wave3.5/C4-WAVE3.5-CONTEXT-v2.manifest.yaml` · git blob `e2fb43821bd2696f1decd6b1a90d572a960fd882` · 3,574 B · SHA-256 `a2af752c7dcf1b934d25a29c967f4e179ebc42513ff5d6b2e368428b5ca844bb` (recomputed; equals C1's inventory row for the same path in `annex_A1…csv`). **Original** manifest (not derived).

| Field (SOURCE-ASSERTED about the Markdown) | Value |
|---|---|
| `filename` | `C4-WAVE3.5-CONTEXT-v2.md` |
| expected `sha256` | `22ca9931e0799e3285ac802f65677bc0859790acb9081b65addc340477f60a90` |
| `repo_target` | `kkbb22/ARGON-HEALTH` |
| `verified_repo_head` | `3520d70946f6623875c6f7d6ea47ef40f5bcc316` |
| `created_at_utc` | `2026-09-20T12:56:52Z` |
| `supersedes` (v1) | `C4-WAVE3.5-ARGON-CONTEXT-MODEL.md`, sha256 `a845053fd43af7a5642ae5287b2a1c762a83446867de8652f6dceae071358fe9` |
| a path of the Markdown | **not stated** — the manifest lists only `source_refs` (12 HEALTH documents it analysed) |

## 2. Retrieval attempt at the exact historical repository and commit

| Check | Result (VERIFIED, this session) |
|---|---|
| `3520d70…` exists in `kkbb22/ARGON-HEALTH` and is an ancestor of `main` (`fb6e3e3…`) | Yes |
| Tree at `3520d70`: 53 files; any path containing `wave`, `C4`, `context`, `assurance` | None |
| All 12 `source_refs` paths exist at `3520d70` and on `main` | Yes (existence only; line citations not re-verified) |
| SHA-256 of **all 201 blobs** in HEALTH history (all refs, 26 commits, PR refs 1–2) against `22ca9931…` and `a845053f…` | 0 matches |
| Filename search over HEALTH history (`wave3.5`, `C4-WAVE`, `CONTEXT-v2`) | 0 matches |
| AI-OS (9 refs, 18 commits): SHA-256 of 129 blobs outside `archive/external-health/` | 0 matches (reproduced here) |

**Independent corroboration (SOURCE-ASSERTED, not re-run):** C1's Phase A annex (`annex_A7`, `annex_A4_blobsearch.py` SHA-256 `15fd623a…ef1`, `annex_A5_zipscan.py` SHA-256 `cc926ba4…1fe`) and claim `CL-016` in `C1_CLAIM_TRACEABILITY_MATRIX.csv` record a hash search of **144 AI-OS + 201 HEALTH blobs plus a recursive scan of 7 tracked zip files**, with 0 hits for either hash and no filename match; status "NOT RECOVERED". That scan includes the `archive/external-health/` zips that I did not open. I did not reproduce it.

## 3. Interpretation

- **INFERRED:** `repo_target` names the repository the analysis was about, and the Markdown is a C4 **output** produced 2026-09-20 from HEALTH at `3520d70`. The cited sources exist at that commit; the output itself is not in that tree or in history. AI-OS `STATUS.md` L58–59 says the file was "never uploaded" (a repository assertion).
- The original text sits in none of the places the manifest points to. The remaining candidate locations are outside any repository: the original C4 session, a chat export or library download, or the owner's local copy. All **UNKNOWN**.

## 4. What the new bundle added

- `c2-c6.TXT` (221,902 B, 2,240 lines) SHA-256 `a542be977e7af20dfe90be08585b1a05e094351805a0d8c9dcb22301b2d0039a` — **VERIFIED equal** to the hash C6 declared for its source container (`c2-c6(1).TXT`), and byte-identical to the copy in the C3 review bundle. This closes C6's "source TXT not provided" item for the **hash**; the declared extraction range and quotations were not re-derived here.
- That TXT contains (L1220–) an **earlier** C4 recovery report written when the manifest itself was unavailable; it records the same non-recovery and no reconstruction. It is a SOURCE-ASSERTED record of an earlier session, not the missing file.
- VERIFIED this session: every member of the bundle was SHA-256-hashed, including nested zips (89 zip members, recursive) and the members of both `.rar` archives (read through libarchive: the C6 pack/reconciliation files; synthesis v2.1.2 and C7 rev5/rev6 files) — **0 matches** for `22ca9931…` or `a845053f…`.

## 5. Not checked

`archive/external-health/` content opened by me (hash-level corroboration relies on C1); unreachable or force-deleted GitHub objects; forks; the owner's local clone and original chat sessions; hash variants beyond exact bytes for AI-OS (CRLF/trailing-newline variants were compared only in the earlier C4 package for HEALTH).

## 6. Options (no action taken)

- **A** keep the orphan manifest with a note: "Markdown not found at the manifest's repository/commit nor in checked AI-OS/HEALTH history; original output not retrievable".
- **B** a separately named, clearly labelled **reconstruction** only with explicit written owner authorization; v2's exact wording and the v1-derived `semantic_graph` cannot be reproduced from any checked source. Not performed.

## 7. Closure evidence

The original `.md` bytes with filename, source (session/export/path) and SHA-256 equal to `22ca9931…` (ideally also v1 `a845053f…`), or a written owner statement that the artifact is unrecoverable. Owner: human owner (local files/sessions); C7 for independent confirmation. Wave 3.5 recovery does **not** authorize Wave 4 or any HEALTH write.
