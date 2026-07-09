from dotenv import load_dotenv
from httpx import __name
from agents import Agent,OpenAIChatCompletionsModel,Runner
from openai import AsyncOpenAI
import os
import asyncio

load_dotenv(override=True)
client = AsyncOpenAI(
    base_url=os.getenv("GENERALCOMPUTE_BASE_URL"),
    api_key=os.getenv("GENERALCOMPUTE_API_KEY")
)

# apikey = os.getenv("GENERALCOMPUTE_API_KEY")
# print(apikey)

model = OpenAIChatCompletionsModel(model="minimax-m2.7",openai_client=client)

agent = Agent(
    name="coder",
    instructions="write the program that the user asks",
    model=model
)

async def main():
    result =await Runner.run(agent,"write a program to calulate the sum of two numbers")
    print(result.final_output)


if __name__=="__main__":

    asyncio.run(main())