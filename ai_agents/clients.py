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

bluesmind = OpenAIChatCompletionsModel(model="gpt-5-mini", openai_client=bluesmind_client)

# Gemini client
gemini_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY")
)

gemini = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=gemini_client)

# IAMHC client
iamhc_client = AsyncOpenAI(
    # base_url=os.getenv("IAMHC_BASE_URL"),
    base_url="https://api.iamhc.cn/v1",
    api_key=os.getenv("IAMHC_API_KEY")
)

iamhc = OpenAIChatCompletionsModel(model="Qwen3-Coder-Next-FP8", openai_client=iamhc_client)

# General Compute client
generalcompute_client = AsyncOpenAI(
    base_url=os.getenv("GENERALCOMPUTE_BASE_URL"),
    api_key=os.getenv("GENERALCOMPUTE_API_KEY")
)

generalcompute = OpenAIChatCompletionsModel(model="minimax-m2.7", openai_client=generalcompute_client)

# Literouter client
literouter_client = AsyncOpenAI(
    base_url=os.getenv("LITEROUTER_BASE_URL"),
    api_key=os.getenv("LITEROUTER_API_KEY")
)

literouter = OpenAIChatCompletionsModel(model="glm-5.1-cheap:free", openai_client=literouter_client)
