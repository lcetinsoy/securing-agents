from Skills import Skill 
from TaskPlanner import TaskPlanner

class Agent:

    def __init__(self, planner:TaskPlanner):# injection de dépendance
        #avantage 1 : c'est l'utilisateur de la classe qui décide de l'implémentation de TaskPlanner
        #avantat2 : pour les tests unitaires on peut créer notre fausse implémentation
        self.planner = planner
        self.skills = []
    
    def add_skill(self, skill:Skill):
        pass
    
    def do(self, general_goal: str, max_iter=None):
        
        feedback = ""
        n_action = 0
        while n_action <= max_iter:
                        
            skill = self.planner.get_next_task(general_goal)
            
            if skill.name == "finish":
                break
            
            feedback = skill.execute()
            n_action += 1
            