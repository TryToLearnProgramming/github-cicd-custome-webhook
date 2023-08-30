from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Define a secret key to validate the webhook requests
# SECRET_KEY = "your_secret_key_here"

SCRIPTS_DIR = "./scripts"

# Define a route to receive the GitHub webhook events
@app.route('/webhook/', methods=['POST'])
def webhook():
    # Check if the request has the correct secret key
    # if request.headers.get('X-Hub-Signature') != f'sha1={hashlib.sha1(SECRET_KEY.encode() + request.data).hexdigest()}':
    #     return jsonify({'message': 'Invalid secret key'}), 401
    
    payload = request.get_json()

    # Extract relevant information from the payload
    event_type = request.headers.get('X-GitHub-Event')
    print("the event => ",event_type)
    # print("Staus", payload[event_type]['status'])
          
    # repository_name = payload['repository']['name']
    tag = payload['tag']
    # Run a shell script based on the event type and repository name
    if event_type == 'workflow_run':
        # subprocess.run(['./scripts/push_script.sh', repository_name], shell=True)
        print("github_actions started...")
        script_path = os.path.join(SCRIPTS_DIR, "action-script.sh")
        subprocess.run(["bash", script_path, tag])
        print("sucessfully run: ", script_path)
    # elif event_type == 'pull_request':
    #     # subprocess.run(['./scripts/pull_request_script.sh', repository_name], shell=True)
    #     print("pull req. created")
    #     script_path = os.path.join(SCRIPTS_DIR, "pull_request_script.sh")
    #     subprocess.run(["bash", script_path])
    #     print("sucessfully run: ", script_path)
    # Add more event types and corresponding scripts as needed

    return jsonify({'message': 'Webhook received'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

