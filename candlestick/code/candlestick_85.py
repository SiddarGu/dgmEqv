import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# Define the data
data = {'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08', '2021-01-09'],
        'Opening Value ($)': [120.5, 123.6, 124.8, 125.2, 128.9, 131.2, 134.6, 136.2, 138.6],
        'Closing Value ($)': [123.5, 124.5, 125.1, 128.7, 131.0, 134.5, 136.0, 138.5, 140.0],
        'Peak Value ($)': [127.0, 128.0, 129.0, 130.8, 133.2, 135.9, 140.1, 141.8, 142.9],
        'Lowest Value ($)': [118.4, 120.0, 122.5, 123.8, 125.6, 129.5, 132.1, 133.9, 135.5]}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns
df.rename(columns={'Opening Value ($)': 'Open', 'Closing Value ($)': 'Close', 'Peak Value ($)': 'High', 'Lowest Value ($)': 'Low'}, inplace=True)

# Create candlestick chart
mpf.plot(df, type='candle', title='Social Media Industry Stocks Fluctuations', figratio=(12,6), style='charles',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/27_202312302321.png'))