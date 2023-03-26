# Binance BNB/USDT Price Fetcher

This Python project retrieves the BNB/USDT price from the Binance WebSocket API and prints the updates in real-time. The project uses the `websocket-client` library to establish a WebSocket connection to the Binance API.

## Libraries

- `websocket-client`: A WebSocket client library for Python that provides a simple interface for connecting to WebSocket servers and handling WebSocket messages.
- `json`: A built-in Python library for encoding and decoding JSON data.
- `ssl`: A built-in Python library for SSL/TLS support.

## Usage

1. Install the `websocket-client` library:

```bash
pip install websocket-client
```

2. Run the Script
```bash
python binance_websocket.py
```
You should see real-time BNB/USDT price updates printed in your terminal.

## Info

The script provided in this project disables SSL certificate verification. This is for testing purposes only and should not be used in production environments. It's recommended to resolve the root cause of SSL certificate verification issues on your system instead of disabling SSL certificate verification.
