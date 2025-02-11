from pydantic import BaseModel, Field
from typing import List

class SingleChoiceQuiz(BaseModel):
    title: str = Field(description="The title of the quiz")
    description: str = Field(description="Provide a detailed explanation of what the quiz is asking, ensuring that no hints or answer details are disclosed")
    choices: List[str] = Field(description="The choices of the quiz")
    correctChoice: int = Field(description="The correct choice index of the quiz")
    reason: str = Field(description="The reason of the correct answer")