from agents import Agent,Runner
import asyncio
import os
from clients import zenmux,bluesmind,gemini,iamhc,literouter

sys_msg = """"""

agent = Agent(
    name="test_agent",
    instructions="you're a helpfull assistant",
    model=gemini
)

async def main():
    result = await Runner.run(agent, "hello")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
