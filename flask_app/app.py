from flask import Flask
from flask import request, jsonify
from random import sample

server = Flask(__name__)

@server.route('/health', methods=['GET'])
def health():
    return "App is Running"

@server.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'The model is up and running. Send a POST request'
    else:
        return 'This Post request'

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=8001)