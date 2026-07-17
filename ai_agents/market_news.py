
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from ai_agents.schemas.schemas import NewsResearch, MarketIntelligenceReport
from dotenv import load_dotenv
from agents import Agent, Runner, trace, enable_verbose_stdout_logging
from ai_agents.agent_tools.tools import tavily_search, duckduckgo_search, searxng_search,serper_search
from ai_agents.clients import groq,zenmux,nara,gemini,generalcompute,bluesmind
from ai_agents.prompts.prompts import NEWS_RESEARCHER_INSTRUCTIONS, MARKET_ANALYST_INSTRUCTIONS

load_dotenv(override=True)
news_researcher = Agent(
    name="news_research",
    instructions=NEWS_RESEARCHER_INSTRUCTIONS,
    model=bluesmind,
    tools=[searxng_search, duckduckgo_search, serper_search],
    output_type=NewsResearch
)

market_analyst = Agent(
    name="market_analyst",
    instructions=MARKET_ANALYST_INSTRUCTIONS,
    model=generalcompute    ,
    output_type=MarketIntelligenceReport
)


async def run_marketing_news_agent():
    enable_verbose_stdout_logging()
    with trace("market_news_workflow"):
        research_result = await Runner.run(news_researcher,"most recent news of tech,marketing,startup,AI and how can it help marketing ")
        print("--- RESEARCH DONE ---")
        
        analysis_result = await Runner.run(market_analyst, str(research_result.final_output))
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        analysis_result.final_output.generated_at = current_time
        print(analysis_result.final_output)
        return analysis_result.final_output

