from app.core.prompt.grade_text_prompt import grade_text_prompt
from app.core.util.ai_manager import AIManager
from langchain.output_parsers import PydanticOutputParser
from app.core.util.function_execution_time_measurer import FunctionExecutionTimeMeasurer
from app.dto.request.grade_text_request import GradeTextRequest
from app.dto.response.grade_text_response import GradeTextResponse


class GradeService:
    def __init__(self):
        self.quiz_generation_prompt = grade_text_prompt
        self.ai_manager = AIManager()

    def grade_text(self, request: GradeTextRequest):

        parser = PydanticOutputParser(pydantic_object=GradeTextResponse)

        generated_quiz_has_parsing_format = (
            FunctionExecutionTimeMeasurer.run_function(
                "주관식 채점 태스크",
                self.ai_manager.chat,
                self.quiz_generation_prompt.format(
                        answers=request.submitAnswers,
                        correct_answer=request.correctAnswer,
                    ),
                parser
            )
        )

        result = parser.parse(generated_quiz_has_parsing_format)

        return result