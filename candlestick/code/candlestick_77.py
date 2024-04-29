import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# Create the DataFrame
data = {'Date': ['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', '2018-01-06'],
        'Opening Price': [1200, 1230, 1220, 1250, 1280, 1300],
        'Closing Price': [1230, 1220, 1250, 1280, 1300, 1290],
        'High Price': [1250, 1255, 1270, 1300, 1320, 1325],
        'Low Price': [1180, 1200, 1205, 1220, 1250, 1270]}

df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance column requirements
df.rename(columns={'Opening Price': 'Open', 'Closing Price': 'Close', 'High Price': 'High', 'Low Price': 'Low'}, inplace=True)

# Create the figure
fig = plt.figure()

# Create the candlestick chart
mpf.plot(df, type='candle', figratio=(12,6), style='yahoo', title='Contemporary Art Market Trends in the First Week of 2018', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/64_202312302321.png'))