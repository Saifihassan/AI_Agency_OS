from tavily import TavilyClient
from agents import function_tool,Agent
import os
import json
import requests
from duckduckgo_search import DDGS
from ai_agents.clients import groq,zenmux,sambanova,bluesmind,gemini,nara,generalcompute,iamhc
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

@function_tool
def searxng_search(query: str) -> str:
    """
    Search the web using SearXNG for up-to-date information.
    """
    url = os.getenv("SEARXNG_URL", "http://localhost:8080/search")
    params = {
        "q": query,
        "format": "json"
    }
    response = requests.get(url, params=params)
    return str(response.json())

@function_tool
def firecrawl_scrape(url: str) -> str:
    """
    Scrape the content of a provided URL using Firecrawl.
    """
    api_key = os.getenv("FIRECRAWL_API_KEY") or os.getenv("FIRECRAW_API_KEY")
    endpoint = "https://api.firecrawl.dev/v1/scrape"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "url": url,
        "formats": ["markdown"]
    }
    response = requests.post(endpoint, headers=headers, json=payload)
    return str(response.json())


