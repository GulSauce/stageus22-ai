from langchain.prompts import PromptTemplate


quiz_generation_prompt = PromptTemplate(
    template="""
        당신은 퀴즈 생성 전문가입니다. {subject}에 대한 퀴즈를 생성해주세요.
        
        ## 개수
        개수는 {count} 개 생성하세요
        
        ## 문제 구성
        주관식과 객관식을 모두 생성해주세요. 객관식 4: 주관식 1 비율로 생성해주세요.
        
        ## 명령
        아래의 참고자료와 당신이 알고 있는 정보를 활용하여 퀴즈를 생성해주세요.
        {reference}
        제목:{title}, 내용: {content}와 어울리는 퀴즈를 생성해주세요.
    """ ,
    input_variables=[
        "subject",
        "count",
        "reference",
        "title",
        "content"
    ],
)
