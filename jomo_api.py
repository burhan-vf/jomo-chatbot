from get_recommendations import get_recommendations
from flask import Flask, request
from flask_cors import CORS
import json
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app, origins=['https://jomofechatbot.virtualforce.io'], methods=['GET', 'POST'])

@app.route('/jomo-recommendations', methods=['POST', 'GET'])
def testing():
    request_json = request.json
    query = request_json['query']

    response = get_recommendations(query = query)
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
