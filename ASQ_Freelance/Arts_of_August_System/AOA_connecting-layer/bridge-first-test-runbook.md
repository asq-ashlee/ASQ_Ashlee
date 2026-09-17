# Historical IAP runbook — superseded

The Firebase sign-in proof succeeded. Do not use the IAP steps below to deploy the current artist-facing bridge. Follow `bridge-cloud-run.md` for the Firebase-token architecture. This section is retained as historical planning context.

# First private read-only bridge test — operator runbook

Status: superseded as a deployment sequence pending the authentication decision in `bridge-auth-decision.md`. Use the fixed values as reference only. No Cloud Run service, secrets, or Site connection exists yet. The IAP setup below remains an optional private technical rehearsal, not the chosen artist-facing browser path.

## Fixed values

| Setting | Value |
| --- | --- |
| Google Cloud project ID | `stoked-proxy-502319-c4` |
| Google Cloud project number | `1032949592191` |
| Existing Firestore database | `(default)`, Firestore Native, `nam5` |
| First tester | `ashlee@asqashlee.xyz` |
| Test listing | `AOA-ART-0065`, Eastern Trail Marsh |
| GitHub source | `asq-ashlee/ASQ_Ashlee`, `main`, governed `artworks.csv` |
| Cloud Run service name | `aoa-artwork-bridge-readonly` (proposed; confirm before setting IAP audience) |
| Cloud Run region | Select during deployment; keep `AOA_IAP_AUDIENCE` consistent with it |

## Cloud setup, in order

1. In the Arts of August OS Google Cloud project, verify billing/trial status and set a modest budget alert before deployment. Confirm who administers the project and can grant IAP access.
2. Create a dedicated Cloud Run service identity for this client and enable only APIs needed for Cloud Run, Artifact Registry/build, Secret Manager, and IAP. No Firestore or Drive role is needed for this read-only slice.
3. Create a fine-grained GitHub credential for the existing repository with **Contents: read-only** and a short expiry, owned by an account authorized to access the repo. Store it directly in this project's Secret Manager as `aoa-github-readonly`; never paste it into chat, source code, or the Site. Grant the dedicated service identity access to that one secret. A GitHub App installation is the preferable longer-term credential design.
4. Build the container from the `AOA_connecting-layer` directory using `bridge-Dockerfile` and deploy it as a new Cloud Run service with **Require authentication → IAP**. Do not enable public access. If the project has no Google organization, Google recommends using the Cloud Console for the initial IAP OAuth setup. Since Ashlee's email is outside `artsofaugust.org`, configure external-user OAuth access and grant only `ashlee@asqashlee.xyz` IAP access to this service.
5. Configure the service with `AOA_ALLOWED_EMAILS=ashlee@asqashlee.xyz`, `AOA_IAP_AUDIENCE=/projects/1032949592191/locations/REGION/services/aoa-artwork-bridge-readonly`, and `AOA_GITHUB_TOKEN` as a Secret Manager reference. Substitute the actual deployed region and verify the signed-header audience shown in IAP settings. Never put these values in a browser bundle; the token must remain server-only.
6. Test an authenticated GET to `/v1/artworks/identity?artwork_id=AOA-ART-0065&slug=eastern-trail-marsh`. Expected: `existing` and the governed source revision. Test an unapproved account and missing assertion: both must be denied. Test an unknown title: `clear` means only that no index match was found; it does not start a workflow.
7. Review Cloud Run and GitHub logs for errors, check the revision returned, and confirm that no repo, Firestore, Drive, or Lovable write occurred. Keep the Sites prototype disconnected until browser sign-in/CORS is proven and a new artwork intake path is governed.

## Acceptance gate

The read-only rehearsal passes only when the live service authenticates Ashlee, reads the current governed CSV with its own secret, returns `existing` for Eastern Trail Marsh, and denies unauthorized requests. A local mocked test or a successful deployment alone does not satisfy this gate.

## Current access limit

Codex can prepare code and inspect connected GitHub/Drive/Lovable resources here. There is no connected Google Cloud administration tool in this session, so cloud setup and deployment must be done by a project administrator or through a separately authorized execution path. Do not send Cloud credentials in chat.
