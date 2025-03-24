import requests
import json
from utils.llm import llm, chat_history

BASE_URL = "http://127.0.0.1:5000"

print('')
print("GITHUB MCP SERVER CLIENT \n")
try:
    healthCheck = requests.get(f"{BASE_URL}/healthCheck")
    healthCheck.raise_for_status()
    healthCheck = healthCheck.json()
    
    if healthCheck.get('status') == 'OK':
        print("Server is up and running! \n")

        # Prompt user for credentials and Authenticate with GitHub API
        auth_token = input("Enter your GitHub Auth Token: ")

        creds = {"auth_token": auth_token}
        cred_response = requests.post(f"{BASE_URL}/auth", json=creds)
        print('')
        print(f"STATUS   : {cred_response.json()['status']}")
        print(f"USERNAME : {cred_response.json()['username']} \n")
        available_features = cred_response.json()['available_features']['functions']
        print(f"AVAILABLE FEATURES : {available_features} \n")
        chat_history.append({"role": "user", "content": f'{available_features}'})

        # LLM Loop is initiated
        print("Enter your Queries below, type 'exit' to quit. \n")
        while True:
            user_input = input("You 👨 : ")
            if user_input.lower() == "exit":
                print("Exiting chat...")
                break

            llm_response = llm(user_input)
            llm_response = json.loads(llm_response)
            if llm_response['function_name'] == 'None':
                print("LLM 🤖 : ", llm_response['answer'], "\n")
                chat_history.append({"role": "assistant", "content": llm_response['answer']})
            if llm_response['function_name'] == 'get_repos':
                repos_response = requests.get(f"{BASE_URL}/get_repos")
                print("LLM 🤖 : ", llm_response['answer'], "\n")
                chat_history.append({"role": "assistant", "content": llm_response['answer']})
                print(repos_response.json()['result'])
                chat_history.append({"role": "assistant", "content": repos_response.json()['result']})

    else:
        print("Server is down!")
except Exception as e:
    print("Failed to reach server:", e)
