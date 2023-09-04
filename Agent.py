class Skill:
    
    def __init__(self, name: str, description: str):
        self.name = name,
        self.description = description
                
class RunCodeSkill(Skill):
    
    def execute(self): pass
        #pas besoin de openai
    
class GenerateCodeSkill(Skill):
    
    def execute(self): pass
    
        #open AI caché
        
        
        

class TaskPlanner:
    
    def get_next_skill(
            self,
            skills: list[Skill],
            general_goal: str,
            generated_code: str,
            feedback: str
    ) -> Skill:
        #open ai caché 
        return skills[0]
    
    
class Agent:

    
    def __init__(self, planner:TaskPlanner):# injection de dépendance
        #avantage 1 : c'est l'utilisateur de la classe qui décide de l'implémentation de TaskPlanner
        #avantat2 : pour les tests unitaires on peut créer notre fausse implémentation
        self.planner = planner
        self.skills = []
    
    def add_skill(self, skill:Skill):
        pass
    
    def execute(self, general_goal: str, max_iter=None):
        
        feedback = ""
        while True:
                        
            skill = self.planner.get_next_skill(general_goal, feedback, etc. etc.)
            if skill.name =="finish":
                break
        
            feedback = skill.execute()
            
            