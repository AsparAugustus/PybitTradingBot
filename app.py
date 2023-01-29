import json, config
from flask import Flask, request, jsonify
from functions import cancel_all_orders, any_positions, place_order, client
import pp
import time



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST'])
def webhook():

    data = json.loads(request.data)

    if data['passphrase'] != config.WEBHOOK_PASSPHRASE or data['passphrase'] is None :
        return {
            "code" : "error",
            "message" : "Invalid passphrase"
        }
    
    print(data)

    return {
        
        "code" : "success",
        "message" : str(request.data)
    }