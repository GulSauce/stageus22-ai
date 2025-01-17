from langchain_community.tools import DuckDuckGoSearchRun

def search_with_subject(subject):
    search = DuckDuckGoSearchRun()
    searched_result = search.invoke(subject + " 나무위키")
    print(searched_result)
    return searched_result