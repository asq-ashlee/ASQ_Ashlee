"""Read-only AOA bridge using verified Firebase end-user identity."""

import json
import os
from urllib.parse import parse_qs

from github_artwork_source import ArtworkSourceUnavailable, check_current_identity


def verify_firebase_identity(token, project_id):
    import firebase_admin
    from firebase_admin import auth

    try:
        app = firebase_admin.get_app()
    except ValueError:
        app = firebase_admin.initialize_app(options={"projectId": project_id})
    return auth.verify_id_token(token, app=app)


def _respond(start_response, status, body, origin=None):
    payload = json.dumps(body, separators=(",", ":")).encode("utf-8")
    headers = [
        ("Content-Type", "application/json; charset=utf-8"),
        ("Content-Length", str(len(payload))),
        ("Cache-Control", "no-store"),
        ("X-Content-Type-Options", "nosniff"),
        ("Vary", "Origin"),
    ]
    if origin:
        headers.append(("Access-Control-Allow-Origin", origin))
    start_response(status, headers)
    return [payload]


def create_app(*, config=None, verifier=None, checker=None):
    config = os.environ if config is None else config
    verifier = verify_firebase_identity if verifier is None else verifier
    checker = check_current_identity if checker is None else checker

    def application(environ, start_response):
        path = environ.get("PATH_INFO")
        if path == "/healthz":
            return _respond(start_response, "200 OK", {"status": "ok"})
        if path not in ("/v1/session", "/v1/artworks/identity"):
            return _respond(start_response, "404 Not Found", {"error": "not_found"})

        allowed_origin = config.get("AOA_STUDIO_ORIGIN", "").rstrip("/")
        request_origin = environ.get("HTTP_ORIGIN", "")
        origin = allowed_origin if allowed_origin and request_origin == allowed_origin else None
        if request_origin and not origin:
            return _respond(start_response, "403 Forbidden", {"error": "origin_not_allowed"})
        if environ.get("REQUEST_METHOD") == "OPTIONS":
            if not origin or environ.get("HTTP_ACCESS_CONTROL_REQUEST_METHOD") != "GET":
                return _respond(start_response, "403 Forbidden", {"error": "origin_not_allowed"})
            start_response("204 No Content", [
                ("Access-Control-Allow-Origin", origin),
                ("Access-Control-Allow-Methods", "GET"),
                ("Access-Control-Allow-Headers", "Authorization"),
                ("Access-Control-Max-Age", "600"),
                ("Vary", "Origin"),
                ("Cache-Control", "no-store"),
            ])
            return [b""]
        if environ.get("REQUEST_METHOD") != "GET":
            return _respond(start_response, "405 Method Not Allowed",
                            {"error": "method_not_allowed"}, origin)

        project_id = config.get("AOA_FIREBASE_PROJECT_ID", "").strip()
        allowed = {email.strip().casefold() for email in
                   config.get("AOA_ALLOWED_EMAILS", "").split(",") if email.strip()}
        if not project_id or not allowed or not allowed_origin:
            return _respond(start_response, "503 Service Unavailable",
                            {"error": "service_unavailable"}, origin)
        authorization = environ.get("HTTP_AUTHORIZATION", "")
        kind, separator, token = authorization.partition(" ")
        if kind.lower() != "bearer" or not separator or not token.strip() or len(token) > 8192:
            return _respond(start_response, "401 Unauthorized",
                            {"error": "authentication_required"}, origin)
        try:
            identity = verifier(token.strip(), project_id)
        except Exception:
            return _respond(start_response, "401 Unauthorized",
                            {"error": "authentication_required"}, origin)
        email = identity.get("email", "").casefold()
        if (identity.get("aud") != project_id or
                identity.get("iss") != f"https://securetoken.google.com/{project_id}" or
                not identity.get("sub") or
                identity.get("email_verified") is not True or
                identity.get("firebase", {}).get("sign_in_provider") != "google.com" or
                email not in allowed):
            return _respond(start_response, "403 Forbidden", {"error": "not_allowed"}, origin)
        if path == "/v1/session":
            return _respond(start_response, "200 OK", {"status": "ready", "email": email}, origin)

        secret = config.get("AOA_GITHUB_TOKEN", "").strip()
        if not secret:
            return _respond(start_response, "503 Service Unavailable",
                            {"error": "service_unavailable"}, origin)
        query = environ.get("QUERY_STRING", "")
        if len(query) > 2048:
            return _respond(start_response, "400 Bad Request", {"error": "invalid_query"}, origin)
        params = parse_qs(query, keep_blank_values=False)
        if set(params) - {"artwork_id", "title", "slug"} or any(
            len(values) != 1 or len(values[0]) > 200 for values in params.values()
        ) or not params:
            return _respond(start_response, "400 Bad Request", {"error": "invalid_query"}, origin)
        try:
            result = checker(secret, **{name: values[0] for name, values in params.items()})
        except (ArtworkSourceUnavailable, ValueError):
            return _respond(start_response, "503 Service Unavailable",
                            {"error": "artwork_index_unavailable"}, origin)
        return _respond(start_response, "200 OK", result, origin)

    return application


application = create_app()
