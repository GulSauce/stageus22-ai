from pydantic import BaseModel
from typing import List

class GradeTextRequest(BaseModel):
    submitAnswers: List[str]
    correctAnswer: str
