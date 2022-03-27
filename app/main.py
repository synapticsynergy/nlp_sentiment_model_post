from typing import Optional

from fastapi import FastAPI
from app.api import user, text

app = FastAPI()

app.include_router(user.router)
app.include_router(text.router)


@app.get("/")
async def root():
    return {"Hello": "World"}
