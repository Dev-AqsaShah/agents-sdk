from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner

key = config("GEMINI_API_KEY")
base_url = config("BASE_URL")

gemini_client = AsyncOpenAI(api_key=key, base_url=base_url)

MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",openai_client=gemini_client)

agent = Agent(
    name="aqsa",
    instructions="you are a helpful assistant. give me ans in detail",
    model=MODEL
)

res = Runner.run_sync(starting_agent=agent,input="2+2=?")

print(res.final_output)