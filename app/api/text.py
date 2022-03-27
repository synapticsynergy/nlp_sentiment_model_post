import os
import requests
from fastapi import APIRouter
from app.services.text import get_text_embeddings

router = APIRouter()


@router.get("/text/", tags=["text"])
async def read_text():
    inputs = ["so stupid, anger, rage", "it was ok I guess", "happy happy joy joy"]
    return {"inputs": inputs, "results": get_text_embeddings(inputs)}
