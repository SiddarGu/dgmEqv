
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# Create DataFrame
df = pd.DataFrame([['2019-04-23',24.5,26.5,27.8,22.7],['2019-04-30',26.6,26.8,28.5,25.2],['2019-05-07',26.5,27,28.2,25.4],['2019-05-14',27.5,27.3,29.2,25.8],['2019-05-21',27.2,27.5,29.4,26.3],['2019-05-28',27.4,26.2,28.7,25.7],['2019-06-04',26.3,27,27.6,24.8]],columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])

# Convert 'Date' to datetime and set as index
df['Date']=pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)

# Rename columns to match mplfinance column requirements
df.rename(columns={'Opening Price ($)':'Open','Closing Price ($)':'Close','High Price ($)':'High','Low Price ($)':'Low'},inplace=True)

# Create candlestick chart with mplfinance
mpf.plot(df,type='candle', figratio=(12,6),title='Transportation & Logistics Company Stock Performance - 7-week Overview',savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/21_202312252310.png'))