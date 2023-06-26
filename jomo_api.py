from get_recommendations import get_recommendations
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/jomo-recommendations', methods=['POST'])
def testing():
    request_json = request.json
    query = request_json['query']

    response = get_recommendations(query = query)
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
