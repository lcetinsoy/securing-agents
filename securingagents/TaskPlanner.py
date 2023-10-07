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
            previous_action_data
            
    ) -> Skill:
        
        previous_action = previous_action_data['action']
        previous_action_feedback = previous_action_data['feedback']
        skill_list = [
            f'{skill.name} ({i}):{skill.description}'
            for i, skill 
            in enumerate(skills)
        ]
        skill_prompt = "\n - ".join(skill_list)
        n_skill = len(skill_list) - 1
        self.prompt = f"""
Role: You are the strongest engineer in the world. You know how to 
decompose problems in sub problems and choose skills to use to solve it. 
Goal: Choose the next skill to apply to reach a tasked goal. You will 
be given a list of skills and a goal and you pick a single number.
You must not choose always the same skill, be creative

Here are a few example of good skill number choice for examples. Do not generate the examples
-- Example 1  

Goal: create a data visualization for the data.csv file
available skills:
    read_file (0): reading data.csv to know what to plot
    write_code (1): write python code with a data_visualization tool
    execute_code (2): launch code so that work well
    
Previous action: None

Reasonning: 
I need to write a code to plot data of a file.
Thus I need to read the file.
There fore I should first pick the read_file skill (0)
The picked skill number is: 0
-- End of example

-- Example 2  
Goal : create a data visualization for the data.csv files

available skills:
 - read_file (0): reading data.csv to know what to plot
 - write_code (1): write python code with a data_visualization tool
 - execute_code (2): launch code so that work well

The previous action was: read_file (0) and was a success.

reasoning: 
The file data file have been read so now
I can write the code to plot the columns I want. 
Therefore the action should write_code (1)
the picked skill number is: 1 

-- End of example    

You have the following goal: {general_goal}
You have the following skills: 
 - {skill_prompt}

Previous action was: {previous_action} and was {previous_action_feedback}

Generate next skill id to use (between 0 and {n_skill}). It should be a single number
The picked skill number is:
"""
        
        plan = self.llm_completer.complete(self.prompt, 1000, 0.5)
        
        task_picker_prompt = f"""
You have the following goal: {general_goal}
The devised plan is: {plan}
Pick the next step number. The output should be a number.
the next step number:"""
        i_skill = self.llm_completer.complete(task_picker_prompt, 10, 0.5)
        i_skill = i_skill.strip()[0]
        return skills[int(i_skill)]
    