from schemas.schemas import MarketIntelligenceReport
from dotenv import load_dotenv
from httpx import __name
from agents import Agent, Runner, trace, enable_verbose_stdout_logging
import asyncio
from agent_tools.tools import tools
from clients import groq,zenmux,nara
from prompts.prompts import MARKET_INTELLIGENCE_AGENT

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
        print(result.final_output)


if __name__=="__main__":

    asyncio.run(main())