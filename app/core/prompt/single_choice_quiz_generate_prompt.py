from langchain.prompts import PromptTemplate


single_choice_quiz_generation_prompt = PromptTemplate(
    template="""
        당신은 퀴즈 생성 전문가입니다. 퀴즈를 생성해주세요
        
        ## 퀴즈 종류
        단일 선택 객관식 퀴즈
        
        ## 주제
        {subject}
        
        ## 개수
        {count}개
        
        ## 참고 자료
        {title}
        {description}
        {reference}
        
        ## 응답 언어
        한국어
    """ ,
    input_variables=[
        "title",
        "subject",
        "description",
        "count",
        "reference"
    ],
)
