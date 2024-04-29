
import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas as pd

data = [['2020-05-10', 80.5, 82.3, 84.2, 78.8], 
        ['2020-05-17', 83.1, 82.2, 85.2, 80.9],
        ['2020-05-24', 83.4, 82.7, 84.2, 81.5],
        ['2020-05-31', 84.2, 85.7, 86.6, 83.4],
        ['2020-06-07', 85.6, 86.9, 87.2, 84.9],
        ['2020-06-14', 86.3, 87.3, 87.9, 85.2],
        ['2020-06-21', 87.5, 86.9, 88.2, 86.2],
        ['2020-06-28', 87.7, 88.4, 89.1, 87.2]]

df = pd.DataFrame(data, columns=['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={'Opening Price ($)':'Open', 'Closing Price ($)':'Close', 'High Price ($)':'High', 'Low Price ($)':'Low'}, inplace=True)

mpf.plot(df, figratio=(12,6), title='Stock Performance of Social Media and the Web Companies - Weekly Overview', 
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/11_202312252310.png'))