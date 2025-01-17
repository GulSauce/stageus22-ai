from langchain.prompts import PromptTemplate


quiz_generation_prompt = PromptTemplate(
    template="""
        당신은 퀴즈 생성 전문가입니다. {prompt}에 대한 퀴즈를 생성해주세요.
        개수는 {count} 개 생성하세요
        주관식과 객관식을 모두 생성해주세요.
        아래의 참고자료와 당신이 알고 있는 정보를 활용하여 퀴즈를 생성해주세요.
        {reference}
    """ ,
    input_variables=[
        "prompt",
        "count",
        "reference"
    ],
)
