
import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf

data = [['2020-02', 50.2, 53.1, 54.2, 49.8],
        ['2020-03', 51.5, 54.2, 56.1, 49.7],
        ['2020-04', 53.7, 55.2, 57.1, 51.6],
        ['2020-05', 56.4, 59.8, 60.5, 54.3],
        ['2020-06', 60.3, 59.9, 61.8, 57.4],
        ['2020-07', 54.7, 56.2, 58.3, 53.2],
        ['2020-08', 55.5, 58.2, 59.1, 54.3],
        ['2020-09', 58.2, 59.3, 60.4, 56.1]]

df = pd.DataFrame(data, columns=['Month','Open Price ($)','Close Price ($)','High Price ($)','Low Price ($)'])
df['Month'] = pd.to_datetime(df['Month'],format='%Y-%m')
df.set_index('Month',inplace=True)
df.rename(columns={'Open Price ($)':'Open','Close Price ($)':'Close','High Price ($)':'High','Low Price ($)':'Low'},inplace=True)

plt.figure(figsize=(12,6))
mpf.plot(df,type='candle',title='Real Estate and Housing Market Price Trend Analysis',savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/16_202312252310.png'))