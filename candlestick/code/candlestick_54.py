import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {
    'Date': ['2019-01-01', '2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01', '2019-06-01', '2019-07-01'],
    'Opening Price ($)': [1000, 1050, 1200, 1300, 1400, 1500, 1600],
    'Closing Price ($)': [1050, 1200, 1300, 1400, 1500, 1600, 1700],
    'High Price ($)': [1100, 1210, 1500, 1450, 1550, 1650, 1750],
    'Low Price ($)': [950, 1000, 1150, 1300, 1375, 1450, 1600]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

savefig = dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/26_202312302321.png')

mpf.plot(df, type='candle', title='Monthly Stock Performance of Leading Education Company', figratio=(12,6), savefig=savefig)
