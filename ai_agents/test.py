from agents import Agent,Runner
import asyncio
from clients import zenmux,bluesmind,gemini,iamhc


sys_msg = """"""

agent = Agent(
    name="test_agent",
    instructions="you write code for user's request ",
    model=iamhc,
)

async def main():
    result = await Runner.run(agent, "create a library management system with all the necessary functionalities in python and output the entire python code without any strings attached to it so that i can copy it")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
