import pandas as pd

import streamlit as st
import cryptocompare

# Function to fetch market cap data from Binance
def get_market_caps():

    # Assuming we have a dictionary with market caps for the sake of this example
    market_caps = {
        'BTC': 1000000000,
        'ETH': 200000000,
        'BNB': 50000000,
        'ADA': 30000000,
        'SOL': 25000000,
        'XRP': 23000000,
        'DOT': 22000000,
        'DOGE':20000000,
        'UNI': 19000000,
        'LTC': 18000000
    }

    sorted_symbols = sorted(market_caps, key=market_caps.get, reverse=True)[:10]
    return sorted_symbols



# Function to fetch historical data from Binance
@st.cache_data
def get_historical_data(symbol, end_date):
    cryptocompare.cryptocompare._set_api_key_parameter("8fcc98eb2d8de315ea41c547c2565e23773f9ec70d79d89546680c8820203821")
    data = cryptocompare.get_historical_price_day(symbol, currency='USD', toTs=end_date, limit=365)
    df = pd.DataFrame(data)
    if 'time' in df.columns:
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.set_index('time', inplace=True)
    return df

