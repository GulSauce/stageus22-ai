from app.core.prompt.quiz_generation_prompt import quiz_generation_prompt
from app.core.util.ai_manager import AIManager
from app.dto.request.generate_quiz_request import GenerateQuizRequest
from langchain.output_parsers import PydanticOutputParser
from app.core.util.function_execution_time_measurer import FunctionExecutionTimeMeasurer
from app.dto.response.quiz_generate_response import QuizGenerateResponse
from app.core.util.serach_engine import search_with_subject


class GenerateService:
    def __init__(self):
        self.quiz_generation_prompt = quiz_generation_prompt
        self.ai_manager = AIManager()

    def generate_quiz(self, request: GenerateQuizRequest):

        searched_result = search_with_subject(request.subject)
        parser = PydanticOutputParser(pydantic_object=QuizGenerateResponse)

        generated_quiz_has_parsing_format = (
            FunctionExecutionTimeMeasurer.run_function(
                "퀴즈 생성 태스크",
                self.ai_manager.chat,
                self.quiz_generation_prompt.format(
                        prompt=request.subject,
                        count=request.count,
                        reference=searched_result
                    ),
                parser
            )
        )

        result = parser.parse(generated_quiz_has_parsing_format)

        return result