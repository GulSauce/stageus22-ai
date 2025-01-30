from pydantic import BaseModel, Field
from typing import Optional
from typing import List
from app.dto.model.quizType import QuizType


class Quiz(BaseModel):
    title: str = Field(description="The title of the quiz")
    description: str = Field(description="The content of the quiz")
    choices: Optional[List[str]] = Field(description="The choices of the quiz if QuizType is TEXT it should be null")
    type: QuizType = Field(description="The type of the quiz")
    singleChoiceCorrectAnswer: Optional[int] = Field(description="The correct answer of the quiz if QuizType is TEXT it should be null")
    textCorrectAnswer: Optional[str] = Field(description="The correct answer of the quiz if QuizType is SINGLE_CHOICE it should be null")
    reason: str = Field(description="The reason of the correct answer")