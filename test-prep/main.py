#  what is LLM 
# tools nhi hote
# data pr train hua ha
# personal info nhi h is k passs
# bhulaker 
# generate answers 
# prediction

from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant."
)

result = Runner.run_sync(
    starting_agent=agent,
    input="What is the capital of Pakistan?"
)

print(result.final_output)
