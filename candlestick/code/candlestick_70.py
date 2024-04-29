import pandas as pd
import mplfinance as mpf

# Define the data
data = {'Date': ['2020-01-06', '2020-01-13', '2020-01-20', '2020-01-27', '2020-02-03', '2020-02-10', '2020-02-17'],
        'Open Price (Solar Power Stock $)': [68, 70, 71, 72.5, 74, 75.5, 76],
        'Close Price (Solar Power Stock $)': [69.5, 70.8, 72, 73, 75, 76, 78],
        'High Price (Solar Power Stock $)': [70.2, 71.2, 73.5, 74, 76.8, 78, 79.5],
        'Low Price (Solar Power Stock $)': [65.7, 68.9, 70.8, 71, 72, 73.8, 75.6]}
df = pd.DataFrame(data)

# Convert 'Date' column to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance column requirements
df.rename(columns={'Open Price (Solar Power Stock $)': 'Open',
                   'Close Price (Solar Power Stock $)': 'Close',
                   'High Price (Solar Power Stock $)': 'High',
                   'Low Price (Solar Power Stock $)': 'Low'}, inplace=True)

# Create a figure and plot the candlestick chart
fig = mpf.plot(df, type='candle', title='Solar Energy Company\'s Weekly Stock Performance',
               figratio=(12,6), style='yahoo', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/86_202312302321.png'))