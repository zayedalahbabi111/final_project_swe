from fastapi.testclient import TestClient
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "poc"))
from backend import app
client = TestClient(app)

def test_create_university_post():
    r = client.post("/posts", json={"content":"Hello UniBoard","audience_type":"UNIVERSITY","community_id":None})
    assert r.status_code == 201
    assert r.json()["content"] == "Hello UniBoard"

def test_community_post_requires_community():
    r = client.post("/posts", json={"content":"Club update","audience_type":"COMMUNITY","community_id":None})
    assert r.status_code == 400

def test_invalid_audience_rejected():
    r = client.post("/posts", json={"content":"Bad","audience_type":"INVALID","community_id":None})
    assert r.status_code == 400