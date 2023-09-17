from functools import wraps
import logging

decorator_logger = logging.getLogger('prompt_logger')
handler = logging.FileHandler('prompt.logs')  # Log dans le fichier 'decorator.log'
decorator_logger.addHandler(handler)
decorator_logger.setLevel(logging.DEBUG)  # Niveau DEBUG

def log_completion(func):
    
    @wraps(func)
    def wrapper(self, prompt, max_token, temperature, *args, **kwargs):
        result = func(self, prompt, max_token, temperature, *args, **kwargs)
        
        decorator_logger.debug(f"Prompt: {prompt}\n, Completion: {result}")
        return result
    return wrapper
