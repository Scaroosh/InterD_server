from binance.client import Client
import time

api_key = 'your_api_key_here'
api_secret = 'your_api_secret_here'

# Initialize the Binance client
client = Client(api_key, api_secret)

# Get account information
account = client.get_account()

# Print the account information
print(account)

def get_latest_price(symbol):
    """Get the latest price of a given symbol."""
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

def make_order(symbol, side, quantity):
    """Place an order."""
    try:
        print(f"Placing {side} order for {quantity} of {symbol}.")
        order = client.order_market(
            symbol=symbol,
            side=side,
            quantity=quantity
        )
    except Exception as e:
        print("An error occurred - ", e)
        return False
    return True

def simple_trading_logic(symbol, quantity, buy_threshold, sell_threshold):
    """Simple trading logic."""
    price = get_latest_price(symbol)
    print(f"Current price of {symbol}: {price}")

    if price < buy_threshold:
        # Buy if the price is below a certain threshold
        result = make_order(symbol, 'BUY', quantity)
        if result:
            print("Buy order executed.")
    elif price > sell_threshold:
        # Sell if the price is above a certain threshold
        result = make_order(symbol, 'SELL', quantity)
        if result:
            print("Sell order executed.")

# Example parameters
symbol = 'BTCUSDT'
quantity = 0.001  # Define your quantity based on your account balance and risk management
buy_threshold = 19000  # Example threshold in USD
sell_threshold = 21000  # Example threshold in USD

# Running the trading logic every 60 seconds
while True:
    simple_trading_logic(symbol, quantity, buy_threshold, sell_threshold)
    time.sleep(60)  # Sleep for 60 seconds before checking again
