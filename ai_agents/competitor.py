import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from agents import Agent, Runner, trace, enable_verbose_stdout_logging
from ai_agents.agent_tools.tools import (
    searxng_search,
    firecrawl_scrape,
)
from ai_agents.clients import bluesmind, gemini, generalcompute

from ai_agents.schemas.schemas import CompetitiveAnalysis
from ai_agents.prompts.prompts import COMPETITOR_ANALYZER_INSTRUCTIONS

competitor_analyzer=Agent(
    name="competitor_analyzer",
    instructions=COMPETITOR_ANALYZER_INSTRUCTIONS,
    model=generalcompute,
    output_type=CompetitiveAnalysis,
    tools=[searxng_search,firecrawl_scrape]
)

async def run_competitor_agent(target_website: str):
    with trace("Competitor analysis"):
        result = await Runner.run(competitor_analyzer, target_website)
        print(result.final_output)
    return result.final_output


