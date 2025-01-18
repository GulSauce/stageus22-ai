from pydantic import BaseModel, Field
from typing import List

from app.dto.model.quiz import  Quiz

class GradeTextResponse(BaseModel):
    scores: List[int] = Field(description="Scores of the answers")