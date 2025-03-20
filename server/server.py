from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/healthCheck', methods=['GET'])
def home():
    return jsonify({"status": "OK"})

@app.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()
    auth_token = data.get('auth_token')

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
        return jsonify({"status": "User Verified ✅ ", "username": username})
    else:
        return jsonify({"status": "FAILED 🚫 ", "username": "NONE"}), 401



# @app.route('/api/data', methods=['GET'])
# def get_data():
#     sample_data = {
#         "id": 1,
#         "name": "Aditya",
#         "role": "Developer"
#     }
#     return jsonify(sample_data)

# @app.route('/api/data', methods=['POST'])
# def post_data():
#     data = request.get_json()
#     return jsonify({"received": data}), 201

if __name__ == '__main__':
    app.run(debug=False)
