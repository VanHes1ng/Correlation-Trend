import pandas as pd
from binance.client import Client
import streamlit as st
# Initialize the Binance client
client = Client()

# Function to fetch market cap data from Binance
def get_market_caps():
    info = client.get_all_tickers()
    prices = {item['symbol']: float(item['price']) for item in info if item['symbol'].endswith('USDT')}
    
    # Assuming we have a dictionary with market caps for the sake of this example
    market_caps = {
        'BTCUSDT': 1000000000,
        'ETHUSDT': 200000000,
        'BNBUSDT': 50000000,
        'ADAUSDT': 30000000,
        'SOLUSDT': 25000000,
        'XRPUSDT': 23000000,
        'DOTUSDT': 22000000,
        'DOGEUSDT':20000000,
        'UNIUSDT': 19000000,
        'LTCUSDT': 18000000
    }

    sorted_symbols = sorted(market_caps, key=market_caps.get, reverse=True)[:10]
    return sorted_symbols



# Function to fetch historical data from Binance
@st.cache_data
def get_historical_data(symbol, start, end):
    klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1DAY, start.strftime('%d %b %Y'), end.strftime('%d %b %Y'))
    data = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
    data.set_index('timestamp', inplace=True)
    data = data[['close']].astype(float)
    return data