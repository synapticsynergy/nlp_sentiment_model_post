from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest import mock
from app.main import app

client = TestClient(app)


def test_get_example():
    with mock.patch("requests.post") as mock_requests:
        mock_requests.return_value.json.return_value = {"outputs": [1, 0.5, 0.0001]}
        resp = client.get("/text/sentiment/example")
        assert resp.json() == {
            "inputs": [
                "I loved it so much I could cry tears of joy",
                "It was okay.",
                "It was the worst movie I have ever seen. Huge waste of time",
            ],
            "results": [1, 0.5, 0.0001],
        }
