
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

from datetime import datetime from flask 
import Flask, request, jsonify app = 
Flask(__name__) @app.route('/api', 
methods=['GET']) def get_info():
    slack_name = 
    request.args.get('HNGx') track = 
    request.args.get('backend') 
    current_day = 'Sunday' utc_time = 
    '2023-09-11T23:01:04.072Z' 
    github_file_url = 
    "https://github.com/luckysitara/bug-free-hng_repo/blob/main/flask_app.py" 
    github_repo_url = 
    "https://github.com/luckysitara/bug-free-hng_repo.git" 
    status_code = 200 response = {
        'slack_name': slack_name, 
        'current_day': current_day, 
        'utc_time': utc_time, 'track': 
        track, 'github_file_url': 
        github_file_url, 
        'github_repo_url': 
        github_repo_url, 'status_code': 
        status_code
    }
    return jsonify(response) if __name__ 
== '__main__':
    app.run(host='0.0.0.0', port=5000)
