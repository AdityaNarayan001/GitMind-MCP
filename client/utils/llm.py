import ollama
import json

from utils.system_prompt import sys_prompt

def llm(available_features, content):
    messages = [
        {"role": "system", "content": 'Instructions : ' + f'{sys_prompt}' + 'Available Features : ' + f'{available_features}'},
        {"role": "user", "content": f'{content}'}
    ]

    response = ollama.chat(
        model="llama3.1", 
        messages=messages,
        options= {
            "temperature": 0.2
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