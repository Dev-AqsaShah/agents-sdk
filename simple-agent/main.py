from agents import Runner
from my_agent.teacher_agent import agent



res = Runner.run_sync(starting_agent=agent,input="2+2=?")

print(res.final_output)