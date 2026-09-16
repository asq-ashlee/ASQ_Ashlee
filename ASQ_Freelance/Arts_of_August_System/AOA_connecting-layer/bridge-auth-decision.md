# Artwork Studio authentication decision

Status: Google provider enabled in the client project; browser integration remains unimplemented and untested.
Date: 2026-09-16

## Goal

Kaleigh opens Artwork Studio, signs in with Google once, and works through
artwork review without seeing GitHub, Cloud Run, token handling, or separate
admin screens. The existing Arts of August project owns authentication and
backend resources. Artwork Studio remains a thin interface and never holds
GitHub, Drive, or Firestore service credentials.

## Recommended browser path

Use Google sign-in through Firebase Authentication or Identity Platform in
the client's Google Cloud/Firebase project. The Sites browser app obtains the
signed end-user ID token and sends it over HTTPS to the Cloud Run bridge.
The bridge verifies the token against the exact client project, checks the
approved artist/operator identity, and executes only the requested action.
The bridge's service identity and Secret Manager hold backend access.

Firebase Authentication manages user identity, not a new artwork catalog or
artwork source of truth. Firestore remains the existing live artwork database;
the governed CSV and Drive assets retain their existing roles.

For a browser-hosted Site on a different domain, configure only that Site's
exact origin for sign-in/redirect and API CORS. Never use wildcard CORS with
credentials. The service may be reachable over HTTPS, but every data and
mutation route must reject requests lacking a verified, permitted user token.
The response must not expose privileged backend credentials.

## Existing IAP prototype

The current draft `bridge_service.py` verifies signed Cloud Run IAP
assertions. It is useful as a private server-side read-only test, but
cross-origin IAP login from the Sites domain has not been validated.
Do not deploy it as the final artist-facing integration or wire the Site to
it on an assumption that browser sign-in will work.

A simpler same-origin IAP design could instead host the artist UI behind IAP,
but that would change the chosen Sites deployment boundary. Keep the Sites UI
where it is for this first integration and validate Google sign-in tokens.

## Before implementing the change

1. Completed: Firebase Authentication was initialized in
   `stoked-proxy-502319-c4`; Google sign-in is enabled. Public-facing name is
   `Arts of August` and Ashlee's monitored address is the support email.
   Next, inspect existing web app registrations before creating any new one.
2. Confirm Kaleigh's Google account for the future artist allowlist. Ashlee
   (`ashlee@asqashlee.xyz`) is the first tester.
3. Make a narrow sign-in and read-only identity proof using Eastern Trail Marsh.
   Deny an unapproved account and verify the signed token server-side.
4. Only after that proof, add the first governed write action. Preserve the
   separate Approve Master, Approve Artwork, and Publish approvals.

Google reference: https://docs.cloud.google.com/run/docs/authenticating/end-users
Google reference: https://firebase.google.com/docs/auth/admin/verify-id-tokens
