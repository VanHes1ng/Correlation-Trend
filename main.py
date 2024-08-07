import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import time
from functions import get_market_caps, get_historical_data, get_trend_val

# Set Page Configurations
st.set_page_config(
    page_title="Correlation Trend",
    page_icon="📊",
    layout="wide"
)
[_, c, _] = st.columns([1, 15, 1])

# WELCOME
welcome = c.title("***:blue[Welcome] to Crypto Correlation App***")
time.sleep(.5)
welcome.empty()
welcome = c.title("***Welcome :blue[to] Crypto Correlation App***")
time.sleep(.5)
welcome.empty()
welcome = c.title("***Welcome to :blue[Crypto] Correlation App***")
time.sleep(.5)
welcome.empty()
welcome = c.title("***Welcome to Crypto :blue[Correlation] App***")
time.sleep(.5)
welcome.empty()
welcome = c.title("***Welcome to Crypto Correlation :blue[App]***")
time.sleep(.5)
welcome.empty()
c.title("***:blue[Crypto] Correlation App***")

about = open("components/about.txt", "r")

option = c.selectbox(
    "Which Coin would you like to be ploted?",
    ("BTC", "ETH", "BNB", "ADA", "SOL", "XRP", "DOT", "DOGE", "UNI", "LTC"))

# Get market cap data
top_10_cryptos = get_market_caps()

# Define the date range
end_date = datetime.strptime('2050-12-31', '%Y-%m-%d')

# Fetch historical price data for the top 10 cryptocurrencies
price_data = pd.DataFrame()
for symbol in top_10_cryptos:
    data = get_historical_data(symbol, end_date)
    price_data[symbol] = data['close']

# Calculate the correlation matrix
correlation_matrix = price_data.corr()

# Create a heatmap of the correlation matrix
fig1 = plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='black')

# Fetch historical data for BTC
_data = get_historical_data(option, end_date)

btc_data = get_historical_data("BTC", end_date)

# Calculate the 25-period SMA
btc_data['SMA_25'] = btc_data['close'].rolling(window=25).mean()
_data['SMA_25']    = _data['close'].rolling(window=25).mean()

# Determine the binary trend for BTC
btc_data['SMA_Trend']= get_trend_val(btc_data)
_data['SMA_Trend']   = get_trend_val(_data)

# Plot BTC close price and SMA with color change based on trend
fig2 = plt.figure(figsize=(14, 7))
plt.plot(_data['close'], label=f'{option} Close Price', color='black', linewidth=1)
sma_color = ['red' if x == -1 else '#5396ec' for x in _data['SMA_Trend']]
plt.plot(_data['SMA_25'], label='SMA 25', color='black', linewidth=2, alpha=0.7)
for i in range(len(_data) - 1):
    plt.plot(_data.index[i:i+2], _data['SMA_25'].iloc[i:i+2], color=sma_color[i], linewidth=3)

plt.title(f'{option} Close Price with SMA 25')
plt.legend()

# Get the last value of BTC trend
btc_trend = btc_data['SMA_Trend'].iloc[-1]

# Multiply the correlation values by the BTC trend
adjusted_trends = round(correlation_matrix['BTC'] * btc_trend,2)

# Create a DataFrame to display the results
trend_table = pd.DataFrame({
    'Coin': adjusted_trends.index,
    'Adjusted Trend': adjusted_trends.values
})

avg_tren = round(trend_table.loc[:, 'Adjusted Trend'].mean(),2)

with c:
    [c1, c2] = st.columns([1.2, 2])

    c1.subheader("Correlation Top :blue[10]")
    c1.pyplot(fig1, use_container_width = True)
    c2.subheader(f":orange[{option}] TREND")
    c2.pyplot(fig2, use_container_width = True)
    c1.divider()
    c2.divider()
    c1.subheader("Adjusted Trend Values")
    c1.dataframe(trend_table.style.highlight_max(subset="Adjusted Trend", color="#5396ec"), use_container_width = True, hide_index=True)
    c2.metric(label="Overall Market Crypto Trend (AVG)", value=avg_tren)

    with c2.expander("DESCRIPTION:"):
        st.markdown(about.read())

    st.divider()
    st.write('''Crypto Correlation App 2024\n
             This site is for informational purposes only. The information on our website is not financial advice, and you should not consider it to be financial advice.''')

    st.write("@VanHes1ng")

    st.write('''TradingView: https://www.tradingview.com/u/VanHe1sing/\n 
Telegram: https://t.me/IvanKocherzhat\n 
GitHub: https://github.com/VanHes1ng\n
X: https://x.com/Van_He1sing           
''')

     
