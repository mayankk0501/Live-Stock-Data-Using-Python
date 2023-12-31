import websocket, json
from config import *

def on_open(ws):
    print('opened')
    auth_data = {
        "action":"auth",
        "params":API_KEY
    }
    
    ws.send(json.dumps(auth_data))

    channel_data = {
        "action":"subscribe",
        "params":TICKERS
    }

    ws.send(json.dumps(channel_data))

def on_close(ws):
    print('connection closed')

def on_message(ws, message):
    print('Received a message')
    print(message)

socket = 'wss://delayed.polygon.io/stocks'

ws = websocket.WebSocketApp(socket, on_open = on_open, on_message = on_message, on_close = on_close)
ws.run_forever()