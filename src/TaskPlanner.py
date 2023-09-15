from typing import List
from Skills import Skill

class TaskPlanner:
    
    def get_next_task(
            self,
            general_goal: str,
            skills: List[Skill]
            
    ) -> Skill:
        
        return skills[0]
    