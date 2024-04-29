

import plotly.graph_objects as go
import pandas as pd

data = [
    ['2020-12-01', 20.2, 21.7, 25.8, 18.6],
    ['2020-12-02', 21.9, 20.2, 22.8, 18.3],
    ['2020-12-03', 21.1, 22.7, 23.6, 20.4],
    ['2020-12-04', 23.2, 20.9, 23.4, 19.8],
    ['2020-12-05', 21.2, 21.9, 22.8, 20.3],
    ['2020-12-06', 20.6, 22.7, 23.8, 20.2],
    ['2020-12-07', 22.4, 21.0, 23.2, 20.5]
]

df = pd.DataFrame(data, columns=['Date', 'Open Price ($)', 'Close Price ($)', 'High Price ($)', 'Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Open Price ($)'], close=df['Close Price ($)'], high=df['High Price ($)'], low=df['Low Price ($)'], increasing_line_color='green', decreasing_line_color='red')])

fig.update_layout(title='Weekly Price Range of Agriculture and Food Production Commodity', xaxis_title='Date', yaxis_title='Price ($)', xaxis_rangeslider_visible=True, yaxis_range=[min(df['Low Price ($)']) - 2, max(df['High Price ($)']) + 2], width=1000, height=800, font=dict(family="Arial"))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/43_202312252244.png')