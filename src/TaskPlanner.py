from typing import List
from Skills import Skill
from LLMCompleter import LLMCompleter

class TaskPlanner:
    
    def __init__(self, llm_completer:LLMCompleter):
        
        self.llm_completer = llm_completer
    
    def get_next_task(
            self,
            general_goal: str,
            skills: List[Skill]
            
    ) -> Skill:
        
        skill_list = [f'{i} {skill.name}:{skill.description}' for skill,i in enumerate(skills)]
        
        prompt = f"""
            You have the following goal: {general_goal}
            You have the follwoing skills: {skill_list}
            
            return the next step to do as a number.
            The skill number is:
        """
        
        i_skill = self.llm_completer.complete(prompt, 1000, 0.5)
        
        return skills[int(i_skill)]
    