from pydantic import BaseModel, Field
from typing import List
from app.dto.model.text_quiz import TextQuiz


class GenerateTextQuizResponse(BaseModel):
    quizzes: List[TextQuiz] = Field(description="list of the quiz")