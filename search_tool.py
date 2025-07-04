from langchain.utilities import TavilySearchAPIWrapper

def search(query):
    search_api = TavilySearchAPIWrapper()
    return search_api.run(query)