from pydantic import BaseModel

class GenerateTextQuizRequest(BaseModel):
    title: str
    description: str
    subject: str
    quizCount: int
