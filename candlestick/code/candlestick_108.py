import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Create DataFrame
data = {'Date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01'],
        'Opening Price ($)': [3000, 3150, 3300, 3450, 3600],
        'Closing Price ($)': [3100, 3250, 3400, 3550, 3700],
        'High Price ($)': [3200, 3300, 3450, 3600, 3750],
        'Low Price ($)': [2900, 3100, 3250, 3400, 3550]}

df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns
df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 
                   'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

# Create figure
fig = plt.figure(dpi=200, figsize=(8, 4))

# Plot candlestick chart
mpf.plot(df, type='candle', style='charles', figratio=(8, 4),
         title='The Auction Price Trend of Fine Arts in the First Quarter of 2021',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/30_202312302321.png'))

plt.close(fig)