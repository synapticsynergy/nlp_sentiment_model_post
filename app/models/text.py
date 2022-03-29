from pydantic import BaseModel


class TextRequest(BaseModel):
    texts: list
