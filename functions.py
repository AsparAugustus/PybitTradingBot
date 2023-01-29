from pybit.usdt_perpetual import HTTP
import pp
import time
import config

client = HTTP(endpoint="https://api-testnet.bybit.com", api_key=config.TESTNET_BYBIT_API_KEY, api_secret=config.TESTNET_BYBIT_API_SECRET)
print('loggedin')

def cancel_all_orders():
    client.cancel_all_active_orders(symbol="ETHUSDT")


def any_positions():

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





wallet_balance = client.get_wallet_balance()

# pp(wallet_balance['result']['USDT']['available_balance'])


# pp(cancel)

# active_order = client.get_active_order(symbol="ETHUSDT", order_status="")

# pp(active_order)

# # if active_order['result']['data'] != None:
# #     print('hello')

# pp(active_order['result']['data'])








