import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Create dataframe
data = {
    'Date': ['2021-01-01', '2021-01-08', '2021-01-15', '2021-01-22', '2021-01-29', '2021-02-05', '2021-02-12', '2021-02-19', '2021-02-26', '2021-03-05', '2021-03-12', '2021-03-19', '2021-03-26'],
    'Opening Price ($)': [295000, 310000, 310000, 300000, 310000, 330000, 310000, 310000, 320000, 335000, 340000, 345000, 365000],
    'Closing Price ($)': [300000, 315000, 305000, 305000, 325000, 315000, 320000, 315000, 325000, 330000, 350000, 360000, 370000],
    'High Price ($)': [320000, 330000, 315000, 310000, 330000, 340000, 325000, 320000, 330000, 355000, 360000, 370000, 385000],
    'Low Price ($)': [290000, 305000, 300000, 290000, 310000, 310000, 290000, 290000, 310000, 320000, 330000, 340000, 350000]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

# Create figure
fig = plt.figure(figsize=(12, 6))

# Create candlestick chart
mpf.plot(df, type='candle', title='Real Estate Housing Market trends: Weekly Opening and Closing Prices', figratio=(12,6), style='yahoo', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/112_202312302321.png'))