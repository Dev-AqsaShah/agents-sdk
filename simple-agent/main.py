from agents import Runner, set_tracing_disabled, enable_verbose_student_logging
from my_agent.teacher_agent import gemini_agent

set_tracing_disabled(True)
enable_verbose_student_logging()


res = Runner.run_sync(
    starting_agent=gemini_agent,
    input="2+2=? and is me multiply karo 100")

print(res.final_output)