import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# Create DataFrame with the given data
data = {
    'Date': ['2022-03-01', '2022-03-02', '2022-03-03', '2022-03-04', '2022-03-05', '2022-03-06', '2022-03-07', '2022-03-08', '2022-03-09', '2022-03-10'],
    'Opening Price': [120, 122, 125, 130, 134, 138, 142, 146, 149, 153],
    'Close Price': [122, 124, 128, 134, 136, 142, 145, 148, 152, 156],
    'High Price': [125, 128, 132, 138, 140, 145, 148, 150, 156, 159],
    'Low Price': [118, 120, 123, 126, 130, 135, 140, 144, 147, 150]
}

df = pd.DataFrame(data)

# Convert 'Date' column to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance column requirements
df.rename(columns={'Opening Price': 'Open', 'High Price': 'High', 'Low Price': 'Low', 'Close Price': 'Close'}, inplace=True)

# Create figure
fig = plt.figure(figsize=(10, 6))

# Create candlestick chart using mplfinance
mpf.plot(df, type='candle', style='yahoo', figratio=(6, 1.5), title='March 2022 Stock Trends in Transportation and Logistics Sector', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/117_202312302321.png'))
