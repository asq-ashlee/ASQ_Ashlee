# Artwork Studio bridge: Firebase authenticated, read-only Cloud Run slice

Status: draft code in review, not deployed. The Site's Google sign-in has been
verified for Ashlee, but the bridge is not connected to the Site.

## Contract

- `GET /v1/session`: validates the Firebase ID token and approved identity;
  returns a minimal ready state and email. No GitHub credential is needed.
- `GET /v1/artworks/identity?title=...`: verifies the same identity, then
  checks the current governed GitHub `artworks.csv`. Returns `existing`,
  `ambiguous`, or `clear` and the GitHub blob SHA. `clear` is not
  permission to create an artwork.
- `GET /healthz`: process health only, with no data.
- No write, image, Firestore, Drive, Lovable, or publish routes exist.

## Client-owned deployment

Use project `stoked-proxy-502319-c4` (number `1032949592191`) in the
Arts of August account. The existing Firestore `(default)` database in this
project is unaffected. Set:

| Variable | Value |
| --- | --- |
| `AOA_FIREBASE_PROJECT_ID` | `stoked-proxy-502319-c4` |
| `AOA_STUDIO_ORIGIN` | `https://arts-of-august-artwork-studio.dohertyashlee.chatgpt.site` |
| `AOA_ALLOWED_EMAILS` | `ashlee@asqashlee.xyz` for the first test |
| `AOA_GITHUB_TOKEN` | Secret Manager binding to a repo-scoped read-only GitHub credential |

Later add Kaleigh's confirmed Google email to the allowlist. Do not infer it.
The Cloud Run service identity needs access to that one Secret Manager secret.
The bridge does not inherit GitHub access from Codex. It needs no Firestore or
Drive permissions for this slice.

The browser sends `Authorization: Bearer <Firebase ID token>` over HTTPS.
Firebase Admin verifies signature, expiry, and client project. The service
also checks project audience/issuer, verified email, Google provider, and the
explicit email allowlist. It allows browser cross-origin requests only from
the exact Studio origin, with `GET` and `Authorization`. Origin checks are
an additional browser boundary, never a substitute for token verification.
Tokens and GitHub credentials must not be logged or returned in responses.

Cloud Run's ingress endpoint must be reachable from the Site's browser. For
this Firebase-token architecture, **do not enable IAP**: it would require a
second browser authentication flow. If the Cloud Run service allows unauthenticated
invocation at the platform layer, every data endpoint still verifies a Firebase
ID token and allowlist before returning data. `/healthz` is public but has no
artwork data. Prefer a dedicated bridge service with request logging configured
to avoid sensitive authorization headers. Restrict who can deploy or change
configuration with client-owned IAM.

Deploy this directory as source with its standard `Dockerfile`; the container
starts the WSGI entrypoint `bridge_service:application`. Before deployment, review
billing, region, service account, and the read-only GitHub credential. Store
the GitHub credential directly in Secret Manager, never in the Site or repo.
No Cloud Run resources or secrets have been created by this code change.

## Verification sequence

1. Run `python -m unittest -v test_bridge_identity.py test_github_artwork_source.py test_bridge_service.py`.
2. Deploy and confirm unauthenticated `/v1/session` returns 401,
   disallowed Google accounts return 403, and Ashlee's signed-in session returns
   200. A spoofed email header must not grant access.
3. Supply the read-only GitHub secret and check Eastern Trail Marsh returns
   `existing` from the governed index. A GitHub outage must yield an error,
   never `clear`.
4. Only after this proof, connect a small read-only Site action. Do not add
   artwork writes or publishing until their separate review and approval gates
   have been designed and verified.

Firebase reference: https://firebase.google.com/docs/auth/admin/verify-id-tokens
