import websocket
import json
import ssl
def on_message(ws, message):
    data = json.loads(message)
    if 'e' in data and data['e'] == 'aggTrade':
        symbol = data['s']
        price = float(data['p'])
        print(f"Data Received: {symbol}: {price}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("WebSocket closed")

def on_open(ws):
    print("Starting...")
    ws.send(json.dumps({
        "method": "SUBSCRIBE",
        "params": ["bnbusdt@aggTrade"],
        "id": 1
    }))

if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws",
                                 on_open=on_open,
                                 on_message=on_message,
                                 on_error=on_error,
                                 on_close=on_close)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
