
import plotly.graph_objects as go
import pandas as pd

data = [['2019-05-01',45.9,50.5,51.2,43.6],
        ['2019-05-02',49.2,50.9,51.5,48.6],
        ['2019-05-03',48.9,50.3,51.8,47.5],
        ['2019-05-04',50,50.9,53.2,49.8],
        ['2019-05-05',50.2,52.1,53.2,49.9],
        ['2019-05-06',51.2,53.9,54.2,50.2],
        ['2019-05-07',52.4,54.8,55.9,51.8]]

df = pd.DataFrame(data, columns = ['Date','Open','Close','High','Low'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.update_layout(title='Price Trend of Retail and E-commerce Stocks - Weekly Overview',
                  xaxis_title='Date',
                  yaxis_title='Price ($)',
                  width=800,
                  height=500)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/2_202312251608.png')