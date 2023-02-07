import json, config
from flask import Flask, request, jsonify
from functions import cancel_all_orders, any_open_positions, place_order, client
from chart import save_chart_data
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
    

    price = round(data['strategy']['order_price'], 2)

    qty = data['strategy']['market_position_size']


    sl = round(data['strategy']['order_price'] * 0.99, 2)
    tp = round(data['strategy']['order_price'] * 1.01, 2)




  

    if (data['strategy']['order_id'] == 'long') and (any_open_positions() == False):


        if (data['strategy']['alertmessage'] is not None):
            alert_message = data['strategy']['alertmessage'] 
            # print("alert_message", alert_message)

            number_strings = alert_message.split(', ')

            numbers = [round(float(num), 2) for num in number_strings]


            price = numbers[0]
            sl = numbers[1]
            tp = numbers[2]

            ##place_order(qty, price, tp, sl):

            print(price, tp, sl)

            cancel_all_orders()

            

            place_order(qty, price, tp, sl)

            save_chart_data()


    

    

    return {
        # str(request.data)
        "code" : "success",
        "message" : str(request.data),
        "order" : "Placed an order of %d ETH at %f, with TP at %f and SL at %f" %(qty, price, tp, sl)
    }