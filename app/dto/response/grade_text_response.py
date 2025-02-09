from pydantic import BaseModel, Field
from typing import List

class GradeTextResponse(BaseModel):
    scores: List[int] = Field(description="Scores of the answers")