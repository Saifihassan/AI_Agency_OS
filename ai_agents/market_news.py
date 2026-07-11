import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from ai_agents.schemas.schemas import MarketIntelligenceReport
from dotenv import load_dotenv
from httpx import __name
from agents import Agent, Runner, trace, enable_verbose_stdout_logging
import asyncio
from ai_agents.agent_tools.tools import tools
from ai_agents.clients import groq,zenmux,nara
from ai_agents.prompts.prompts import MARKET_INTELLIGENCE_AGENT

load_dotenv(override=True)
market_intelligence_agent = Agent(
    name="market_news_agent",
    instructions=MARKET_INTELLIGENCE_AGENT,
    model=nara,
    tools=tools,
    output_type=MarketIntelligenceReport
)



async def main():
    enable_verbose_stdout_logging()
    with trace("market_news_workflow"):
        result =await Runner.run(market_intelligence_agent,"most recent news of tech,marketing,startup,AI and how can it help marketing ")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        result.final_output.time_stamp = current_time
        print(result.final_output)


if __name__=="__main__":

    asyncio.run(main())