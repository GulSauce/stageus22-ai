from app.core.prompt.single_choice_quiz_generate_prompt import single_choice_quiz_generation_prompt
from app.core.prompt.text_quiz_generate_prompt import text_quiz_generation_prompt
from app.core.util.ai_manager import AIManager
from app.dto.request.generate_single_choice_quiz_request import GenerateSingleChoiceQuizRequest
from langchain.output_parsers import PydanticOutputParser
from app.core.util.function_execution_time_measurer import FunctionExecutionTimeMeasurer
from app.dto.request.generate_text_quiz_request import GenerateTextQuizRequest
from app.core.util.serach_engine import search_with_subject
from app.dto.response.generate_single_choice_quiz_response import GenerateSingleChoiceQuizResponse
from app.dto.response.generate_text_quiz_response import GenerateTextQuizResponse


class GenerateService:
    def __init__(self):
        self.single_choice_quiz_generation_prompt = single_choice_quiz_generation_prompt
        self.text_quiz_generation_prompt = text_quiz_generation_prompt
        self.ai_manager = AIManager()

    def generate_single_choice_quiz(self, request: GenerateSingleChoiceQuizRequest):
        searched_result = search_with_subject(request.subject)
        parser = PydanticOutputParser(pydantic_object=GenerateSingleChoiceQuizResponse)

        generated_quiz_has_parsing_format = (
            FunctionExecutionTimeMeasurer.run_function(
                "객관식 퀴즈 생성 태스크",
                self.ai_manager.chat,
                self.single_choice_quiz_generation_prompt.format(
                    title=request.title,
                    description=request.description,
                    subject=request.subject,
                    count=request.quizCount,
                    reference=searched_result
                ),
                parser
            )
        )

        result = parser.parse(generated_quiz_has_parsing_format)

        return result

    def generate_text_quiz(self, request: GenerateTextQuizRequest):
        searched_result = search_with_subject(request.subject)
        parser = PydanticOutputParser(pydantic_object=GenerateTextQuizResponse)

        generated_quiz_has_parsing_format = (
            FunctionExecutionTimeMeasurer.run_function(
                "주관식 퀴즈 생성 태스크",
                self.ai_manager.chat,
                self.text_quiz_generation_prompt.format(
                        title=request.title,
                        description=request.description,
                        subject=request.subject,
                        count=request.quizCount,
                        reference=searched_result
                    ),
                parser
            )
        )

        result = parser.parse(generated_quiz_has_parsing_format)

        return result