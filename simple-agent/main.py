from agents import Runner, set_tracing_disabled, enable_verbose_stdout_logging
from my_agent.teacher_agent import gemini_agent

set_tracing_disabled(True)
enable_verbose_stdout_logging()


res = Runner.run_sync(
    starting_agent=gemini_agent,
    input="mujhe user ke name ki list do. ")

print(res.final_output)