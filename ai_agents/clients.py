from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
import os

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

zenmux = OpenAIChatCompletionsModel(model="z-ai/glm-4.7-flash-free", openai_client=zenmux_client)
groq = OpenAIChatCompletionsModel(model="gpt-oss-120b", openai_client=groq_client) 
# groq2 = OpenAIChatCompletionsModel(model="llama-3.3-70b-versatile", openai_client=groq_client) 

# SambaNova client
sambanova_client = AsyncOpenAI(
    base_url="https://api.sambanova.ai/v1",
    api_key=os.getenv("SAMBANOVA_API_KEY")
)

sambanova = OpenAIChatCompletionsModel(model="gpt-oss-120b", openai_client=sambanova_client)

# Nara Router client
nara_client = AsyncOpenAI(
    base_url="https://router.bynara.id/v1",
    api_key=os.getenv("NARAROUTER_API_KEY")
)

nara = OpenAIChatCompletionsModel(model="mistral-large", openai_client=nara_client)

# Blues Mind client
bluesmind_client = AsyncOpenAI(
    base_url=os.getenv("BLUESMIND_BASE_URL"),
    api_key=os.getenv("BLUESMIND_API_KEY")
)

bluesmind = OpenAIChatCompletionsModel(model="gpt-4o", openai_client=bluesmind_client)
