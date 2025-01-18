from fastapi import APIRouter, Depends

from app.dto.request.grade_text_request import GradeTextRequest
from app.service.grade_service import GradeService

router = APIRouter()


def get_grade_service():
    return GradeService()

@router.post("/grade/text")
def generate_quiz(
    gradeTextRequest: GradeTextRequest,
    gradeService=Depends(get_grade_service),
):
    return gradeService.grade_text(gradeTextRequest)