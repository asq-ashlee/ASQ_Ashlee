"""Private, read-only WSGI entry point for the AOA Cloud Run bridge.

Deployment must enable Cloud Run IAP and restrict its access policy. This
service also verifies the signed IAP assertion and a configured email allowlist.
No endpoint in this service can create, update, or publish artwork.
"""

import json
import os
from urllib.parse import parse_qs

from github_artwork_source import ArtworkSourceUnavailable, check_current_identity

IAP_CERTS_URL = "https://www.gstatic.com/iap/verify/public_key"
IAP_ISSUER = "https://cloud.google.com/iap"


def verify_iap_assertion(assertion, audience):
    from google.auth.transport import requests
    from google.oauth2 import id_token

    claims = id_token.verify_token(
        assertion, requests.Request(), audience=audience,
        certs_url=IAP_CERTS_URL,
    )
    if claims.get("iss") != IAP_ISSUER or not claims.get("sub"):
        raise ValueError("Invalid IAP identity")
    return claims


def _respond(start_response, status, body):
    payload = json.dumps(body, separators=(",", ":")).encode("utf-8")
    start_response(status, [
        ("Content-Type", "application/json; charset=utf-8"),
        ("Content-Length", str(len(payload))),
        ("Cache-Control", "no-store"),
        ("X-Content-Type-Options", "nosniff"),
    ])
    return [payload]


def create_app(*, config=None, verifier=None, checker=None):
    config = os.environ if config is None else config
    verifier = verify_iap_assertion if verifier is None else verifier
    checker = check_current_identity if checker is None else checker

    def application(environ, start_response):
        if environ.get("PATH_INFO") == "/healthz":
            return _respond(start_response, "200 OK", {"status": "ok"})
        if environ.get("PATH_INFO") != "/v1/artworks/identity":
            return _respond(start_response, "404 Not Found", {"error": "not_found"})
        if environ.get("REQUEST_METHOD") != "GET":
            return _respond(start_response, "405 Method Not Allowed",
                            {"error": "method_not_allowed"})

        audience = config.get("AOA_IAP_AUDIENCE", "").strip()
        allowed = {email.strip().casefold() for email in
                   config.get("AOA_ALLOWED_EMAILS", "").split(",") if email.strip()}
        token = config.get("AOA_GITHUB_TOKEN", "").strip()
        if not audience or not allowed or not token:
            return _respond(start_response, "503 Service Unavailable",
                            {"error": "service_unavailable"})
        assertion = environ.get("HTTP_X_GOOG_IAP_JWT_ASSERTION", "")
        if not assertion:
            return _respond(start_response, "401 Unauthorized",
                            {"error": "authentication_required"})
        try:
            identity = verifier(assertion, audience)
        except Exception:
            return _respond(start_response, "401 Unauthorized",
                            {"error": "authentication_required"})
        if identity.get("email", "").casefold() not in allowed:
            return _respond(start_response, "403 Forbidden", {"error": "not_allowed"})

        query = environ.get("QUERY_STRING", "")
        if len(query) > 2048:
            return _respond(start_response, "400 Bad Request", {"error": "invalid_query"})
        params = parse_qs(query, keep_blank_values=False)
        if set(params) - {"artwork_id", "title", "slug"} or any(
            len(values) != 1 or len(values[0]) > 200 for values in params.values()
        ) or not params:
            return _respond(start_response, "400 Bad Request", {"error": "invalid_query"})
        try:
            result = checker(token, **{name: values[0] for name, values in params.items()})
        except (ArtworkSourceUnavailable, ValueError):
            return _respond(start_response, "503 Service Unavailable",
                            {"error": "artwork_index_unavailable"})
        return _respond(start_response, "200 OK", result)

    return application


application = create_app()
