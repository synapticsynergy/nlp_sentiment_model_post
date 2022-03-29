import os
import requests

MODEL_BASE_URL = os.environ.get("MODEL_BASE_URL", "localhost:8501")


def get_sentiment_predictions(texts: list):
    data = {"inputs": texts}
    resp = requests.post(f"http://{MODEL_BASE_URL}/v1/models/sentiment_model:predict", json=data)
    resp.raise_for_status()
    predictions = resp.json()["outputs"]
    return predictions
