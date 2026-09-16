import io
import json
import unittest

from bridge_service import create_app


CONFIG = {
    "AOA_IAP_AUDIENCE": "/projects/123/locations/us-east1/services/aoa-bridge",
    "AOA_ALLOWED_EMAILS": "kaleigh@example.com",
    "AOA_GITHUB_TOKEN": "server-only-test-token",
}


def call(app, path="/v1/artworks/identity", query="title=Eastern+Trail+Marsh",
         assertion="signed-test-assertion", method="GET"):
    info = {}
    environ = {
        "PATH_INFO": path, "QUERY_STRING": query, "REQUEST_METHOD": method,
        "wsgi.input": io.BytesIO(),
    }
    if assertion:
        environ["HTTP_X_GOOG_IAP_JWT_ASSERTION"] = assertion
    body = b"".join(app(environ, lambda status, headers: info.update(
        status=status, headers=dict(headers),
    )))
    return info["status"], json.loads(body), info["headers"]


class BridgeServiceTests(unittest.TestCase):
    def setUp(self):
        self.calls = []

        def checker(token, **identity):
            self.calls.append((token, identity))
            return {"state": "existing", "source_sha": "reviewed-revision",
                    "matches": [{"artwork_id": "AOA-ART-0065"}]}

        self.app = create_app(
            config=CONFIG, verifier=lambda jwt, aud: {
                "sub": "test-user", "email": "kaleigh@example.com"
            }, checker=checker,
        )

    def test_existing_artwork_is_read_only(self):
        status, body, headers = call(self.app)
        self.assertEqual(status, "200 OK")
        self.assertEqual(body["state"], "existing")
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertEqual(self.calls, [(
            "server-only-test-token", {"title": "Eastern Trail Marsh"},
        )])

    def test_no_assertion_is_denied(self):
        self.assertEqual(call(self.app, assertion="")[0], "401 Unauthorized")
        self.assertFalse(self.calls)

    def test_unlisted_identity_is_denied(self):
        app = create_app(config=CONFIG, verifier=lambda jwt, aud: {
            "sub": "other", "email": "other@example.com"
        }, checker=lambda *a, **kw: self.fail("Should not read index"))
        self.assertEqual(call(app)[0], "403 Forbidden")

    def test_missing_configuration_fails_closed(self):
        app = create_app(config={}, verifier=lambda *a: self.fail("No auth"))
        self.assertEqual(call(app)[0], "503 Service Unavailable")

    def test_no_mutation_route(self):
        self.assertEqual(call(self.app, method="POST")[0], "405 Method Not Allowed")
        self.assertEqual(call(self.app, path="/v1/artworks/publish")[0],
                         "404 Not Found")

    def test_repeated_or_unknown_query_is_rejected(self):
        self.assertEqual(call(self.app, query="title=A&title=B")[0], "400 Bad Request")
        self.assertEqual(call(self.app, query="secret=x")[0], "400 Bad Request")
        self.assertFalse(self.calls)


if __name__ == "__main__":
    unittest.main()
