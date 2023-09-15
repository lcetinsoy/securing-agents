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
        
        
        