from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

auth_data = {"username": None, "auth_token": None}

availabe_features = {
        "functions": [
            {
                'id':'F001',
                'function_name':'get_repos',
                'function_description':'Fetches Names of all Repositories.',
            }
        ]
}

@app.route('/healthCheck', methods=['GET'])
def home():
    return jsonify({"status": "OK"})

@app.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()
    auth_token = data.get('auth_token')
    auth_data['auth_token'] = auth_token

    url = "https://api.github.com/user"
    payload = {}
    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {auth_token}',
    'X-GitHub-Api-Version': '2022-11-28'
    }
    response = requests.get(url, headers=headers, data=payload)

    if response.status_code == 200:
        username = response.json()['login']
        auth_data['username'] = username
        return jsonify({"status": "User Verified ✅ ", "username": username, "available_features": availabe_features})
    else:
        return jsonify({"status": "FAILED 🚫 ", "username": "NONE"}), 401

@app.route('/get_repos', methods=['GET'])
def get_repos():
    url = f"https://api.github.com/users/{auth_data['username']}/repos"

    payload = {}
    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'{auth_data["auth_token"]}',
    'X-GitHub-Api-Version': '2022-11-28'
    }

    res = ""
    response = requests.get(url, headers=headers, data=payload)
    if response.status_code == 200:
        response = json.loads(response.text)
        for i in range(len(response)):
            result = dict(response[i])
            result = result['name']
            res += f'{result} \n'
        return jsonify({"result": res})
    else:
        return jsonify({"result": "FAILED"}), 401

if __name__ == '__main__':
    app.run(debug=False)
