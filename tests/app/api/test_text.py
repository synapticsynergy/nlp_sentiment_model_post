import json
from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest import mock
from app.main import app
from app.models.text import TextRequest


client = TestClient(app)


def test_get_example():
    with mock.patch("requests.post") as mock_requests:
        mock_requests.return_value.json.return_value = {"outputs": [0.999997854, 0.435923845, 0.00120159087]}
        resp = client.get("/text/sentiment/example")
        assert resp.json() == {
            "inputs": [
                "I loved it so much I could cry tears of joy",
                "It was roughly what I expected",
                "It was the worst movie I have ever seen. Huge waste of time",
            ],
            "results": [0.999997854, 0.435923845, 0.00120159087],
        }


def test_predict_sentiment():
    with mock.patch("requests.post") as mock_requests:
        mock_requests.return_value.json.return_value = {"outputs": [0.723295271]}
        resp = client.post(
            "/text/sentiment/predict",
            json=TextRequest(
                texts=["I'm feeling sentimental, please tell me approximately how sentimental"]
            ).dict(),
        )
        assert resp.json() == {
            "inputs": [
                "I'm feeling sentimental, please tell me approximately how sentimental",
            ],
            "results": [0.723295271],
        }
