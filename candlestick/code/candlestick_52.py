import pandas as pd
import mplfinance as mpf

# Create the DataFrame
data = {'Date':['2021-01-26', '2021-02-02', '2021-02-09', '2021-02-16', '2021-02-23'],
        'Open Price ($)':[2530, 2580, 2640, 2705, 2810],
        'Close Price ($)':[2580, 2630, 2700, 2800, 2900],
        'High Price ($)':[2600, 2650, 2750, 2820, 2950],
        'Low Price ($)':[2500, 2560, 2630, 2685, 2800]}

df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns
df.rename(columns={'Open Price ($)':'Open', 'Close Price ($)':'Close', 'High Price ($)':'High', 'Low Price ($)':'Low'}, inplace=True)

mpf.plot(df, figratio=(12,6), type='candle', title='Weekly Trends in Production Manufacturing Equipment Prices', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/72_202312302321.png'))
