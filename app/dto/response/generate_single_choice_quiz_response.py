from pydantic import BaseModel, Field
from typing import List
from app.dto.model.single_choice_quiz import SingleChoiceQuiz


class GenerateSingleChoiceQuizResponse(BaseModel):
    quizzes: List[SingleChoiceQuiz] = Field(description="list of the quiz")