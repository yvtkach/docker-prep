import hello


class FakeDB:
    def __init__(self, *args, **kwargs):
        pass

    def populate_db(self):
        pass

    def query_titles(self):
        return ["Blog post #1", "Blog post #2"]


def test_health_returns_ok():
    client = hello.server.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_home_lists_posts(monkeypatch):
    monkeypatch.setattr(hello, "DBManager", FakeDB)
    monkeypatch.setattr(hello, "conn", None)
    client = hello.server.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Blog post #1" in response.data
