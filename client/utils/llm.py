import ollama
import json

from utils.system_prompt import sys_prompt

def llm(available_features, content):
    messages = [
        {"role": "system", "content": 'Available Features : ' + f'{available_features}' + 'Instructions : ' + f'{sys_prompt}'},
        {"role": "user", "content": f'{content}'}
    ]

    response = ollama.chat(model="llama3.1", messages=messages)

    try:
        json_response = json.loads(response['message']['content'])
        return json.dumps(json_response, indent=2)
    except json.JSONDecodeError:
        return "Error: Response is not valid JSON"