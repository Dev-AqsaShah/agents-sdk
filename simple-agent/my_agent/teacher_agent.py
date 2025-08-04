from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
# from my_data_type.my_data_type_schema import MyData
from my_tool.math_tool import plus, multiply, subtract


gemini_agent = Agent(
    name="aqsa",
    instructions="you are a helpful assistant. give me ans in detail",
    model=GEMINI_MODEL,
    # output_type=MyData
    tools=[plus, multiply, subtract]
)


print(gemini_agent.name)
print(gemini_agent.tools)