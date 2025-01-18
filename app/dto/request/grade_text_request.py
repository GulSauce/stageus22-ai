from pydantic import BaseModel
from typing import List


class GradeTextRequest(BaseModel):
    answers: List[str]
    correct_answer: str
