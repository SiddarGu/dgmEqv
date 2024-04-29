import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# Create DataFrame
data = {'Date': ['2020-03-02', '2020-03-03', '2020-03-04', '2020-03-05', '2020-03-06', '2020-03-07', '2020-03-08', '2020-03-09', '2020-03-10', '2020-03-11'],
        'Opening Price ($)': [200, 210, 215, 225, 217, 230, 235, 238, 242, 245],
        'Closing Price ($)': [210, 215, 210, 215, 220, 235, 232, 240, 245, 247],
        'High Price ($)': [215, 220, 217, 230, 225, 240, 238, 243, 247, 255],
        'Low Price ($)': [195, 200, 205, 210, 210, 225, 230, 235, 238, 243]}
df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance column requirements
df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

# Create figure
fig = plt.figure()

# Plot candlestick chart
mpf.plot(df, type='candle', figratio=(12,6), style='classic', title='E-commerce Company\'s Stock Price Fluctuation in First Week of March 2020',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/91_202312302321.png'))

plt.close(fig)