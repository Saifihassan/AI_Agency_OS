import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import Agent, Runner, trace, enable_verbose_stdout_logging
from ai_agents.agent_tools.tools import (
    searxng_search,
    firecrawl_scrape,
)
from ai_agents.clients import bluesmind, gemini, generalcompute
from ai_agents.schemas.schemas import ProspectAnalysis, OutreachSequence
from ai_agents.prompts.prompts import PROSPECT_ANALYZER_INSTRUCTIONS, OUTREACH_GENERATOR_INSTRUCTIONS
import asyncio


prospect_analyzer=Agent(
    name="prospect_analyzer",
    instructions=PROSPECT_ANALYZER_INSTRUCTIONS,
    model=generalcompute,
    output_type=ProspectAnalysis,
    tools=[searxng_search,firecrawl_scrape]
    
)

outreach_generator =Agent(
    name="outreach_generator",
    instructions=OUTREACH_GENERATOR_INSTRUCTIONS,
    model=bluesmind,
    output_type=OutreachSequence
    
)


async def run_outreach_agent(website: str, service: str, outreachtone: str):
    with trace("Outreach Sequence"):
        prompt = f"Website: {website}\nService Offered: {service}\nOutreach Tone: {outreachtone}"
        res = await Runner.run(prospect_analyzer, prompt)
        print("========ANALYZER OUTPUT========")
        print(res.final_output)
        print("===============================")
        outreach_seq = await Runner.run(outreach_generator, res.final_output.model_dump_json())
        print("========OUTREACH OUTPUT========")
        print(outreach_seq.final_output)
        print("===============================")
    return {
        "prospect_analysis": res.final_output,
        "outreach_sequence": outreach_seq.final_output
    }

