from agents import Agent
from my_config.gemini_config import MODEL


agent = Agent(
    name="aqsa",
    instructions="you are a helpful assistant. give me ans in detail",
    model=MODEL
)
