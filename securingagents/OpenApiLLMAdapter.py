import openai
import os
from dotenv import load_dotenv


from securingagents.LLMCompleter import LLMCompleter
from securingagents.PromptLogging import log_completion

class OpenApiLLMAdapter(LLMCompleter):
    
    def __init__(self):
        load_dotenv()
        self.key = os.getenv('OPEN_API_KEY')
        openai.api_key = self.key
        self.model ="davinci-002"
        
    @log_completion
    def complete(self, prompt: str, max_token: int, temperature: float) -> str:
        
        completion = openai.Completion.create(
            model=self.model,
            temperature=temperature,
            prompt=prompt
        )
        
        return completion.choices[0].text