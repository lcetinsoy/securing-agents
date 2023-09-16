from typing import List
from securingagents.Skills import Skill
from securingagents.LLMCompleter import LLMCompleter

class TaskPlanner:
    
    def __init__(self, llm_completer:LLMCompleter):
        
        self.llm_completer = llm_completer
    
    def get_next_task(
            self,
            general_goal: str,
            skills: List[Skill],
            feedback
            
    ) -> Skill:
        
        skill_list = [f'{i} {skill.name}:{skill.description}' for skill,i in enumerate(skills)]
        
        prompt = f"""
            You are the best manager in the world with abilities to 
            plan and decompose tasks. You have been tasked a goal
            and you must decompose into a set of tasks related to 
            a list of available skills
            
            Example of a goal and the tasked
            
            Goal : create a data visualization for the data.csv files
            skills : read_file, write_file, execute_code
            tasks:
                - read_file: reading data.csv to know what to plot
                - write_code: write python code with a data_visualization tool
                - execute_code 
                
            reasoning: I need to know how is structured the csv file to load it
            and plot its data. I might write wrong code sometimes and I need to
            iterate several times between the tasks.  
            
            End of example    
        
            You have the following goal: {general_goal}
            You have the follwoing skills: {skill_list}
            
            {feedback}
            
            return the next step to do as a number.
            The skill number is:
        """
        
        i_skill = self.llm_completer.complete(prompt, 1000, 0.5)
        
        return skills[int(i_skill)]
    