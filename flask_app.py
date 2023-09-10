from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.now(pytz.UTC).strftime('%A')

    # Get the current UTC time
    utc_time = datetime.utcnow().replace(tzinfo=pytz.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub URLs
    github_file_url = "https://github.com/luckysitara/mysite/blob/main/flask_app.py"
    github_repo_url = "https://github.com/luckysitara/mysite"

    # Status Code
    status_code = 200

    # Create the response JSON
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': status_code
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040)

