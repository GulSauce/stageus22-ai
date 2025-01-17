from pydantic import BaseModel


class GenerateQuizRequest(BaseModel):
    subject: str
    count: int
