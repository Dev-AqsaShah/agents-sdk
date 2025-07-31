from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_data_type.my_data_type_schema import MyData

gemini_agent = Agent(
    name="aqsa",
    instructions="you are a helpful assistant. give me ans in detail",
    model=GEMINI_MODEL,
    output_type=MyData
)
