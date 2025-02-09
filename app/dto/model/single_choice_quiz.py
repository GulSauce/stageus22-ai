from pydantic import BaseModel, Field
from typing import List

class SingleChoiceQuiz(BaseModel):
    title: str = Field(description="The title of the quiz")
    description: str = Field(description="The content of the quiz")
    choices: List[str] = Field(description="The choices of the quiz")
    correctChoice: int = Field(description="The correct choice index of the quiz")
    reason: str = Field(description="The reason of the correct answer")