import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Data
data = {'Date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01'],
        'Open Price ($)': [215000, 220000, 225000, 240000, 245000],
        'Close Price ($)': [220000, 225000, 235000, 245000, 250000],
        'High Price ($)': [225000, 230000, 240000, 250000, 255000],
        'Low Price ($)': [210000, 215000, 220000, 235000, 240000]}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns
df.rename(columns={'Open Price ($)': 'Open', 'Close Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

# Plot candlestick chart
mpf.plot(df, type='candle', figratio=(12,6), style='yahoo', title='Monthly Housing Market Prices for 2021', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/63_202312302321.png'))