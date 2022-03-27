from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_success():
    resp = client.get("/users")
    assert resp.json() == [{"username": "Rick"}, {"username": "Morty"}]
