# Arts of August — client repository and integration plan

Status: planning and migration preparation; no repository, service, database, or publication has been changed by this plan.
Prepared: September 17, 2026

## Decision

Create a private, client-owned GitHub repository for Arts of August. It will hold Kaleigh's governed operational records, rules, client configuration, and the code needed for her bridge. Keep reusable, client-neutral implementation in an ASQ-maintained starter or shared component. Do not mirror the entire ASQ repository into clients.

Artwork Studio remains the artist-facing interface. Its future bridge runs in Kaleigh's Google Cloud project `stoked-proxy-502319-c4`, authenticates Kaleigh, calls the governed AOA workflow, and coordinates approved changes to Kaleigh's GitHub records, Google Drive originals/masters, Firestore live records, and the existing Lovable public website. Each approval and publication remains a separate explicit action.

## Current state and sources

- ASQ GitHub source: https://github.com/asq-ashlee/ASQ_Ashlee/tree/main/ASQ_Freelance/Arts_of_August_System
- Older Drive workspace copy: https://drive.google.com/drive/folders/10E_44sCtfn62kM3BgJqDa2KG3vzAvKms
- Current draft bridge work: https://github.com/asq-ashlee/ASQ_Ashlee/pull/1
- Kaleigh's Google Cloud project: `stoked-proxy-502319-c4`; Firestore `(default)`; Google sign-in has been tested at Artwork Studio's private auth-check page.
- No client GitHub repository or Cloud Run service was visible during this review. The Site-to-bridge connection and publication workflow are not live.

The Drive folder is a copy of files, not a Git remote. It includes an older Lovable app and historical exports; it should not be used as a blind clone. ASQ's current GitHub repository is public, so review client records and historical content before copying to or continuing to maintain them there.

## Boundary of each account

| ASQ-controlled | Kaleigh-controlled |
| --- | --- |
| Reusable starter, shared bridge improvements, deployment guidance, general tests | Private Arts of August repo with her authoritative CSV records, client rules, and approved change history |
| Proposed updates sent as reviewed pull requests | Her Google Cloud project, Firestore and service identity |
| No production client credentials or artwork records | Her Drive canonical originals/masters; her existing Lovable website and payment links |

A starter/template creates a client repository once; it does not continuously synchronize it. A later shared release should produce a reviewable pull request in each client repo, with client configuration and data excluded from bulk updates. Never force-push a mirror over client changes.

## What to move for Kaleigh

1. Adapt the AOA `README.md`, `AOA_WORKFLOW_INDEX.md`, `AOA_UPDATE_WORKFLOW.md`, `AOA_DATABASE_MAP.md`, `AOA_RELATION_RULES.md`, and relevant `AOA_SYSTEM/` rules. Remove ASQ-wide identity instructions that are not Kaleigh-specific.
2. Move the authoritative `AOA_datasets/` master CSVs, schemas, and approved per-artwork records only after checking which records are current. Preserve stable artwork IDs and relationships. Do not treat the raw root-level Notion exports as additional masters.
3. Move the applicable `AOA_artwork-lab/` intake, photography/master, approval and listing guidance. Review `AOA_source-intelligence/`, `AOA_product-studio/`, and `AOA_distribution-studio/` individually rather than copying placeholders as live automation.
4. Move approved `AOA_connecting-layer/` contracts and production-ready bridge code with focused tests after draft PR #1 is reviewed. The current draft bridge references `asq-ashlee/ASQ_Ashlee`; make repository and dataset path client-specific before deployment.
5. Move only necessary `scripts/` and update their paths. Keep original-resolution files and canonical image assets in the designated client Drive location, with stable references in records.
6. Leave `AOA_exports/`, raw Etsy/Notion downloads, scratch logs, local editor settings, duplicate CSV copies, temporary test assets, and any `.env` or credential material out of the new repository. Archive historical files in client Drive if they are needed.
7. Treat `AOA_Website_Loveable/` as an older site copy. Do not deploy it as a replacement for the existing public site without an independent website reconciliation.

## Migration sequence

1. **Ownership:** Kaleigh creates or identifies her GitHub account. Create a private repository such as `arts-of-august-system` under her account, add Ashlee as a collaborator with the access needed to maintain it, and enable two-factor authentication. Do not select the public ASQ monorepo in Cloud Build.
2. **Inventory:** Compare current GitHub `main`, draft PR #1, the Drive copy, Firestore, and the existing public site. Record source path, destination path, record counts, stable IDs, and conflicts in a migration checklist. Identify the single master for every dataset.
3. **Seed:** Copy the reviewed AOA subset into a branch of the private repo. Rewrite README, paths, service names, and configuration. Do not add secrets. Review the diff and merge the initial seed after record reconciliation.
4. **Cutover:** Point the bridge's read configuration to the new client repo and verify a read-only list and one artwork against the current records. Make exactly one repo writable as the governed master; stop writes to the old ASQ location before enabling writes in the new location.
5. **Bridge:** Complete review of PR #1; deploy the bridge to Kaleigh's Cloud Run project with least-privilege service identity and secret storage for any non-Google credentials. Restrict calls to authenticated authorized artists; confirm logs and failure behavior. The Studio should not claim a write or publication succeeded until verified by the bridge.
6. **Artist workflow:** Add draft intake and image transfer, deterministic canonical master approval, review approval, preparation, website preview, separate publication approval, and verified live confirmation in stages. Drive holds images, GitHub holds governed records, Firestore remains the live application database, and the existing Lovable site stays the storefront.
7. **Reusable client pattern:** Extract generic bridge code and setup instructions to an ASQ starter/shared component. Issue versioned changes and propose a pull request to each client. Test each client's configuration before merging/deploying; never distribute one client's records or credentials to another.

## Immediate next action

Create the empty private repository in Kaleigh's GitHub account and invite `asq-ashlee` as collaborator. Share its repository URL. Then prepare the source-to-destination migration checklist and initial branch; reconcile records before any cutover or Cloud Run deployment.

## Gates

- No second writable master during migration.
- No original artwork image or secret in Git.
- No automatic publishing from merely approving a master or artwork.
- Existing Firestore and public site remain authoritative for live state until a verified, explicitly approved cutover.
