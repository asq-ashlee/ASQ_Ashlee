# Artwork Studio bridge: private read-only Cloud Run slice

Status: draft code, not deployed. This service is not connected to the Artwork Studio.

The only data endpoint is `GET /v1/artworks/identity` with at least one of
`artwork_id`, `title`, or `slug`. It returns `existing`, `ambiguous`,
or `clear` and the GitHub blob SHA checked. `clear` is **not** approval to
create artwork. There are no write, image, Firestore, Lovable, or publish routes.

## Client-owned deployment

For Arts of August, use the Google Cloud project shown in the client's console:

- Organization shown: `artsofaugust.org`
- Project display name: `Arts of August OS`
- Project ID: `stoked-proxy-502319-c4`
- Project number: `1032949592191`

The final IAP audience can be filled in after choosing the region and Cloud Run
service name: `/projects/1032949592191/locations/REGION/services/SERVICE_NAME`.
These identifiers are configuration values, not credentials. The screenshot does
not establish whether the existing Firestore database lives in this project;
verify that before adding Firestore access or deploying.

Each future artist/customer should own a separate Google Cloud project (or
isolated account under their control), service identity, IAM policy, secrets,
billing, and data/asset permissions. Reuse the reviewed bridge code as a
versioned template, with explicit customer-specific configuration. Do not
share a GitHub credential, IAP allowlist, Drive folder, Firestore instance, or
operational artwork data across customers. A customer's public site remains
their presentation layer, and their existing governed records remain their
source of truth.

The console screenshot shows a free-trial balance and 26 days remaining at
capture time. Confirm the billing plan and expected spend before deploying a
billable service; this draft does not create resources or incur cloud charges.

## Security boundary

- Deploy Cloud Run with **Require authentication → Identity-Aware Proxy (IAP)**.
  Grant IAP access only to the intended artist/operator accounts. Do not deploy
  with public access or disable IAP.
- Set `AOA_IAP_AUDIENCE` to the signed-header audience for this exact Cloud Run
  service: `/projects/PROJECT_NUMBER/locations/REGION/services/SERVICE_NAME`.
- Set `AOA_ALLOWED_EMAILS` to the explicitly permitted Google account emails.
  Both IAP policy and the service's signed-JWT verification/allowlist must pass.
  A missing audience or allowlist makes the data endpoint unavailable.
- Supply `AOA_GITHUB_TOKEN` from Google Secret Manager to the Cloud Run service
  identity. Use a read-only, repository-scoped credential and give the service
  identity access to that secret only. Do not commit or browser-expose the token.
- The fixed GitHub path is the existing governed `artworks.csv` on `main`.
  Each request fetches the current file; a failed read returns an error, never
  an assumed `clear`.
- Cloud Run's service account does not inherit the current ChatGPT connection's
  access to GitHub or Drive.

## Local check

From this directory, run:

```sh
python -m unittest -v test_bridge_identity.py test_github_artwork_source.py test_bridge_service.py
```

Tests mock the GitHub read and IAP assertion. They do not prove deployment
settings, browser sign-in, or live GitHub permissions. The reviewed Lovable
listing for Eastern Trail Marsh is the existing-artwork test case.

## Deployment readiness

The WSGI entry point is `bridge_service:application`. Build
`bridge-Dockerfile` with this directory as the Docker build context. Before
deployment, confirm this project is the intended owner and verify its existing
Firestore relationship. Confirm IAP OAuth setup for Kaleigh's account, GitHub credential ownership, region,
and browser access strategy. Configure Secret Manager and IAP in Google Cloud
outside the code review. Do not route the Sites prototype to this endpoint until
cross-origin sign-in and request authorization are verified.
