import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Create DataFrame from data
data = {
    'Date': ['2020-03-11', '2020-03-12', '2020-03-13', '2020-03-14', '2020-03-15',
             '2020-03-16', '2020-03-17', '2020-03-18', '2020-03-19', '2020-03-20'],
    'Open Price ($)': [200, 210, 220, 210, 238, 242, 248, 250, 280, 295],
    'Close Price ($)': [205, 220, 215, 230, 235, 250, 260, 270, 285, 300],
    'High Price ($)': [210, 225, 228, 235, 240, 255, 265, 275, 290, 305],
    'Low Price ($)': [195, 205, 210, 208, 230, 240, 243, 248, 275, 290]
}

df = pd.DataFrame(data)

# Convert Date to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance requirements
df.rename(columns={'Open Price ($)': 'Open', 'Close Price ($)': 'Close',
                   'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

# Create candlestick chart using mplfinance
mpf.plot(df, type='candle', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/45_202312302321.png'),
         style='classic', figratio=(12,6), title='Daily Stock Price Fluctuations in Legal Sector')
