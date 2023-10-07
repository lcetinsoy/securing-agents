from abc import abstractmethod
from securingagents.LLMCompleter import LLMCompleter


class Skill:
    
    def __init__(self, llm_completer: LLMCompleter):
        self.llm_completer = LLMCompleter
        
    @abstractmethod
    def apply(self): pass
 

class ImprovePlanner():
    name="improve_planner"
    description="improve the planning and skill choosing of the agent. Usefull if the agent is stuck"
    def __init__(self, llm_completer: LLMCompleter):
        
        self.llm_completer = llm_completer
        
    def apply(self, planner):

        current_prompt = planner.get_prompt()
        
        improver_prompt = f"""
        The following text is a planification prompt for an AI agent. 
        Suggest and improved prompt (be creative)
        
        {current_prompt}

        """
        new_prompt = self.llm_completer.complete(improver_prompt, 1000)
        planner.set_prompt(new_prompt)



class WriteFile(Skill):
    name="write_to_file"
    description="can be used to write text or code"
    def apply(self, goal: str):
        
        
        with open(path, 'w') as f:
            f.write(content)
            
            
class ReadLogFile(Skill): pass


class ReadFile(Skill):
    name="read_file"
    description="can be used to read a file to get its content"
    
    
    def __init__(self, llm_completer: LLMCompleter):
        self.llm_completer = llm_completer
    def apply(self, goal: str):
        
        prompt = """
        You have the goal {goal} and you must read the file to reach the goal
        the filepath is:
        """
        
        path = self.llm_completer.complete(prompt, 200)
        
        with open(path, 'r') as f:
            content = f.read()
        return content