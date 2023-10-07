from securingagents.Skills import Skill 
from securingagents.TaskPlanner import TaskPlanner
from typing_extensions  import Self

class Agent:
    
    @classmethod
    def build_default(cls) -> Self:
        from securingagents.OpenApiLLMAdapter import OpenApiLLMAdapter
        agent = cls(TaskPlanner(OpenApiLLMAdapter()))
        return agent

    def __init__(self, planner:TaskPlanner):# injection de dépendance
        #avantage 1 : c'est l'utilisateur de la classe qui décide de l'implémentation de TaskPlanner
        #avantage 2 : pour les tests unitaires on peut créer notre fausse implémentation
        self.planner = planner
        self.skills = []
    
    def add_skill(self, skill_class:Skill):
        
        skill = skill_class(self.planner.llm_completer)
        self.skills.append(skill)
    
    def do(self, general_goal: str, max_iter=None):
        
        feedback = {
            "action": "None",
            "feedback": "None"
        }
        n_action = 0
        while n_action <= max_iter:
                        
            skill = self.planner.get_next_task(general_goal, self.skills, feedback)
            print(f"doing: {skill.name}")
            if skill.name == "finish":
                break
            
            feedback = skill.apply(general_goal)
            n_action += 1
            