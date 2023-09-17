from securingagents.Agent import Agent

task = "create a python file saying hello"
#task = input('Give me a task:')
agent = Agent.build_default()
agent.do(task, max_iter=10)