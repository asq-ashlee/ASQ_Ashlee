# Artwork Studio bridge: private read-only Cloud Run slice

Status: draft code, not deployed. This service is not connected to the Artwork Studio.

The only data endpoint is `GET /v1/artworks/identity` with at least one of
`artwork_id`, `title`, or `slug`. It returns `existing`, `ambiguous`,
or `clear` and the GitHub blob SHA checked. `clear` is **not** approval to
create artwork. There are no write, image, Firestore, Lovable, or publish routes.

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
deployment, confirm the Google Cloud project,
IAP OAuth setup for Kaleigh's account, GitHub credential ownership, region,
and browser access strategy. Configure Secret Manager and IAP in Google Cloud
outside the code review. Do not route the Sites prototype to this endpoint until
cross-origin sign-in and request authorization are verified.
