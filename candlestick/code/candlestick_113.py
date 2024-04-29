
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

data = [['2019-10-22',110,112,115,105],
        ['2019-10-23',113,110,114,108],
        ['2019-10-24',113,111,114,109],
        ['2019-10-25',111,112,113,109],
        ['2019-10-26',112,110,114,108],
        ['2019-10-27',110,113,114,108],
        ['2019-10-28',112,110,114,108],
        ['2019-10-29',111,112,113,109]]

df = pd.DataFrame(data, columns=['Date','Open Price ($)','Close Price ($)','High Price ($)','Low Price ($)'])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)
df = df.rename(columns={"Open Price ($)": "Open", "Close Price ($)": "Close", "High Price ($)": "High", "Low Price ($)": "Low"})

fig = plt.figure(figsize=(15,5))
mpf.plot(df,type='candle',title='Financial Stock Performance - Recent Week Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/25_202312252310.png'))