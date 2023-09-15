from Agent import Agent
from TaskPlanner import TaskPlanner
from Skills import RunCodeSkill


class PlannerFake(TaskPlanner):
    
    def get_next_task(self, general_goal:str):
        
        return RunCodeSkill("run skill", "allows to run code")


def test_plan_action():
    
    planner = PlannerFake()
    agent = Agent(planner)
    
    agent.do("build a simple python script which prints hello!", 4)
    