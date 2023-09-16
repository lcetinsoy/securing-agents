from securingagents.Agent import Agent
from securingagents.TaskPlanner import TaskPlanner
from securingagents.Skills import Skill
from typing import List
from securingagents.LLMCompleter import LLMCompleter

class PlannerFake(TaskPlanner):
    
    def get_next_task(self, general_goal:str, skills: List[Skill]):
        
        return Skill("run skill", "allows to run code")


def test_plan_action():
    
    planner = PlannerFake(LLMCompleter())
    agent = Agent(planner)
    agent.add_skill(Skill("derp", "do nothing"))
    
    agent.do("build a simple python script which prints hello!", 4)
    