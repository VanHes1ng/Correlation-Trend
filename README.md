### Correlation Trend Application

![plot](components/main.png)
This Streamlit-based web application allows users to analyze the correlation trends of the top 10 cryptocurrencies in relation to Bitcoin (BTC) and visualize these trends in a table.

#### Key Features:

1. **Market Data Retrieval**:
   - Fetches the top 10 cryptocurrencies by market cap.
   - Defines a date range for data analysis from January 1, 2023, to December 31, 2025.

2. **Historical Price Data**:
   - Fetches historical price data for the top 10 cryptocurrencies within the specified date range.
   - Stores the closing prices of these cryptocurrencies in a DataFrame.

3. **Correlation Analysis**:
   - Calculates the correlation matrix for the closing prices of the top 10 cryptocurrencies.
   - Creates a heatmap to visualize the correlation matrix, highlighting the relationships between different cryptocurrencies.
![plot](components/heatmap.png)

4. **BTC Trend Analysis**:
   - Fetches historical price data for BTC.
   - Calculates the 25-period Simple Moving Average (SMA) for BTC.
   - Determines the binary trend for BTC based on the SMA, categorizing the trend as:
     - 1 (upward trend) if the current SMA value is higher than the previous two values.
     - -1 (downward trend) if the current SMA value is lower than the previous two values.
![plot](components/btc_trend.png)

5. **Adjusted Trend Calculation**:
   - Multiplies the correlation values by the BTC trend to get adjusted trend values.
   - Creates a DataFrame to display the adjusted trend values for each cryptocurrency.
   - Calculates the average of the adjusted trend values.
![plot](components/scores.png)

6. **Additional Information**:
   - Show AVG of all Adjusted Trend Values, which is an overall Crypto Market Trend
   - Provides an "About" section for additional context or information about the application.
![plot](components/avg.png)

### Usage Instructions:

1. **View Correlation Heatmap**:
   - Analyze the correlation heatmap to understand the relationships between the top 10 cryptocurrencies.

2. **Analyze BTC Trend**:
   - Review the BTC trend chart to observe BTC's price movements and it's trend.

3. **Review Adjusted Trends**:
   - Check the adjusted trend values for each cryptocurrency to see it trends.
   - Look at the average adjusted trend value for a summary statistic.

This application provides a comprehensive tool for cryptocurrency traders and analysts to understand market correlations and trends, helping them make informed investment decisions.
