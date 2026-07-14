from agents import Agent,Runner
import asyncio
from clients import zenmux,bluesmind,gemini,iamhc


sys_msg = """"""

agent = Agent(
    name="test_agent",
    instructions="you write code for user's request ",
    model=iamhc
)

async def main():
    result = await Runner.run(agent, "create a hospital management system with all the necessary functionalities")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
