from tavily import TavilyClient
from agents import function_tool
import os

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@function_tool
def tavily_search(query: str) -> str:
    """
    Search the web for up-to-date information.
    """
    response = tavily.search(
        query=query,
        search_depth="advanced",
        max_results=5,
    )

    return str(response["results"])