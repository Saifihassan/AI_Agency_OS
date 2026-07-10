
from schemas.schemas import NewsSearcherOutput, NewsVerifierOutput, NewsAnalystOutput
from tavily import TavilyClient
from agents import function_tool,Agent
import os
import json
import requests
from duckduckgo_search import DDGS
from clients import groq,zenmux,sambanova,bluesmind
from prompts.prompts import NEWS_SEARCHER_INSTRUCTIONS, NEWS_ANALYST, NEWS_VERIFIER_INSTRUCTIONS
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

@function_tool
def duckduckgo_search(query: str) -> str:
    """
    Search the web using DuckDuckGo for up-to-date information.
    """
    results = DDGS().text(query, max_results=5)
    return str(results)

@function_tool
def serper_search(query: str) -> str:
    """
    Search the web using Google Search (via Serper API) for up-to-date information.
    """
    url = "https://google.serper.dev/search"
    payload = json.dumps({
      "q": query,
      "num": 5
    })
    headers = {
      'X-API-KEY': os.getenv("SERPER_API_KEY", ""),
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return str(response.json())



news_searcher = Agent(
    name="news_searcher",
    instructions=NEWS_SEARCHER_INSTRUCTIONS,
    model=bluesmind,
    tools=[tavily_search, duckduckgo_search, serper_search],
    output_type=NewsSearcherOutput
)
news_verifier = Agent(
    name="news_verifier",
    instructions=NEWS_VERIFIER_INSTRUCTIONS,
    model=bluesmind,
    tools=[duckduckgo_search],
    output_type=NewsVerifierOutput
)

news_analyst=Agent(
    name="news_analyst",
    instructions=NEWS_ANALYST,
    model=sambanova,
    output_type=NewsAnalystOutput
)

tools = [news_searcher.as_tool(tool_name="news_searcher",tool_description="searches the internet and provides latest market news"),news_verifier.as_tool(tool_name="news_verifier",tool_description="verifies the news and returns the results in a concise and informative manner"),news_analyst.as_tool(tool_name="news_analyst",tool_description="provides actionable intelligence for marketing agencies" )]

