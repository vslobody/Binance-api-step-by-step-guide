import os
from time import sleep

from binance.client import Client
from binance import ThreadedWebsocketManager as ThreadedWebsocketManager

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)
btc_price = {'error':False}

def btc_trade_history(msg):    
    print(f"message type: {msg['e']}")
    print(msg)


# init and start the WebSocket
twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
twm.start()
conn_key = twm.start_symbol_ticker_socket(symbol='BNBBTC', callback=btc_trade_history)

# put script to sleep to allow WebSocket to run for a while
# this is just for example purposes
sleep(30)

# stop websocket
bsm.stop_socket(conn_key)
