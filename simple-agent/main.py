from agents import Runner, set_tracing_disabled
from my_agent.teacher_agent import gemini_agent

set_tracing_disabled(True)


res = Runner.run_sync(
    starting_agent=gemini_agent,
    input="2+2=?")

print(res.final_output)