from pybit.usdt_perpetual import HTTP
import pp
import time
import config



global api_key
global api_secret

class Client:
    def __init__(self, strategy_name):
        self.strategy_name = strategy_name


    def login(self):

        strategy_name = self.strategy_name

        if strategy_name == "Test real" or strategy_name == None:
            api_key=config.TESTNET_BYBIT_API_KEY
            api_secret=config.TESTNET_BYBIT_API_SECRET
        elif strategy_name == "FXS algo":
            api_key=config.TESTNET_BYBIT_FXS_API_KEY
            api_secret=config.TESTNET_BYBIT_FXS_API_SECRET

        client = HTTP(endpoint="https://api-testnet.bybit.com", api_key=api_key, api_secret=api_secret)
        print('Logged in %s' %(strategy_name))
        return client
    
    client = login(self)
    



    def cancel_all_orders():
        client.cancel_all_active_orders(symbol="ETHUSDT")


    def any_open_positions():

        my_positions = client.my_position(symbol='ETHUSDT')

        for position in my_positions['result']:
            if(position['size']) != 0:
                return True
        
        return False

    def place_order(qty, price, tp, sl):

        pp(client.place_active_order(
        symbol="ETHUSDT",
        side="Buy",
        order_type="Limit",
        qty=qty,
        price=price,
        time_in_force="GoodTillCancel",
        reduce_only=False,
        close_on_trigger=False,
        take_profit=tp,
        stop_loss=sl
    ))

    def get_wallet_usdt_balance():
        wallet_balance = client.get_wallet_balance()
        usdt_balance = wallet_balance['result']['USDT']['wallet_balance']

        return usdt_balance







print(get_wallet_usdt_balance())

# pp(wallet_balance['result']['USDT']['available_balance'])


# pp(cancel)

# active_order = client.get_active_order(symbol="ETHUSDT", order_status="")

# pp(active_order)

# # if active_order['result']['data'] != None:
# #     print('hello')

# pp(active_order['result']['data'])










