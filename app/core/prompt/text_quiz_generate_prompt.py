from langchain.prompts import PromptTemplate

text_quiz_generation_prompt = PromptTemplate(
    template="""
        당신은 퀴즈 생성 전문가입니다.g
        주관식 퀴즈를 생성하세요
        {subject}에 대한 퀴즈를 생성해주세요.
        개수는 {count} 개 생성하세요
        아래의 참고자료와 당신이 알고 있는 정보를 활용하여 퀴즈를 생성해주세요.
        # 참고자료
        {title}
        {description}
        {reference}
    """,
    input_variables=[
        "title",
        "subject",
        "description",
        "count",
        "reference"
    ],
)

