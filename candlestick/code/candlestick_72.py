import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Data
data = {
    'Date': ['2021-03-01', '2021-03-02', '2021-03-03', '2021-03-04', '2021-03-05', '2021-03-06', '2021-03-07', '2021-03-08', '2021-03-09', '2021-03-10'],
    'Opening Price': [30, 34, 33, 36, 38, 35.2, 37, 38.5, 39, 42.5],
    'Closing Price': [33, 32, 35.2, 37.5, 35, 36.7, 38, 38.2, 42, 45],
    'High Price': [35, 36, 37, 38.5, 39, 38, 40, 42, 44, 47],
    'Low Price': [27.5, 31, 32.8, 35.6, 34, 34.5, 36, 35, 38.5, 41]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as index
df.set_index('Date', inplace=True)

# Rename columns
df.rename(columns={'Opening Price': 'Open', 'Closing Price': 'Close', 'High Price': 'High', 'Low Price': 'Low'}, inplace=True)

# Create candlestick chart
mpf.plot(df, type='candle', title='Daily Stock Performance in Manufacturing and Production Sector',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/87_202312302321.png'),
         figratio=(8, 6), style='yahoo')