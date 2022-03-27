import os
import requests

MODEL_BASE_URL = os.environ.get("MODEL_BASE_URL", "localhost:8501")


def get_text_embeddings(texts: list):
    data = {"inputs": texts}
    resp = requests.post(f"http://{MODEL_BASE_URL}/v1/models/sentiment_model:predict", json=data).json()
    embeddings = resp["outputs"]
    return embeddings
