from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_success():
    resp = client.get("/")
    assert resp.json() == {"Hello": "World"}
