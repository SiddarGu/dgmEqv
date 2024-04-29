import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Create DataFrame with the given data
data = {'Date': ['2021-01-03', '2021-01-10', '2021-01-17', '2021-01-24', '2021-01-31', '2021-02-07', '2021-02-14', '2021-02-21', '2021-02-28', '2021-03-07', '2021-03-14', '2021-03-21', '2021-03-28', '2021-04-04', '2021-04-11', '2021-04-18', '2021-04-25', '2021-05-02', '2021-05-09', '2021-05-16'],
        'Open Price ($)': [75, 78, 76, 81, 85, 86, 84, 86, 88, 90, 93, 94, 97, 99, 100, 102, 105, 107, 108, 110],
        'Close Price ($)': [79, 77, 80, 85, 86, 84, 85, 87, 90, 92, 94, 96, 99, 100, 101, 104, 106, 108, 110, 112],
        'High Price ($)': [81, 82, 83, 88, 89, 87, 88, 90, 92, 94, 96, 98, 101, 103, 104, 106, 108, 110, 112, 114],
        'Low Price ($)': [72, 76, 75, 80, 83, 82, 81, 85, 86, 88, 90, 92, 94, 96, 98, 99, 102, 104, 105, 107]}

df = pd.DataFrame(data)

# Convert 'Date' column to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance requirements
df.rename(columns={'Open Price ($)': 'Open', 'Close Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

mpf.plot(df, type='candlestick', style='blueskies', title='Energy and Utilities Sector Weekly Stock Prices in 2021', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/83_202312302321.png'))
