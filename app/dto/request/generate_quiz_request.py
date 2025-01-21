from pydantic import BaseModel


class GenerateQuizRequest(BaseModel):
    title: str
    content: str
    subject: str
    count: int
