from securingagents.Agent import Agent
from securingagents.Skills import *


task = "create a python file saying hello and save it in hello.py"
#task = input('Give me a task:')

agent = Agent.build_default()
agent.add_skill(ReadFile)
agent.add_skill(WriteFile)
agent.do(task, max_iter=10)