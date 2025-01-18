from pydantic import BaseModel, Field
from typing import List

from app.dto.model.quiz import  Quiz

class GradeTextResponse(BaseModel):
    score: List[int] = Field(description="Scores of the answers")