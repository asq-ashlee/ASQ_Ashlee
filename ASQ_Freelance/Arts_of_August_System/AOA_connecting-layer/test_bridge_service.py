import io
import json
import unittest

from bridge_service import create_app


ORIGIN = "https://arts-of-august-artwork-studio.dohertyashlee.chatgpt.site"
PROJECT = "stoked-proxy-502319-c4"
CONFIG = {
    "AOA_FIREBASE_PROJECT_ID": PROJECT,
    "AOA_ALLOWED_EMAILS": "ashlee@asqashlee.xyz",
    "AOA_STUDIO_ORIGIN": ORIGIN,
    "AOA_GITHUB_TOKEN": "server-only-test-token",
}


def claims(**changes):
    result = {
        "aud": PROJECT,
        "iss": f"https://securetoken.google.com/{PROJECT}",
        "sub": "test-user",
        "email": "ashlee@asqashlee.xyz",
        "email_verified": True,
        "firebase": {"sign_in_provider": "google.com"},
    }
    result.update(changes)
    return result


def call(app, path="/v1/artworks/identity", query="title=Eastern+Trail+Marsh",
         token="signed-test-token", method="GET", origin=ORIGIN, headers=None):
    info = {}
    environ = {
        "PATH_INFO": path, "QUERY_STRING": query, "REQUEST_METHOD": method,
        "wsgi.input": io.BytesIO(),
    }
    if token:
        environ["HTTP_AUTHORIZATION"] = "Bearer " + token
    if origin:
        environ["HTTP_ORIGIN"] = origin
    environ.update(headers or {})
    body = b"".join(app(environ, lambda status, response_headers: info.update(
        status=status, headers=dict(response_headers),
    )))
    return info["status"], json.loads(body) if body else None, info["headers"]


class BridgeServiceTests(unittest.TestCase):
    def setUp(self):
        self.calls = []

        def checker(token, **identity):
            self.calls.append((token, identity))
            return {"state": "existing", "source_sha": "reviewed-revision",
                    "matches": [{"artwork_id": "AOA-ART-0065"}]}

        self.app = create_app(
            config=CONFIG, verifier=lambda jwt, project: claims(), checker=checker,
        )

    def test_existing_artwork_is_read_only(self):
        status, body, headers = call(self.app)
        self.assertEqual(status, "200 OK")
        self.assertEqual(body["state"], "existing")
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertEqual(headers["Access-Control-Allow-Origin"], ORIGIN)
        self.assertEqual(self.calls, [(
            "server-only-test-token", {"title": "Eastern Trail Marsh"},
        )])

    def test_session_requires_identity_but_not_github_secret(self):
        config = {key: value for key, value in CONFIG.items() if key != "AOA_GITHUB_TOKEN"}
        app = create_app(config=config, verifier=lambda *a: claims())
        status, body, _ = call(app, path="/v1/session")
        self.assertEqual(status, "200 OK")
        self.assertEqual(body["email"], "ashlee@asqashlee.xyz")
        self.assertEqual(call(app, token="", path="/v1/session")[0], "401 Unauthorized")

    def test_missing_invalid_and_unapproved_identity_denied(self):
        self.assertEqual(call(self.app, token="")[0], "401 Unauthorized")
        for modified in (
            {"aud": "other-project"}, {"iss": "other-issuer"},
            {"email_verified": False}, {"email": "other@example.com"},
            {"firebase": {"sign_in_provider": "password"}}, {"sub": ""},
        ):
            app = create_app(config=CONFIG, verifier=lambda *a, m=modified: claims(**m))
            self.assertEqual(call(app)[0], "403 Forbidden")
        app = create_app(config=CONFIG, verifier=lambda *a: (_ for _ in ()).throw(ValueError()))
        self.assertEqual(call(app)[0], "401 Unauthorized")
        self.assertFalse(self.calls)

    def test_origin_and_preflight(self):
        self.assertEqual(call(self.app, origin="https://evil.example")[0], "403 Forbidden")
        status, _, headers = call(
            self.app, method="OPTIONS", token="",
            headers={"HTTP_ACCESS_CONTROL_REQUEST_METHOD": "GET"},
        )
        self.assertEqual(status, "204 No Content")
        self.assertEqual(headers["Access-Control-Allow-Headers"], "Authorization")
        self.assertNotIn("Access-Control-Allow-Credentials", headers)
        self.assertFalse(self.calls)

    def test_missing_configuration_fails_closed(self):
        app = create_app(config={}, verifier=lambda *a: self.fail("No auth"))
        self.assertEqual(call(app, origin="")[0], "503 Service Unavailable")

    def test_no_mutation_route_and_invalid_query(self):
        self.assertEqual(call(self.app, method="POST")[0], "405 Method Not Allowed")
        self.assertEqual(call(self.app, path="/v1/artworks/publish")[0], "404 Not Found")
        self.assertEqual(call(self.app, query="title=A&title=B")[0], "400 Bad Request")
        self.assertEqual(call(self.app, query="secret=x")[0], "400 Bad Request")
        self.assertFalse(self.calls)


if __name__ == "__main__":
    unittest.main()
