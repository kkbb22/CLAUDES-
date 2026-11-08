# ARGON DENTAL — Final Independent Review of All Seven Cloud Deliverables

| Field | Value |
|---|---|
| Reviewer role | Independent architecture reviewer (Cloud 7, second pass) |
| Review date | 2026-11-08 |
| Inputs | Seven Markdown files uploaded to this session (see §0.2) |
| Nature of work | Review and documentation only. No repository was modified. No application code was written or executed. No real patient data was used. |
| **Updated verdict** | **NOT READY for implementation.** Ready to start **Phase 0 (decisions and evidence)** immediately. See §A. |
| Production-readiness claim | **None.** Nothing in this report states or implies that any ARGON control is implemented, tested, or production-ready. |

---

## 0. How to read this report

### 0.1 Labels

| Label | Meaning |
|---|---|
| **[FACT-R]** | Observed by this reviewer in one of the seven uploaded reports (what the report *says*, not whether it is true of the software). |
| **[FACT-W]** | Verified by this reviewer from a web source during this review (source named). |
| **[PROPOSAL]** | This reviewer's recommendation. Needs the named approver. |
| **[ASSUMPTION]** | Unverified. Must be confirmed before reliance. |
| **[OPEN]** | Unresolved question. |

A statement that a report "documents" or "specifies" something is never evidence that the software does it.

### 0.2 What this review did and did not read (read this first)

The brief asks for all seven reports to be read in full. **That was not fully achieved.** The six team reports total about 840 KB. I read all of Cloud 2 (database) except its reference list, and the decision-bearing sections of the others. The table states exactly what was and was not read. Findings about unread sections may be incomplete.

| # | Report | Read in detail | Read structurally only (headings, indexes, keyword scans) | Not read |
|---|---|---|---|---|
| 2 | Cloud 2 — Database and System Architecture | §1–§23, §25 (entities, identity, chart model, tenancy, versioning, files, integrity, backup, API, migration, security, risks, acceptance, tests, decisions, sequence) | §24 references | Nothing material |
| 3 | Cloud 3 — Clinical Workflow Requirements | §1, §6.3 entities, §13 screens, §15 roles, §20.1 sample tests, §22–§25, Appendix E | Workflows W-01…W-18, FR tables, clinical foundations, §9–§12, §14 dictionary, journeys, edge cases | Most individual requirement rows |
| 4 | Cloud 4 — UX/UI Design System | §1, §2.3, §8.9, §13.2; keyword scans | Screens S01–S18, tokens, components, journeys | Most screen bodies, appendices |
| 5 | Cloud 5 — Regulatory Research | §1, §3 assumptions, §5.1–§5.10, §6.5–§6.10, §8 requirements, §11 gates | Compliance matrices, comparison matrix, tests, questions | Reference list, Appendix B |
| 6 | Cloud 6 — Quality Engineering | §1–§2, §8 traceability, §9 gates, §13–§14, test-ID inventory | Strategy §3–§6, regression, checklist | The 160 test-case bodies (§7) |
| 7a | Security Architecture Assessment | §0–§5, §6.4–§6.6, §6.13, §9, §10.4, §11–§13, §14.2 | Other control tables (§6.1–§6.3, §6.7–§6.12, §6.14–§6.16), threat model, data-class matrix | Test catalogue §10.2, appendices |
| 7b | My previous review | Byte-compared with my earlier output: identical | — | — |

**Consequences.**
- Counts such as "135 controls" or "160 test cases" are **[FACT-R]** quoted from the reports; I did not recount them.
- The traceability matrix in §D is at **requirement-family level**. It uses the real IDs I saw. Where I did not read a specific test body, the row says "family".
- **The repository could not be accessed.** This session has no network access to the repository, so I could not clone it, read it, or place the report in it. I read the uploaded copies only. The report was **not committed or pushed** (as instructed); it is saved as an output file in this session for you to copy into the folder.
- I could not re-verify most legal claims. The one external check I made is in §0.3.

### 0.3 External checks made by this reviewer

| Check | Result | Label |
|---|---|---|
| Does Firebase list Gulf regions for Cloud Functions? | Official Firebase Cloud Functions locations page lists **me-central1 (Doha)** and **me-central2 (Dammam)**, both "2nd gen only", and also Tel Aviv. URL: https://firebase.google.com/docs/functions/locations (returned by search 2026-11-08). | **[FACT-W]** |
| Does Realtime Database or Firestore offer a Gulf region? | **Not established.** Cloud 5 says Firestore lists Doha/Dammam; the Security report says its retrieved Firestore page showed no Gulf region and that Realtime Database appears limited to US, Belgium, Singapore (indirect source). The Functions page itself says function regions do not always match database regions. | **[OPEN]** |
| Jordan "Cybersecurity" law number | Earlier search in this session returned a law-firm article (Clyde & Co, Oct 2023) stating that Electronic Crimes Law **No. 17 of 2023** was passed in August 2023. This supports suspicion that the Security report's "Cybersecurity Law No. 17 of 2023" is a mislabel. Cloud 5 cites Cybersecurity Law **No. 16 of 2019**. Neither was verified from primary text. | **[OPEN]** |

---

# A. UPDATED INDEPENDENT VERDICT

## A.1 Verdict

**NOT READY for implementation.** Implementation means building clinical features, migrating data, changing the live rules or functions, or touching any real patient data.

**READY to start Phase 0 now.** Phase 0 is decisions, evidence collection, and re-audit. It needs no new application code.

**Why the label did not change, but the reasons did.** My earlier verdict was NOT READY mainly because no evidence existed. That is no longer true. The six reports are serious, mostly consistent on principles, and honest about their own limits. The remaining blockers are **decisions and verifications**, not missing design thinking. That distinction matters for the owner: every blocker below can be closed without writing production code.

## A.2 What improved since my earlier review

