from agents import Agent,Runner
import asyncio
from clients import zenmux,bluesmind


sys_msg = """"""

agent = Agent(
    name="test_agent",
    instructions="you write code for user's request ",
    model=bluesmind,
)

async def main():
    result = await Runner.run(agent, "create a calculator in one line in python")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
