import pandas
import os
from binance.client import Client
 

api_key = os.environ['BINANCE_API_KEY']
api_secret = os.environ['BINANCE_API_SECRET']

# connect to Binance
client = Client(api_key, api_secret, testnet=True)
 
# Retrieve tickers and format in DataFrame
tickers = client.get_all_tickers()
df = pandas.DataFrame(tickers)
df.set_index('symbol', inplace=True)
print(df.head(20))