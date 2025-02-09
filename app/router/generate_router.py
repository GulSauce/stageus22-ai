from fastapi import APIRouter, Depends

from app.dto.request.generate_single_choice_quiz_request import GenerateSingleChoiceQuizRequest
from app.dto.request.generate_text_quiz_request import GenerateTextQuizRequest
from app.service.generate_service import GenerateService

router = APIRouter()


def get_generate_service():
    return GenerateService()
@router.post("/generate/quiz/text")
def generate_quiz(
    generateSingleChoiceQuizRequest: GenerateSingleChoiceQuizRequest,
    generateService=Depends(get_generate_service),
):
    return generateService.generate_text_quiz(generateSingleChoiceQuizRequest)

@router.post("/generate/quiz/single-choice")
def generate_quiz(
    generateTextQuizRequest: GenerateTextQuizRequest,
    generateService=Depends(get_generate_service),
):
    return generateService.generate_single_choice_quiz(generateTextQuizRequest)