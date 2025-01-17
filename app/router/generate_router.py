from app.dto.request.generate_quiz_request import GenerateQuizRequest
from fastapi import APIRouter, Depends
from app.service.generate_service import GenerateService

router = APIRouter()


def get_generate_service():
    return GenerateService()

@router.post("/generate/quiz")
def generate_quiz(
    generateQuizRequest: GenerateQuizRequest,
    generateService=Depends(get_generate_service),
):
    return generateService.generate_quiz(generateQuizRequest)