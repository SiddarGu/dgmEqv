import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# Define the data
data = {'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01', '2020-10-01', '2020-11-01', '2020-12-01'],
        'HR Budget Opening ($)': [50000, 52000, 54000, 55000, 56000, 58000, 59000, 61000, 62000, 63000, 65000, 66000],
        'HR Budget Closing ($)': [52000, 54000, 55000, 56000, 58000, 59000, 61000, 62000, 63000, 65000, 66000, 68000],
        'HR Budget High ($)': [53000, 56000, 56000, 57000, 59000, 60000, 62000, 64000, 64000, 66000, 67000, 69000],
        'HR Budget Low ($)': [48000, 51000, 52000, 54000, 55000, 56000, 58000, 60000, 61000, 62000, 64000, 65000]}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as index
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance column requirements
df.rename(columns={'HR Budget Opening ($)': 'Open', 'HR Budget Closing ($)': 'Close', 'HR Budget High ($)': 'High', 'HR Budget Low ($)': 'Low'}, inplace=True)

# Create a candlestick chart using mplfinance.plot()
mpf.plot(df, type='candle', title='Human Resources Monthly Budget Trend in 2020',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/65_202312302321.png'),
         figratio=(12,6))
