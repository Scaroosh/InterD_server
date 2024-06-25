from datetime import datetime
from abc import ABC, abstractmethod

class Broker(ABC):
    @abstractmethod
    def place_market_order(self, symbol, amount):
        pass

    @abstractmethod 
    def get_current_price(self, symbol):
        pass

    @abstractmethod
    def print_order_history(self):
        pass

class VirtualBroker:
    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.order_history = []

    def place_market_order(self, symbol, amount):
        current_price = self.get_current_price(symbol)
        
        if amount > 0:  # Buy order
            if self.portfolio.balance >= amount * current_price:
                self.portfolio.update_position(symbol, amount, current_price)
                self.order_history.append({
                    'type': 'buy',
                    'symbol': symbol,
                    'amount': amount,
                    'price': current_price,
                    'timestamp': datetime.now()
                })
                return True
            else:
                print("Insufficient funds")
                return False
        elif amount < 0:  # Sell order
            if self.portfolio.get_position(symbol) >= abs(amount):
                self.portfolio.update_position(symbol, amount, current_price)
                self.order_history.append({
                    'type': 'sell',
                    'symbol': symbol,
                    'amount': abs(amount),
                    'price': current_price,
                    'timestamp': datetime.now()
                })
                return True
            else:
                print("Insufficient crypto balance")
                return False
        else:
            print("Invalid order amount")
            return False

    def get_current_price(self, symbol):
        return 100  # TODO: API connection

    def print_order_history(self):
        for order in self.order_history:
            print(f"{order['timestamp']}: {order['type'].upper()} {order['amount']} {order['symbol']} @ ${order['price']}")