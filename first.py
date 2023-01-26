from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

API_KEY = "PKN9OKD6BB77ZKJUC1B0"
SECRET_KEY = "oOpqI9Vj5J7qeQ1pzmTegFLFNl3YyWh1lZEVVddJ"

end = "https://paper-api.alpaca.markets"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
account = trading_client.get_account()

market_order_data = MarketOrderRequest(
                      symbol="META",
                      qty=1,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.GTC
                  )
market_order = trading_client.submit_order(market_order_data)