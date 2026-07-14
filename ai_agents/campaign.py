import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ai_agents.agent_tools.tools import searxng_search,firecrawl_scrape

from agents import Agent, Runner, trace, enable_verbose_stdout_logging
from ai_agents.clients import bluesmind
from ai_agents.prompts.prompts import CAMPAIGN_PLANNER_INSTRUCTIONS, CONTENT_GENERATOR_INSTRUCTIONS
from ai_agents.schemas.schemas import CampaignPlan, CampaignAssets
import asyncio

enable_verbose_stdout_logging()

campaign_planner = Agent(
    name="campaign_planner",
    instructions=CAMPAIGN_PLANNER_INSTRUCTIONS,
    model=bluesmind,
    output_type=CampaignPlan,
    tools=[searxng_search,firecrawl_scrape]
)

content_generator=Agent(
    name = "content_generator",
    instructions=CONTENT_GENERATOR_INSTRUCTIONS,
    model=bluesmind,
    output_type=CampaignAssets
    
)

async def run_campaign_agent(website: str, campaign_goal: str, target_platforms: list):
    with trace("execution"):
        platforms_str = ", ".join(target_platforms)
        prompt = f"Website/Business: {website}\nGoal: {campaign_goal}\nPlatforms: {platforms_str}"
        result = await Runner.run(campaign_planner, prompt)
        print("=========campaign plan========")
        print(result)
        print("=========content generator output=============")
        content=await Runner.run(content_generator,result.final_output.model_dump_json())
        print(content.final_output)
        print("========================================")
        return content.final_output

