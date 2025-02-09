from pydantic import BaseModel, Field
from typing import Optional

class TextQuiz(BaseModel):
    title: str = Field(description="The title of the quiz")
    description: str = Field(description="The content of the quiz")
    correctAnswer: Optional[str] = Field(description="The correct answer of the quiz if QuizType is SINGLE_CHOICE it should be null")
    reason: str = Field(description="The reason of the correct answer")