
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# Load data
data = [['2019-01',50,52,54,48],
        ['2019-02',54,56,59,51],
        ['2019-03',58,56,60,53],
        ['2019-04',62,59,65,56],
        ['2019-05',50,52,54,48],
        ['2019-06',54,56,58,52],
        ['2019-07',58,56,59,54],
        ['2019-08',62,59,65,56]]

# Create a DataFrame
df = pd.DataFrame(data, columns=['Month','Open','Close','High','Low'])
df['Month'] = pd.to_datetime(df['Month'])

# Set 'Month' as index
df.set_index('Month', inplace=True)

# Create candlestick chart
fig = plt.figure(figsize=(10,7))
mpf.plot(df,
         type='candle',
         title='Government and Public Policy Financial Trend Analysis',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/17_202312252310.png'))