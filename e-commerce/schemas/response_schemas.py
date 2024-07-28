from pydantic import BaseModel


class Response_Message(BaseModel):
    message: str