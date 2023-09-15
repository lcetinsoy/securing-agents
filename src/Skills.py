class Skill:
    
    def __init__(self, name: str, description: str):
        self.name = name,
        self.description = description
 

class WriteFile(Skill):
    
    def apply(self, path, content):
        
        with open(path, 'w') as f:
            f.write(content)
            
class ReadFile(Skill):
    
    def apply(self, path):
        
        with open(path, 'r') as f:
            content = f.read()
        return content