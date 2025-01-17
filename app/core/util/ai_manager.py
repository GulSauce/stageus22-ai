from app.core.config.ai_model import chat_model
from langchain.schema import HumanMessage


class AIManager:
    @staticmethod
    def chat(prompt, parser=None):
        human_messages = [HumanMessage(content=prompt)]
        if parser:
            if parser:
                human_messages = [
                    HumanMessage(content=parser.get_format_instructions())
                ] + human_messages

        response = chat_model.invoke(human_messages)
        return response.content