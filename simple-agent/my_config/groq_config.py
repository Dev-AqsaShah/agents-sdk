from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel

key = config("GROQ_API_KEY")
base_url = config("BASE_URL_GROQ")

gemini_client = AsyncOpenAI(api_key=key, base_url=base_url)

MODEL = OpenAIChatCompletionsModel(
    model="llama-3.3-70b-versatile",openai_client=gemini_client)
