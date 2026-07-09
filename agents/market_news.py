from dotenv import load_dotenv
from httpx import __name
from agents import Agent,OpenAIChatCompletionsModel,Runner
from openai import AsyncOpenAI
import os
import asyncio
from agent_tools.tools import tavily_search
load_dotenv(override=True)


# Zenmux client
zenmux_client = AsyncOpenAI(
    base_url=os.getenv("ZENMUX_BASE_URL"),
    api_key=os.getenv("ZENMUX_API_KEY")
)

# Groq client
groq_client = AsyncOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

zenmux = OpenAIChatCompletionsModel(model="stepfun/step-3.7-flash-free",openai_client=zenmux_client)
groq = OpenAIChatCompletionsModel(model="openai/gpt-oss-120b",openai_client=groq_client)
agent = Agent(
    name="market_news_agent",
    instructions="You're task is to provide the latest market news based on the user query and by latest i mean the current month and the current year",
    model=groq,
    tools=[tavily_search]
)

async def main():
    result =await Runner.run(agent,"top 10 headlines in tech industries")
    print(result.final_output)


if __name__=="__main__":

    asyncio.run(main())