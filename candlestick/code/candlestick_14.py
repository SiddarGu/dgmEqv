
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Create the DataFrame
df = pd.DataFrame({'Date': ['2019-06-01','2019-06-08','2019-06-15','2019-06-22','2019-06-29'],
                   'Opening Price ($)': [8.5,9.3,10.5,11.1,11.8],
                   'Closing Price ($)': [9.2,10.2,11.6,12.2,12.3],
                   'High Price ($)': [10.1,11.1,12.2,13.1,13.4],
                   'Low Price ($)': [7.8,8.3,10.1,10.5,11.1]})

# Convert the dates to datetime and set them as the index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename the columns to match mplfinance column names
df.rename(columns={'Opening Price ($)': 'Open',
                   'Closing Price ($)': 'Close',
                   'High Price ($)': 'High',
                   'Low Price ($)': 'Low'}, inplace=True)

# Create the figure and plot the candlestick chart
fig = plt.figure(figsize=(8, 5))
mpf.plot(df,type='candle',title='Financial Trends of Education and Academics Sector',savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/22_202312252310.png'))