from pydantic import BaseModel, Field
from typing import Optional
from typing import List
from app.dto.model.quizType import QuizType


class Quiz(BaseModel):
    title: str = Field(description="The title of the quiz")
    content: str = Field(description="The content of the quiz")
    choices: Optional[List[str]] = Field(description="The choices of the quiz if QuizType is TEXT it should be null")
    type: QuizType = Field(description="The type of the quiz")
    singleChoiceAnswer: Optional[int] = Field(description="The answer of the quiz if QuizType is TEXT it should be null")
    textAnswer: Optional[str] = Field(description="The answer of the quiz if QuizType is SINGLE_CHOICE it should be null")
    reason: Optional[str] = Field(description="The reason of the quiz")