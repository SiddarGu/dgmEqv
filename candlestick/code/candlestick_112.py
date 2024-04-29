import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# Initialize the data
data = {'Date': ['2022-06-01', '2022-06-02', '2022-06-03', '2022-06-04', '2022-06-05', '2022-06-06', '2022-06-07', '2022-06-08', '2022-06-09', '2022-06-10'],
        'Opening Price ($)': [83.55, 85.25, 87.12, 86.80, 88.82, 91.00, 92.70, 94.60, 96.35, 97.95],
        'Closing Price ($)': [85.27, 86.90, 86.78, 88.53, 90.52, 92.68, 94.37, 96.25, 97.99, 99.62],
        'High Price ($)': [86.55, 88.22, 89.05, 90.10, 91.98, 94.19, 95.77, 97.67, 99.42, 101.06],
        'Low Price ($)': [81.43, 84.38, 85.90, 85.78, 87.54, 90.03, 91.66, 93.54, 95.31, 97.30]}
df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# Rename columns to match mplfinance column requirements
df = df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'})

# Create the candlestick chart
mpf.plot(df, type='candle', figratio=(12,6), style='classic', title='Food and Beverage Industry: Market Performance Over 10 Days', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/89_202312302321.png'))