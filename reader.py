from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Define a secret key to validate the webhook requests
# SECRET_KEY = "your_secret_key_here"

SCRIPTS_DIR = "/home/ubuntu/scripts"

# Define a route to receive the GitHub webhook events
@app.route('/webhook', methods=['POST'])
def webhook():
    # Check if the request has the correct secret key
    # if request.headers.get('X-Hub-Signature') != f'sha1={hashlib.sha1(SECRET_KEY.encode() + request.data).hexdigest()}':
    #     return jsonify({'message': 'Invalid secret key'}), 401
    
    payload = request.get_json()

    # Extract relevant information from the payload
    event_type = request.headers.get('X-GitHub-Event')
    print("the event => ",event_type)
    print("Staus", payload[event_type]['status'])
          
    repository_name = payload['repository']['name']

    # Run a shell script based on the event type and repository name
    if event_type == 'push':
        # subprocess.run(['./scripts/push_script.sh', repository_name], shell=True)
        print("push happend")
        script_path = os.path.join(SCRIPTS_DIR, "pull_request_script.sh")
        subprocess.run(["bash", script_path])
        print("sucessfully run: ", script_path)
    elif event_type == 'pull_request':
        # subprocess.run(['./scripts/pull_request_script.sh', repository_name], shell=True)
        print("pull req. created")
        script_path = os.path.join(SCRIPTS_DIR, "pull_request_script.sh")
        subprocess.run(["bash", script_path])
        print("sucessfully run: ", script_path)
    # Add more event types and corresponding scripts as needed

    return jsonify({'message': 'Webhook received'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


# import os
# import subprocess
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Replace with your own SECRET_KEY for webhook security
# SECRET_KEY = "your_secret_key_here"

# # Replace with the path to your scripts directory
# SCRIPTS_DIR = "/path/to/scripts/directory"

# @app.route("/webhook", methods=["POST"])
# def webhook_handler():
#     event_type = request.headers.get("X-GitHub-Event")
    
#     # Verify the payload using your SECRET_KEY here
    
#     if event_type == "push":
#         payload = request.json
#         ref = payload["ref"]
        
#         # Customize this part to trigger specific scripts based on the ref
#         if ref == "refs/heads/main":
#             script_path = os.path.join(SCRIPTS_DIR, "main.sh")
#             subprocess.run(["bash", script_path])
#             return jsonify({"message": "Script triggered successfully."}), 200
    
#     return jsonify({"message": "Event not processed."}), 200

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)
