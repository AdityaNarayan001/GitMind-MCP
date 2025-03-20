import requests
from utils.llm import llm

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

        # LLM Loop is initiated
        print("Enter your Queries below, type 'exit' to quit. \n")
        while True:
            user_input = input("You 👨 : ")
            if user_input.lower() == "exit":
                print("Exiting chat...")
                break
            llm_response = llm(available_features, user_input)
            print("LLM 🤖 : ", llm_response, "\n")

    else:
        print("Server is down!")
except Exception as e:
    print("Failed to reach server:", e)





# # GET request
# response = requests.get(f"{BASE_URL}/api/data")
# print("GET Response:", response.json())

# # POST request
# data = {"id": 2, "name": "Narayan", "role": "Engineer"}
# response = requests.post(f"{BASE_URL}/api/data", json=data)
# print("POST Response:", response.json())
