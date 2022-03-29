import os
import requests
from fastapi import APIRouter
from app.services.text import get_sentiment_predictions
from app.models.text import TextRequest

router = APIRouter()


@router.get("/text/sentiment/example", tags=["text"])
async def get_text_example():
    inputs = [
        "I loved it so much I could cry tears of joy",
        "It was okay.",
        "It was the worst movie I have ever seen. Huge waste of time",
    ]
    return {"inputs": inputs, "results": get_sentiment_predictions(inputs)}


@router.post("/text/sentiment/predict", tags=["text"])
async def get_text_prediction(req: TextRequest):
    return {"inputs": req.texts, "results": get_sentiment_predictions(req.texts)}
