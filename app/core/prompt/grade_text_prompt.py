from langchain.prompts import PromptTemplate


grade_text_prompt = PromptTemplate(
    template="""
        당신은 문장 채점 전문가입니다.
        주어진 배열 {answers}을 {correct_answer}와 비교하여 각 배열 요소의 유사도 점수를 채점해주세요.
        점수는 0점부터 100점까지 입니다.
    """ ,
    input_variables=[
        "answers",
        "correct_answer"
    ],
)
