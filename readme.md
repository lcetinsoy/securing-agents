# Securing agents

LLM based agent for mapping and auditing complex environments

Deploy realiable agents securing your production IT system.
You environnments change all the time, ensure that your production 
system stay secured or get informed immediatly. 

Specify the permissions of the securing agents in a fine grained manner
so that you are sure the agents does not interfer. 

Why not an agent for a CI/CD pipeline ? 
Because it is the prod env which matters

## Quick start

### installation

```bash
make install 

#or 

pip install -r requirements.txt


cp .env.template .env

#add you api key (openai for now)
```

### usage 

```bash
python main.py 
```
Notice error line, fork, fix and make a PR :D 

## todo 

- a skill neeed a call to LLM to choose the parameters. 

- Si trop d'erreur de prompt, faire un improve planner automatique (idem si nombre pas généré par exemple) 

- get feedback from a run skill
- plug feedback in the planner
- handle skill error

### notes
- port to go / rust to have static binary agent for deployment easing

## Licence

Not licensed yet (only published for now)
Might be either BSL, GPL or MIT depending on the project direction