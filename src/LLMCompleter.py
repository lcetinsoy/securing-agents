import abc

class LLMCompleter:
    
    @abc.abstractmethod
    def complete(self, prompt:str, max_token:int, temperature:float) -> str: pass