| Earlier gap | Status now | Evidence |
|---|---|---|
| G-01 No evidence baseline | **Partly closed.** Six reports exist. Only the Security team read the ARGON-HEALTH repository (reported commit `fb6e3e38`, 2026-10-10). Nobody inspected the legacy Firebase code or live rules. | [FACT-R] Security §3.1; Cloud 2 §2; Cloud 3 §0.1; Cloud 4 §0.2; Cloud 6 §0.2 |
| G-03 Tenant-isolation specification | **Substantially advanced** (Cloud 2 §10, Security §6.4, Cloud 6 Area 6) but blocked by the unresolved storage-engine choice (UR-01). | [FACT-R] |
| G-06 Regulatory sources; Jordan breach timing | **Improved.** Security and Cloud 5 agree on 24 h to affected people and 72 h to the regulator for serious breaches (Art. 20, as reported). My earlier "conflict" item is superseded, with the caveat that it still rests on reports of the Arabic law's text. | [FACT-R] Security §4.1; Cloud 5 §5.5 |
| Penalty figures | The "up to JOD 1 million" claim from tertiary sources that I listed as a conflict is **rejected** by Cloud 5 (Appendix B) and not supported by Security's article-level extract (daily fines capped at 3% of prior-year revenue; JOD 1,000–10,000 criminal fines). | [FACT-R] |
| G-09 QA | **Advanced** (Cloud 6: 84 verification requirements, 160 test cases, gates). Not yet reconciled to the product requirements or to the chosen storage engine (UR-02, UR-34). | [FACT-R] |

## A.3 Blockers (each must close before the verdict can move)

| ID | Blocker | Why it blocks | Closed by |
|---|---|---|---|
| **B-1** | **Is real patient data already in the legacy live system, and are the earlier-reported P0 security weaknesses real?** The Security report and Cloud 5 describe a live Firebase system serving five clinics [FACT-R]. Cloud 5 itself flags this as conflicting with the one-clinic pilot premise. The Security report lists unverified P0 hypotheses (role self-escalation; password hashes readable; append-only bypass). | If true, Jordan's data-protection law already applies to live data, and the risks are live, not future. | Owner confirms facts; read-only re-audit of live rules/functions (Security AR-01, AR-02, Q-15) |
| **B-2** | **Storage-engine decision (SD-1) is open, and the reports contradict each other.** Cloud 2 and Security recommend hardening the current Firebase store for the pilot. Cloud 6 assumes PostgreSQL and database-level enforcement. Cloud 3 and Cloud 2 disagree on what Realtime Database transactions can do. | Test plan, integrity controls, and tenancy design depend on it. | Owner decision after an evidence spike (UR-01, UR-08) |
| **B-3** | **Hosting region and cross-border position (SD-2) is open.** Foreign hosting of Jordanian health data needs a legal determination (Art. 15 as reported). Gulf region availability for the data stores is unverified. | Residency is hard to change after data exists; can force a substrate change. | Jordanian counsel opinion; console evidence of every store's region |
| **B-4** | **Legal basis, roles, and consent model are unconfirmed.** Reports disagree on whether care processing needs consent. Controller/processor roles are unresolved. | Wrong data model and consent UI. | Counsel (UR-03, UR-06) |
| **B-5** | **Medical-device/software classification is undetermined in Jordan and Saudi Arabia**, and the deterministic drug-allergy alerts in Cloud 3 could matter. Cloud 5 did not research it. | Could add obligations that change scope. | Counsel/regulator (UR-26) |
| **B-6** | **$0/month is not shown to cover the P0 controls.** Security flags MFA, Cloud Functions, backups, legal review, and penetration testing as possibly unfunded. Cloud 5 says qualified legal review has no free substitute. | A P0 control that cannot be funded cannot be waived before real data. | Owner budget decision (UR-24) |
| **B-7** | **Pilot scope exceeds one developer's capacity as written.** Cloud 3 marks 140 of 184 requirements P0 and about 27 of 31 screens P0; Security marks 64 controls and 14 risks P0. P0 means different things in each report. | Nothing is plannable until a pilot slice is cut. | Owner/dentist scope decision (UR-16) |
| **B-8** | **No shared identifiers or single traceability.** Five different test catalogues, three gate vocabularies, and two screen numbering schemes exist. Four Cloud-3 screen groups have no Cloud-4 screen. | Cannot prove every requirement has a screen, an entity, a control, and a test. | §D of this report becomes the baseline (UR-14, UR-15, UR-34) |
| **B-9** | **ADR-024 (object-storage retrieval credentials) is not addressed by name in any of the six reports.** Images are core to dental care. Cloud 2 §12 and Security SEC-IMG-01…03 specify a design. Whether it replaces or satisfies ADR-024 is unknown. | Imaging path cannot be approved. | Security reviewer + owner (UR-27) |

## A.4 Path to a better verdict

**READY WITH CONDITIONS** requires: B-1, B-2, B-3, B-4, B-6, B-7, B-8 closed with evidence, and B-5 and B-9 at least assigned with a dated decision path. **READY FOR IMPLEMENTATION PLANNING** (unconditional) additionally requires counsel's written positions on residency, legal basis, and device status.

**Separate hard rule, independent of the verdict:** no real patient data may enter any new component until all P0 security controls have current evidence against one exact release candidate (Security SG-4, Cloud 6 G2). That rule is stricter than anything in this verdict.

## A.5 Strengths worth keeping

1. Append-only clinical and financial records with supersession (Cloud 2, Cloud 3, Security, Cloud 6 agree).
2. FDI tooth numbering as the storage key, other notations as display (Cloud 2, 3, 4, 6 agree).
3. Never auto-merge patients; reversible merges (Cloud 2, 3, 6).
4. One deployment cell per jurisdiction; no cross-border replication by default (Cloud 2, Security, Cloud 5).
5. No AI or autonomous clinical decisions in the pilot (Cloud 3, Cloud 6, Security).
6. Restore drills, not backup existence, as evidence (Cloud 2, Security, Cloud 6).
7. Generating authorization and tenant tests from one permission catalogue (Security, Cloud 6).
8. Honest evidence labelling in every report. Several reports refused to overclaim.

---

# B. UNIFIED CONTRADICTION AND DECISION REGISTER

**Status vocabulary.** **OPEN**: no resolution agreed. **PROPOSED**: this report proposes a resolution; the named approver has not decided. **SUPERSEDED**: a conflict reported earlier is resolved by later evidence (with caveat). No row is "closed" because no approver has decided anything.

Abbreviations: C2 Database, C3 Clinical, C4 UX/UI, C5 Regulatory, C6 QA, SEC Security, C7 my previous review. Approver roles: **Owner**, **Dentist** (lead dentist/clinical panel), **Counsel-JO**, **Counsel-KSA**, **Sec** (independent security reviewer), **Clinic-Op** (clinic owner/operator), **Tax** (accountant/tax adviser).

## B.1 Contradictions and incompatible recommendations

