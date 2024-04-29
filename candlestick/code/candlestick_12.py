
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = [['2019-05-01', 179, 183, 190, 172], 
        ['2019-05-08', 182, 179, 192, 177],
        ['2019-05-15', 184, 178, 189, 173],
        ['2019-05-22', 181, 185, 196, 175],
        ['2019-05-29', 186, 184, 195, 177],
        ['2019-06-05', 184, 187, 197, 180]]

df = pd.DataFrame(data, columns=['Date', 'Open Price (US$)', 'Close Price (US$)', 'High Price (US$)', 'Low Price (US$)'])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={'Open Price (US$)': 'Open', 
                    'Close Price (US$)': 'Close', 
                    'High Price (US$)': 'High', 
                    'Low Price (US$)': 'Low'}, inplace=True)

mpf.plot(df, type='candle', style="brasil", update_width_config=dict(candle_linewidth=1.75), title='Social Sciences and Humanities Market Index Performance Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/1_202312252258.png'), figratio=(12, 6))