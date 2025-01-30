from pydantic import BaseModel, Field
from typing import List

from app.dto.model.quiz import  Quiz

class QuizGenerateResponse(BaseModel):
    quizzes: List[Quiz] = Field(description="list of the quiz")