| ID | Conflicting reports | Exact issue | Risk | Recommended resolution [PROPOSAL] | Approver | Status |
|---|---|---|---|---|---|---|
| UR-01 | C2 §4.2 and SEC §5.2 vs C6 §2.3 (A-02), §14 Phase 1 | C2 recommends keeping the current Firebase store for the pilot (Path A+). SEC recommends hardening Firebase (Option A), conditional. C6 assumes **PostgreSQL** and plans real-PostgreSQL CI and database-level immutability tests. | Test plan not executable on the chosen store; integrity controls assumed that the store may not provide. | Owner decides SD-1 after a time-boxed evidence spike (§C.3). Until decided, parameterize every C6 database case per store (UR-02). Keep SEC's stop criteria and C2's DG-1 triggers as the exit to PostgreSQL. | Owner (+Sec) | OPEN |
| UR-02 | C6 §2.3 A-02, A-05, A-06; VR-DBI-05 vs C2, C4, SEC | C6 assumes no offline mode, no AI, PostgreSQL. C2, C4, SEC describe offline queues, drafts, RTDB. C6 states these cases must be reconciled when the product is inspected. | ~1/3 of C6 cases depend on unknown facts (C6's own estimate). | Re-baseline C6 after UR-01, UR-12 decided; keep stack-neutral wording; add substrate variants for DBI/TEN/BKP. | Sec + Owner | PROPOSED |
| UR-03 | C2 §3.1, C3 §1, C5 §5.3 vs SEC §4.1 (Art. 6(A)(2)) | C2/C3/C5 (secondary sources, Art. 6/7 text unread by C5) say prior consent is the primary basis. SEC reports primary text making care by a licensed practitioner lawful without consent, with consent needed for non-care purposes. | Consent-centric model built on the wrong basis, or consent wrongly treated as sufficient. | Model a **legal-basis register per purpose** separate from consent records. Treat clinical treatment consent (medical-liability duty) as a different thing from data-processing consent (UR-22). Counsel confirms. | Counsel-JO | OPEN |
| UR-04 | SEC §4.1 vs C5 §1 | SEC says it read the MODEE-hosted PDF with Arabic and English text and cites article numbers. C5 says the same PDF is a scanned image without extractable text, so its article numbers come from a law-firm summary. The two sets of article numbers (11, 14, 15, 20, 21–22) coincide, but may share a common source. | Controls rest on unverified article numbers. | Counsel obtains the official Arabic text and confirms articles; until then label them "reported". | Counsel-JO | OPEN |
| UR-05 | C7, C2 §3.1 vs SEC §4.1, C5 §5.5 | Earlier reports (C2, my C7) treated breach timing and penalties as conflicting. SEC and C5 now converge: serious breach → affected people within 24 h, regulator within 72 h; penalties per Art. 21–22 as reported. "JOD 1 million" is rejected (C5 App. B). | Wrong runbook clocks if the old conflict is kept. | Use 24 h / 72 h as the **working operational assumption**, held as a configurable parameter, pending counsel. | Counsel-JO | SUPERSEDED (caveat: UR-04) |
| UR-06 | C2 §7.2, SEC A-16 vs C5 §5.2 | C2 and SEC assume clinic = controller, ARGON = processor. C5 notes Jordan's definition keys on having data "under custody" and may make a hosting vendor a controller. | Contracts, DPO duties, liability misallocated. | Keep `controller_role` configurable per organization; draft a processor agreement; counsel decides. | Counsel-JO + Owner | OPEN |
| UR-07 | C2 §10 vs SEC/C6 A-03, legacy `clinicId` | C2: tenant = **organization** with clinics as branches. SEC/C6/legacy: tenant = **clinic**. | Mismatched isolation boundaries; wrong cross-branch sharing. | Carry both `organization_id` and `clinic_id` on every record. Isolation boundary = organization; branch scope inside. In the pilot map legacy `clinicId` 1:1 to organization. Cross-branch sharing default restrictive (C2 D-05). | Owner + Sec | PROPOSED |
| UR-08 | C2 §13.2 vs SEC §1.1(5), C3 R-ARCH-2 | C2 relies on client-side multi-path atomic `update()` plus rules validation on RTDB. SEC requires all sensitive writes (finance, audit, roles, finalized clinical) to go through trusted server functions; client rules deny them. C3 states RTDB lacks multi-path transactions, contradicting C2. | Integrity or privilege design that cannot work on the chosen store. | Adopt SEC: server-mediated writes for all P0 data. Resolve the RTDB capability dispute by an emulator-based evidence spike, not by assertion. | Sec + Owner | OPEN |
| UR-09 | C2 §7.3, §18.1 vs SEC SEC-CRY-06 | C2 specifies application-level encryption of national IDs and insurance numbers (`value_encrypted`) with external keys. SEC defers field-level encryption to P2 and relies on masking and isolation. | Either unneeded key-management burden or a larger breach blast radius. | Pilot: make national-ID capture optional; store matching hash and last-4; defer full encrypted value until D-03 (identifier policy) and a key-management design exist. | Sec + Owner | PROPOSED |
| UR-10 | C2 §16.4, C3 §15, SEC §5.7/§7.2 | Role sets differ (C2: `org_admin, clinic_admin, dentist, assistant, receptionist, billing, read_only_auditor`; C3: R, A, D, M, F, DPO, Pt). Cell conflicts: reception creates invoices and payments (C3) vs reads own-day invoices only (C2); merge by manager or dentist-in-charge (C3) vs clinic admin with second confirmation (C2); alert visibility for reception (C3 "presence") vs "limited" (C2). | Over-broad access; tests built on different matrices. | One permission catalogue (§C.4) from which UI, API, rules and tests are generated; clinic-signed matrix before any build (SEC-ROLE-01, C6 G2 #6). | Clinic-Op + Dentist | OPEN |
| UR-11 | C2 §14.1 vs C6 §9 G2(4) vs SEC AR-18 | C2: RPO ≤24 h (≤1 h with point-in-time recovery), RTO ≤8 h read-only / ≤24 h full. C6: RTO ≤4 h, RPO ≤24 h (≤15 min with archiving). SEC: unsigned. | Drill passes against the wrong target. | Clinic signs one RPO/RTO pair; all drills use it. | Clinic-Op | OPEN |
| UR-12 | C4 §7.6, S01–S18 states; C2 §12.2 vs C6 A-05 vs SEC SEC-CRY-05 | C4 holds drafts locally and queues writes offline. C2 queues encrypted offline media. C6 assumes no offline mode. SEC restricts persistent client-side PHI. C3 defers offline to another team. | PHI on shared PCs; untested sync conflicts. | Pilot: writes require connectivity; drafts autosaved server-side; paper downtime fallback. Any local draft needs Sec approval and encryption with a session-held key. Revise C4 offline states accordingly. | Clinic-Op + Sec | PROPOSED |
| UR-13 | C5 §1(3) vs SEC §1.1(7), §14.2 | Firestore Gulf-region availability: C5 says Doha/Dammam exist; SEC's retrieved page showed none. Realtime Database regions: SEC says only US/Belgium/Singapore (indirect source); C5 did not retrieve. This review confirmed only that **Cloud Functions** has Doha and Dammam (2nd gen) [FACT-W]. | Hosting decision built on wrong facts. | Read every store's actual region from the console (C5 REQ-HOST-01); check the official locations page for each product. | Owner (evidence) | OPEN |
| UR-14 | C2 phases/DG-1; C3 phases 0–7; C4 G0–G5; C5 G0–G5; C6 G0–G3; SEC SG-0…SG-5 | "G0" means five different things. | Wrong gate declared passed. | Adopt unified gates PG-0…PG-5 (§E.1) with a mapping table. | Owner | PROPOSED |
| UR-15 | All reports | ID collisions: `D-xx` (C2 vs C7), `Q-xx` (SEC vs C6), `S01` (C4 Login) vs `S-01` (C3 Patient search), `T-01` (C2 tests) vs `ST-01` (SEC) vs `TC-` (C6) vs `AT-` (C3) vs `TS-` (C5), `AC-xx`, `R-xx`. | Mis-traced requirements and tests. | Namespace prefix per source in all future work (e.g., `C3:S-13`). Use §D IDs as baseline. | Owner | PROPOSED |
| UR-16 | C3 App. E and §13 vs SEC §1.2 vs C6 A-11 | C3: 140 of 184 requirements P0; ~27 of 31 screens P0. SEC: 64 P0 controls, 14 P0 risks. C5 and C6 add more. "P0" means pilot-must-have in C3, release-blocking-before-real-data in SEC. One developer (SEC AR-07, C6 A-11). | Unplannable scope; shortcuts on safety items. | Define two tiers: **Safety/Legal-blocking** (cannot be waived) and **Pilot-scope** (cuttable). Owner and dentists approve a pilot slice (§C.2). | Owner + Dentist | OPEN |
| UR-17 | C3 §13 (31 screens) vs C4 §8 (18 screens) | C4 designs 18 screens. A keyword scan of C4 found **no** reference to consent capture, discharge, or break-glass. Diagnosis, procedure record, notes sign-off, recall, patient summary, audit viewer, catalogue admin and incident log are only embedded or partial. | Clinical workflows without UI; consent and discharge cannot be built from the design system. | Produce a C3↔C4 screen map; add missing screens (consent, discharge, audit/break-glass) to C4 before Phase 2. | Dentist + Owner | OPEN |
| UR-18 | C4 §2.3 vs C3 §1(5), S-28 vs C2 §17.3 | C4: an existing 128-code Jordanian fee-schedule catalogue plus doctor-scoped labels. C3: own versioned, dentist-approved catalogue, no licensed code sets. C2: organization-maintained list with `code_system`/`code`. Provenance and licence of the 128-code list are unstated. | Licensing exposure; three catalogue models. | One catalogue entity: `code_system`, `code`, version, approval metadata, effective dates. Confirm origin/licence of the 128 codes. | Dentist + Owner | OPEN |
| UR-19 | C4 §2.3 vs C2/C3/SEC append-only | C4 notes the legacy chart save is **destructive** and a newer `dental_history` is append-only; claims hold only `{role, clinicId}`, so doctor-vs-doctor isolation is UI convention. | Legacy chart overwrites; privacy implied but not enforced. | Wrap legacy save with conflict checks; migrate to append-only (C3 `imported_legacy` flag); do not imply per-doctor privacy until per-staff claims exist. | Owner + Sec | OPEN |
| UR-20 | C2 §7.5 vs C3 §6.3, FR-DX | C2 stores diagnosis as `clinical_note(kind=diagnosis)` plus optional ICD-10. C3 requires a separate `DIAGNOSIS` entity (status, basis, `discussed_with_patient`, dentist-only). | Missing structure for a core clinical concept. | Add `diagnosis` to the C2 model per C3. | Dentist | PROPOSED |
| UR-21 | C2 §9.3 vs C3 §5 | C3 has draft vs confirmed entries (assistants draft, dentist confirms), default `unknown_not_examined`, "exactly one active whole-tooth status". C2 has no draft state; dentition status is a finding category. | Assistant entries unreviewable; ambiguous projection. | Add `draft/confirmed` to findings; define whole-tooth status projection rule in the chart rule table. | Dentist | PROPOSED |
| UR-22 | C2 §7.3 consent purposes vs C3 §10 vs C5 REQ-CON-01 | Three consent taxonomies: C2 (treatment, data_processing, image_capture, marketing, data_sharing_external, cross_border_transfer); C3 (procedure-class consents, signatures); C5 (care, billing, reminders, marketing, analytics, offshore transfer). | One concept modelled three ways. | Two entities: `treatment_consent` (procedure/clinical, with signature evidence) and `privacy_basis_or_consent` (purpose-based, versioned). | Counsel-JO + Dentist | PROPOSED |
| UR-23 | C3 FR-IMG-01 (P0 DICOM upload) vs C2 §12.1, SEC §6.6, C6 A-10 | C3 lists DICOM (.dcm) upload as P0. C2, SEC, C6 treat DICOM/CBCT as outside the pilot. C3 §11.5 says P0 does not need a viewer. | Scope disagreement on imaging. | Pilot: JPEG/PNG/PDF only; DICOM as P1 behind a decision. Update C3 priority. | Dentist + Owner | PROPOSED |
| UR-24 | SEC AR-14, A-02, A-03; C5 §10.3; C2 §12.3; C6 R-06 | MFA may need a paid identity tier; trusted server functions may need a pay-as-you-go plan; legal review and independent testing have no free substitute. The brief says $0 and "justify any paid tool". | P0 controls unfunded; or a quiet $0 violation. | Owner decides explicitly: fund a named minimum, or no real patient data until it is funded. P0 controls cannot be risk-accepted for real data. | Owner | OPEN |
| UR-25 | SEC PRV-01, C5 §5.5, C3 Q-LEG-10 | A DPO is expected for the controller (sensitive data, minors, outside-Kingdom transfer). Whether a sole founder can be DPO is unresolved. | No accountable role at go-live. | Owner names a DPO candidate; counsel confirms eligibility. | Owner + Counsel-JO | OPEN |
| UR-26 | C3 Q-LEG-6, C6 G3(3), SEC Q-12 vs C5 "not researched" | Device status asked by three reports, researched by none for the dental EMR itself. C3 has deterministic drug-allergy alerts (WRN) that could count as decision support. My earlier research found SFDA digital-health guidance reported only by secondary sources. | Possible premarket obligations; scope change. | Written intended-use statement; counsel/regulator determination in each country; keep alerts rule-based and clinician-approved. | Counsel-JO + Counsel-KSA | OPEN |
| UR-27 | C7/owner context vs C2 §12, SEC SEC-IMG | ADR-024 (retrieval credentials) is not mentioned in any of the six reports. C2 §12.2 and SEC-IMG-01…03 define a design: private storage, short-lived (≤5 min, SEC) user-bound URLs minted after authorization. | Image path unapproved; possible duplicate or conflicting decision record. | Reconcile ADR-024 with C2 §12.2 and SEC-IMG-01…03 in one decision record. | Sec + Owner | OPEN |
| UR-28 | C2 D-09, C3 FR-BIL-08, C5 §5.8, C6 R-13 | Whether the pilot clinic must issue invoices through Jordan's national e-invoicing is unresolved (scope conflict in tertiary sources). C3 lists invoicing as P0. | Billing module built wrong. | Tax adviser's written answer before billing design is frozen; adapter pattern only. | Tax | OPEN |
| UR-29 | C2 §17.4, C5 §5.9, §6.8 | Jordan's national health record "Hakeem" and Saudi "NPHIES" obligations for a private dental clinic are not established by official sources. | Late rework. | Keep claims/insurance as adapter boundary only; discovery tasks T-07/T-08 (C5). | Counsel-JO + Counsel-KSA | OPEN |
| UR-30 | C5 §6.5 vs SEC AR-07, C6 A-11 | Remote access from Jordan to Saudi patient data is itself a transfer (C5). A single operator based in Jordan is assumed. | Saudi cell cannot be operated lawfully by the current model. | Saudi stays design-only; any Saudi operation needs a documented transfer basis and an in-Kingdom operating model. | Counsel-KSA + Owner | OPEN |
| UR-31 | SEC §4.1 vs C5 §5.10 vs earlier search | "Cybersecurity Law No. 17 of 2023" (SEC, by name) vs "Cybersecurity Law No. 16 of 2019" (C5). The number 17/2023 matches the Electronic Crimes Law in a law-firm article. | Wrong law cited in compliance mapping. | Treat SEC's citation as unsupported; counsel confirms the correct instruments. | Counsel-JO | OPEN |
| UR-32 | C2 §6–7 vs C3 §6.3, §14 | Entity-name and coverage mismatches (see §C.5 table). C2 lacks: `diagnosis`, `guardian_link`, `medication_statement`, `discharge_instruction`, `recall/follow-up task`, queue state, chair resource, condition catalogue, template catalogue, override log, incident log. C3 lacks: `outbox_event`, `patient_merge`, `patient_match_key`, `external_order`. | Two data models. | Merge into one canonical model (§C.5). | Dentist + Sec | PROPOSED |
| UR-33 | C2 §14.1 vs C5 REQ-RET-01, C6 BKP-006 | Backups kept 12 months (C2) while statutory retention is unknown in both countries; erasure must survive restore (C6). | Over-retention or premature deletion. | Retention is per-class configuration; no purge job enabled until counsel sets periods (SEC AR-24). | Counsel-JO | OPEN |
| UR-34 | C2 §21; C3 §20 (86 AT); C4 §13.4; C5 §13 (TS-); C6 §7 (160 TC); SEC §10.2 (51 ST) | Six test catalogues with no shared IDs. Tenancy alone is tested in C2 T-01…03, SEC ST-19…22, C6 TEN-001…010, C5 TS-10. C6's 84 VRs were written from the brief, not from C3's requirements (C6 Q-03). | Gaps hidden by apparent volume; duplicated effort. | Use §D as the master map; each property gets one owning test family; other catalogues cite it. | Owner + Sec | PROPOSED |
| UR-35 | C2 §20, SEC §12, C3 §21, C5 §12, C6 §9 | Five different pilot-readiness criteria sets, with proposed numeric thresholds (coverage ≥95 % Tier-1, mutation ≥70 %, etc.). | A pilot could pass one set and fail another. | Single go-live checklist = union of non-waivable items (§E, PG-4). Thresholds are proposals, approved by Owner + Sec. | Owner + Sec | PROPOSED |
| UR-36 | Brief ("synthetic data only", one pilot clinic) vs SEC §3.4, C5 A2, C4 §2.3 | Reports describe a live system already serving clinics. | See B-1. | Owner states the facts; read-only re-audit first. | Owner | OPEN |
| UR-37 | C3 §23 vs SEC §11 vs C2 §23 | C3 starts patient registry and roles in Phase 1 with no backup, isolation tests, or MFA step; SEC requires access control, tenant tests and CI first; C2 requires backup and one restore before any pilot data. | Features before safety nets. | Security foundations (PG-1) precede workflow phases. | Owner | PROPOSED |
| UR-38 | SEC AC-21 vs C6 SEC-013 | Both require an independent security assessment or a signed time-limited acceptance, at $0. | Duplicate effort or none. | One assessment plan serving both. | Owner | PROPOSED |
| UR-39 | C2 §18.1 vs SEC AC-02 | C2: MFA for admin, billing and export/merge roles. SEC: MFA for **every** staff account (P0). | Weaker control chosen by accident. | Adopt SEC's rule; feasibility under $0 is UR-24. | Sec + Owner | PROPOSED |

## B.2 Duplicated requirements (consolidate; do not build or test twice)

| Property | Where specified | Consolidated owner |
|---|---|---|
| Tenant isolation, negative tests | C2 §10, §21.1 (T-01…03); SEC-TEN-01…08, ST-19…22; C5 REQ-SEC-02, TS-10; C6 Area 6 (TEN-001…010); C3 §16 | One isolation specification and one test harness (§C.4) |
| Append-only clinical/financial data | C2 §11; C3 FR-ODO-05; SEC AC-07; C6 VR-DBI-05 | Data-model rule + one test family |
| Backup and restore drill | C2 §14, T-50…52; SEC-DR, ST-37…39; C5 REQ-SEC-05, TS-11; C6 Area 15 (BKP-001…008) | One runbook, one drill |
| Audit log and read auditing | C2 `audit_event`; SEC-AUD; C3 FR-AUD; C6 ATZ-009 | One audit design |
| Image upload/retrieval security | C2 §12; SEC-IMG-01…11; C3 §11; C6 Area 11 (FIL-001…011); C4 S13 | One storage design (UR-27) |
| Breach clocks | C2 §3.1; SEC-PRV-04; C5 REQ-BRE-01; C6 R-04 | One incident runbook |
| Role matrix | C2 §16.4; C3 §15; SEC §7.2; C4 §9.3 | One permission catalogue (UR-10) |
| Duplicate detection rules | C2 §8.2; C3 W-02/FR-DUP; C6 Area 7 | One matching specification |
| Money handling (minor units, JOD 3 decimals / SAR 2) | C2 §13.2; C4 decision 6; C6 VR-BIL-01 | One money module |
| AI disabled by default | C3 §2.3; SEC SEC-AI; C6 Area 18 | One policy (see UR-26) |

## B.3 Missing dependencies (no report owns them)

| ID | Missing dependency | Why it matters |
|---|---|---|
| MD-1 | Read-only inventory and re-audit of the **legacy** rules, functions, storage and data shapes (nobody inspected them) | Every Path-A claim is unverified; B-1 |
| MD-2 | Migration/coexistence plan from legacy chart and billing data to the unified model | C2 §17.1 outlines steps but no data inventory exists |
| MD-3 | Intended-use statement and device determination | UR-26 |
| MD-4 | Clinic endpoint inventory (PCs, Wi-Fi, imaging devices, vendor remote access) | SEC-IMG-11 and clinic hardening checklist need it |
| MD-5 | Named people: DPO, security reviewer, deputy for incidents, independent verifier, ≥2 dentists | Several gates require named roles |
| MD-6 | Radiation-protection rules for dental X-ray (JNRC/MoH) | Imaging workflow and logs (C3 R-LEG-4) |
| MD-7 | Prescription rules for dentists in Jordan | C3 Q-LEG-5 |
| MD-8 | Hosting provider terms recorded from provider documents (region, DPA, backups, SLA, data-use) | SEC-HOST-05; no free-tier terms were verified by anyone |
| MD-9 | A single synthetic-data generator and fixture set shared by all test catalogues | C6 DS-00…13 exist; C2, C3, C4 each define their own fixtures |
| MD-10 | Support and operations model (who answers an alert at night; deputy) | 24 h/72 h clocks |

## B.4 Unsupported or doubtful claims found

| ID | Report | Claim | Problem |
|---|---|---|---|
| UC-1 | C3 R-ARCH-2 | RTDB has no multi-path transactions | Contradicts C2's design basis; unverified |
| UC-2 | C2 §13.2 | Multi-path atomic update plus rules gives billing integrity at single-clinic scale | Unverified; depends on UR-08 |
| UC-3 | SEC §4.1 | "Cybersecurity Law No. 17 of 2023" | Likely mislabel (UR-31) |
| UC-4 | SEC §1.1(7), §14.2 | RTDB locations limited to US/Belgium/Singapore | Indirect source; contradicted in part by C5 for Firestore |
| UC-5 | C5 §1(3) | Firestore offers Doha/Dammam | Only Functions confirmed here [FACT-W] |
| UC-6 | C6 §9 | Thresholds (coverage 95 %, mutation 70 %, RTO 4 h) | Proposals, not requirements; no basis stated |
| UC-7 | SEC §3.4 | Legacy P0 flaws (self-escalation, readable password hashes, cascade bypass) | The Security team itself calls them unverified hypotheses |
| UC-8 | C2, C3, C4, C6 | Statements about "existing" ARGON features (128-code catalogue, billing engine with FIFO allocation, dedup engine) | All documented design, none inspected |
| UC-9 | C7 (my earlier review) | Treating the Jordan breach and penalty facts as conflicting | Superseded by UR-05, with caveat |

---

# C. UNIFIED ARCHITECTURE RECOMMENDATION

All of this is **[PROPOSAL]**. Where a recommendation depends on an open decision, the dependency is named. Nothing here claims that any component exists.

## C.1 Principles agreed across the seven reports

1. Modular monolith for the pilot. No microservices, no service mesh, no per-tenant databases (C2 §4.1, §15.4).
2. Server-side authority for identity, role, clinic membership and tenant. UI hiding is not a control (SEC P-1, C2 §5).
3. Append-only truth for clinical and financial data; corrections supersede (C2 §11, C3 §1, SEC P-4).
4. Pilot profile: only components with a written reason. Cache, message bus, search cluster, warehouse are **deferred** (C2 §15.4; SEC does not require them).
5. One deployment cell per jurisdiction (SEC P-10, C2 §3.3, C5 REQ-HOST-03).
6. Synthetic data only outside an approved production environment (all reports).
7. Evolve the existing repositories; any storage change is staged, additive, reversible (SEC P-8, C4 §2.3, C5 §11).

## C.2 Proposed pilot slice (for Dentist and Owner approval; resolves UR-16)

| Tier | Capability | Notes |
|---|---|---|
| **In pilot slice** | Staff sign-in with MFA; roles; audit | Security foundation |
| | Patient registration; duplicate warning (no merge yet) | C3 S-02, S-03 review part |
| | Medical history, allergies, medications | C3 W-03/W-04 |
| | Calendar, appointment, reception check-in and queue | C3 S-07/08/10 |
| | Visit workspace; examination; odontogram; diagnosis | C3 W-07…W-11 |
| | Treatment plan; procedure record; clinical notes with sign-off | C3 W-12/13 |
| | Treatment consent capture | Needs a C4 screen (UR-17) |
| | Images and attachments: JPEG/PNG/PDF only | UR-23, UR-27 |
| | Invoices and payments as **internal** records | Subject to Tax answer (UR-28); no national e-invoicing adapter |
| | Basic discharge instructions | Needs a C4 screen |
| | Prescription **printing with manual allergy-check flag** | Automated alert rules wait for dentist-approved content and device determination (UR-26) |
| **Deferred to a later gate** | Patient merge/unmerge; waitlist; recall outreach; patient summary export; reports beyond operational; periodontal charting; DICOM/CBCT; insurance claims; e-invoicing adapter; messaging; patient portal; AI | Each needs its own decision |

## C.3 Component recommendations

### Frontend
- **Keep** the existing web/PWA client; **no framework rewrite** (C2 §1, C4 §2.3, C4 decision 10) **[PROPOSAL]**.
- Ship the C4 design system as an **additive layer**; fix the documented contrast defects first (C4 decision 2).
- Odontogram: SVG, fixed FDI "dentist's view" layout in both languages (C4 decision 5), pending dentist confirmation. Display notation switch is presentation only (C2 §9.2, C3 §4.2).
- Arabic RTL and English LTR; Western digits in data; tooth numbers and doses in LTR isolates (C4 decision 6; C3 AT-I18N-1; C6 Area 12).
- Persistent patient banner with two identifiers and alert indicator (C2 §8.3, C3 §13, C4 decision 8).
- **Offline:** writes need connectivity; autosave drafts on the server; paper downtime kit (UR-12). Any local draft needs Sec approval.
- No third-party analytics, fonts from CDNs, or SDKs that touch clinical screens (SEC-HOST-07; C4 decision 7 self-hosts fonts).

### Backend
- **Modular monolith** with C2 §16.2 modules: identity and tenancy; patient registry; scheduling; clinical; dental chart and treatment; billing; media; audit and consent. Modules call each other's interface, never each other's storage.
- Every sensitive write goes through **trusted server code** that authorizes, validates, writes, and audits (SEC §5.3; UR-08).
- Money in integer minor units with currency and exponent: JOD three decimals, SAR two (C2, C4, C6) — the exponent values are **[ASSUMPTION]** until implementation confirms ISO 4217 handling.
- Idempotency keys on creates; optimistic concurrency on drafts; outbox only when an integration exists (C2 §13.2). No message bus in the pilot.
- Country behaviour (calendar, coding, retention, notices, tax adapter) is **configuration plus adapters**, not code branches (C5 REQ-I18N-01, C2 §3.3).

### Database
Two realizations of one logical model. Choice is Owner decision SD-1.

| | Option A — Harden current Firebase store (conditional) | Option B — Relational engine (PostgreSQL-class) |
|---|---|---|
| Position in reports | C2 Path A+; SEC Option A "recommended for Jordan pilot, conditional" | C2 Path B (target, triggered by DG-1); SEC "not recommended for pilot"; C6 assumes it |
| Integrity | Server-mediated atomic writes; scheduled reconciliation | Constraints, transactions, row-level security |
| Residency | Region of **each** store unverified (UR-13) | Provider/region choice open |
| Cost | Server functions may need a paid plan (UR-24) | Free tiers small; operations burden on one person (SEC §5.2) |
| Evidence needed before choosing | Emulator spike proving: atomic multi-path billing writes; append-only enforcement incl. rule cascade; per-staff authorization; tenant isolation on every path | Provider terms; backup/PITR on free tier; operations plan |
| Stop criteria to move A→B | Any C2 DG-1 trigger; a confirmed P0 finding that cannot be fixed in rules/functions; residency opinion requires a region the store does not offer | — |

**Recommendation [PROPOSAL]:** do not start building on either until the evidence spike and counsel's residency answer exist. Prefer Option A **only if** the spike passes and a lawful region exists; otherwise Option B staged by the strangler pattern in C2 §4.3. This respects "preserve and improve; rebuild only with evidence".

### Identity and authorization
- Vetted identity provider; no home-made password storage (C2 §18.1).
- **MFA for every staff account** in the pilot (SEC AC-02 P0). C2 §18.1 limits MFA to admin/billing/export roles — **conflict UR-39**; adopt SEC's stricter rule. Feasibility under $0 is open (UR-24).
- Roles are claims set only by trusted code; membership lives in a server-only path (SEC §5.3). Add per-staff identity so doctor-level rules can be enforced (UR-19).
- Single **permission catalogue** (resource × action × role × condition, versioned). UI, API checks, data-layer rules and generated ALLOW/DENY tests all read from it (SEC P-2; C6 VR-ATZ-01).
- Deny by default; step-up for recovery; break-glass with typed reason, alert and review (C2 §10.4, SEC §5.6, C3 §15).
- Operator separation: ARGON operator identities are separate from clinic users; no standing production PHI access (SEC-INS-06).

### Tenant isolation
Boundary = `organization_id`, scope inside = `clinic_id` (UR-07). Required per store **in the pilot profile**:

| Store (pilot) | Required isolation control | Test families |
|---|---|---|
| Primary database | Tenant key on every record; data layer denies cross-tenant access independent of app code; no root-level queries or shared indexes | C6 TEN-001…010; SEC ST-19…22; C2 T-01…03 |
| Object storage | Tenant-prefixed opaque keys; private; short-lived user-bound access minted after authorization | C6 FIL-005/006/011; SEC ST-20/34 |
| Audit store | Server-write-only; tenant-scoped reads; no clinical content | C6 ATZ-009; SEC ST-30…32 |
| Backups/exports | Per-tenant partition; separate credential domain | C6 BKP-003/005; SEC ST-37 |
| Logs/telemetry | No patient identifiers; canary test | C6 SEC-007; SEC ST-40 |
| Deferred stores (cache, bus, search, warehouse) | **Not provisioned.** Re-admission needs an ADR with a measured trigger and a per-store isolation spec | — |

### Clinical data
- Four separate concepts: finding, diagnosis, plan item, procedure (C3 §1(2)); invoices only from performed procedures (C2 §6).
- Medical history is versioned, with `none / yes / not asked / declined` — blank is not "no" (C3 S-04).
- Allergies append-only with status; allergy banner visible wherever prescribing or anaesthesia is possible (C2 §18.3).
- Prescription is immutable after issue; dose text is clinician-entered; the system does not calculate doses (C2 §7.6).
- Guardian relationship model for minors before any minor's record is created (SEC AR-21; C3 `GUARDIAN_LINK`).
- Retention is per-record-class configuration; **no hard-coded period**; purge disabled until counsel sets periods (C5 REQ-RET-01, SEC AR-24).

### Dental odontogram
- Canonical storage key: FDI two-digit text (`"16"`), validated by dentition; display notation is a user setting (C2 §9.2; C3 §4.2).
- Chart = projection of append-only entries with `effective_date` and `recorded_at`; "as of date" supported (C2 §9.1; C3 §5).
- Entries carry `draft/confirmed` state (UR-21), reason on correction, superseded entries always visible in the tooth timeline (C3 S-14).
- Surfaces stored as a controlled set; validity rules by tooth type (C3 AT-SURF-1: `O` on a canine rejected).
- Supernumerary and special cases need a **dentist-approved slot-key format** (C2 D-08, C3 Q-CLIN-8) — **[OPEN]**; do not invent.
- Periodontal charting deferred (C2 D-07).
- Clinical value lists are authored and approved by a dentist, not engineering (C2 §9.1, C3 §19).

### Imaging and file storage
- Pilot types: JPEG, PNG, PDF. DICOM/CBCT deferred (UR-23).
- Private storage, opaque tenant-prefixed keys, short-lived (≤5 min proposed by SEC) user-bound URLs minted after authorization and consent check, every issuance audited (C2 §12.2; SEC-IMG-01…03).
- Server-side validation by file signature, size caps, allow-list; strip location data from non-diagnostic photos; **keep the original radiograph unaltered** and derive viewer copies separately (C2 §12.4; SEC-IMG-04/06; C3 S-20).
- SHA-256 stored at upload and verified on export and in restore drills (SEC-IMG-07).
- **Patient uploads disabled** in the pilot until a scanning path exists (SEC-IMG-05).
- Compression, quotas and volume estimate are decisions (C2 D-10); free-storage limits are **unverified** (C2 §12.3).
- Image identity safeguards: laterality marker check and wrong-patient block (C3 §11.4, WRN-12).
- Reconcile with ADR-024 in one record (UR-27).

### Audit
- Server-written, append-only, hash-chained `audit_event` with daily digest anchored outside the production credential domain (SEC §5.3, AUD controls).
- Records reads, writes, exports, merges, role changes, break-glass; **no clinical content** (C2 §7.9).
- High-risk operations **fail closed** if audit cannot be written (SEC P-6; AC-09).
- Patient-facing access log and reviewer view are P1 (C3 S-27; SEC-AUD-07).

### Backup and recovery
- Platform-native protection **plus** an independent encrypted off-platform backup in a **different account/provider and credential domain**; keys held outside production, two custodians (C2 §14.2; SEC-CRY-04, AR-04).
- At least one copy not deletable with production or operator credentials (C2 §14.2(5); SEC AC-15).
- Monthly restore into an isolated environment with a verification script (counts, referential checks, reconciliation, chart rebuild) (C2; C6 BKP-001/002/008).
- Tenant-level restore proven not to alter other tenants (C6 BKP-005).
- **One RPO/RTO pair signed by the clinic** (UR-11). Proposed starting values are C2's (RPO ≤24 h; RTO ≤8 h read-only, ≤24 h full) and C6's tighter RTO ≤4 h — **[OPEN]**.
- Runbooks: accidental deletion, corruption, provider outage, credential compromise, ransomware; paper day-sheet fallback (C2 §14.2(8); SEC-DR-07).

### Hosting and country separation
- **Cell per jurisdiction**: separate project/stack, data, keys, backups and operator access; no cross-border replication by default (SEC-HOST-04; C2 §3.3).
- Global control plane holds **no patient-identifiable data** (tenant registry, release channel, SaaS billing metadata only) unless counsel approves more **[PROPOSAL]**.
- **Jordan cell:** region per SD-2: (i) non-Gulf region with a legal determination under Art. 15/11/14 as reported; (ii) a Middle East region if verified for each service and affordable; (iii) clinic-local storage for images with cloud metadata. **No default assumed** (SEC §5.2).
- **Saudi cell:** design-only. Planning assumption from C5: in-Kingdom hosting and backups, no Jordan-based standing access without a documented transfer basis; no Saudi production PHI until a Saudi legal determination exists (SEC-HOST-04; C5 §6.5).
- Data inventory and flow map of every store and every third party (SEC-HOST-01). CDN/WAF proxies that terminate TLS count as processors in the path (SEC-HOST-06).

## C.4 Permission catalogue — starting roles (needs clinic and dentist signature)

| Unified role | Maps from | Notes |
|---|---|---|
| `platform_operator` | SEC operator plane | Separate identities; break-glass only; clinic-visible access |
| `org_admin` | C2 | Controls org settings; MFA |
| `clinic_manager` | C2 `clinic_admin`; C3 M | Merge, catalogue approval, user admin |
| `dentist` | C2, C3 D | Diagnosis, plans, procedures, prescriptions, sign-off |
| `assistant_hygienist` | C2 `assistant`; C3 A | Drafts entries; scope of practice is **[OPEN]** (C3 Q-LEG-7) |
| `receptionist` | C2, C3 R | Demographics, scheduling; alert **presence** only |
| `finance` | C2 `billing`; C3 F | Invoices, payments, price list |
| `auditor_dpo` | C2 `read_only_auditor`; C3 DPO | Audit read; no clinical edit |
| `patient` | C3 Pt | Future; not in pilot |

Disputed cells to settle at signature: reception creating invoices/payments; who merges; reception alert visibility; whether finance sees clinical text (UR-10).

## C.5 Canonical entity map (merge of C2 and C3; resolves UR-32)

| Concept | C2 name | C3 name | Unified action |
|---|---|---|---|
| Patient | `patient` | `PATIENT` | Keep C2 fields (MRN, AR+EN names) |
| Identifier | `patient_identifier` | `PATIENT_IDENTIFIER` | Keep; optional in pilot (UR-09) |
| Guardian | `patient_contact(kind=guardian)` | `GUARDIAN_LINK` | **Add** `guardian_link` with authority and consent scope |
| Medical history | `history_entry` | `MEDICAL_HISTORY_VERSION` | Use versioned form with review status |
| Medications | `history_entry(kind=medication_current)` | `MEDICATION_STATEMENT` | **Add** `medication_statement` |
| Allergy | `allergy` | `ALLERGY` | Keep |
| Appointment / visit | `appointment`, `visit` | same | Keep; **add** queue state, chair resource |
| Chart event | `tooth_finding` | `CHART_ENTRY` | One entity; add `draft/confirmed` (UR-21) |
| Diagnosis | note kind | `DIAGNOSIS` | **Add** (UR-20) |
| Notes | `clinical_note` | `CLINICAL_NOTE` | Keep; sign-off state |
| Plan / item | `treatment_plan`, `plan_item` | same | Keep |
| Procedure | `procedure_performed` | `PROCEDURE_RECORD` | Keep one |
| Prescription | `prescription`, `_item` | `PRESCRIPTION` | Keep |
| Media | `media_asset` | `IMAGE_ASSET` | Keep `media_asset`; add laterality, import-verification fields |
| Consent | `consent_record` | `CONSENT_RECORD` | Split per UR-22 |
| Discharge | — | `DISCHARGE_INSTRUCTION` | **Add** |
| Follow-up / recall | — | follow-up task | **Add** |
| Catalogues/templates | `price_list_item` only | catalogues | **Add** versioned condition, procedure and template catalogues |
| Override/incident log | — | incident/correction log | **Add** |
| Billing | `invoice`, `payment`, `payment_allocation`, claims | `INVOICE`, `PAYMENT` | Keep C2; claims deferred |
| Audit | `audit_event` | audit | Keep C2 |
| Merge / match key | `patient_merge`, `patient_match_key` | — | Keep; merge deferred |
| Outbox / external order | `outbox_event`, `external_order` | — | Define now, do not use in pilot |
