
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

df = pd.DataFrame({"Date": ["2019-05-01", "2019-05-02", "2019-05-03", "2019-05-04", "2019-05-05", "2019-05-06", "2019-05-07"],
                   "Opening Price ($)": [50, 55, 52, 53, 51, 54, 51],
                   "Closing Price ($)": [56, 56.8, 54.2, 54.6, 55.4, 55, 53.2],
                   "High Price ($)": [57.2, 58.3, 55.6, 56.7, 56.9, 57, 55.4],
                   "Low Price ($)": [48.2, 53.5, 51.4, 50.5, 49.8, 51.2, 49.7]})

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.rename(columns={"Opening Price ($)": "Open",
                        "Closing Price ($)": "Close",
                        "High Price ($)": "High",
                        "Low Price ($)": "Low"})

fig = plt.figure(figsize=(20, 10))
mpf.plot(df, type='candle', title='Financial Performance of Retail and E-commerce Companies - Weekly Overview',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/3_202312252258.png'), figratio=(12, 6))