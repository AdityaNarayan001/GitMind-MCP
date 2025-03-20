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
        print(f"AVAILABLE FEATURES : {cred_response.json()['available_features']['functions']} \n")

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
