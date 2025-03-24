import ollama
import json

from utils.system_prompt import sys_prompt

chat_history = []
chat_history.append({"role": "system", "content": 'Instructions : ' + f'{sys_prompt}'})
def llm(content):

    chat_history.append({"role": "user", "content": f'{content}'})

    response = ollama.chat(
        model="mistral", 
        messages=chat_history,
        options= {
            "temperature": 0.5
            }
        )

    try:
        json_response = json.loads(response['message']['content'])
        return json.dumps(json_response, indent=2)
    except json.JSONDecodeError:
        return "Error: Response is not valid JSON"
    
# TODO: Add chat context to the model. chat_history
# TODO: improve response type to client.
# TODO: build general MCP client