from pydantic import BaseModel

class GenerateSingleChoiceQuizRequest(BaseModel):
    title: str
    description: str
    subject: str
    quizCount: int
