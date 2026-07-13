from agents.run_internal import agent_bindings
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from agents import Agent,Runner,trace,enable_verbose_stdout_logging
from ai_agents.prompts.prompts import RESEARCH_ANALYST,STRATEGY_ADVISOR
from ai_agents.clients import bluesmind,iamhc,generalcompute,gemini
from ai_agents.schemas.schemas import ResearchAnalysis,StrategyReport
from ai_agents.agent_tools.tools import searxng_search,firecrawl_scrape
import asyncio

enable_verbose_stdout_logging()

research_analyst=Agent(
    name="research_analyst",
    instructions=RESEARCH_ANALYST,
    output_type=ResearchAnalysis,
    model=generalcompute,
    tools=[searxng_search]
)

strategy_advisor=Agent(
    name="strategy advisor",
    instructions=STRATEGY_ADVISOR,
    output_type=StrategyReport,
    model=generalcompute,    
    tools=[firecrawl_scrape]

)

async def run_flow(input:str,website_url:str):
    with trace("execution"):
        query = input
        if website_url:
            query += f"\nCompany URL: {website_url}"
        results = await Runner.run(research_analyst, query)
        print("=====research analysis output======")
        print(results.final_output)
        print("=======strategy advisor output=======")
        report=await Runner.run(strategy_advisor,   results.final_output.model_dump_json())
        print(report.final_output)
        print("===================================")

        return {
            "research": results.final_output,
            "strategy": report.final_output
        }


