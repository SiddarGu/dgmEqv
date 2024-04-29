
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

df = pd.DataFrame([['2019-07-26', 10, 11.2, 12.5, 9.3], ['2019-07-27', 10.5, 11.8, 13.2, 9.9], ['2019-07-28', 11, 11.4, 12.3, 10.5], ['2019-07-29', 12, 13, 14, 11.2], ['2019-07-30', 12.8, 13.2, 14.6, 11.8], ['2019-07-31', 12.5, 13.8, 14.7, 11.6]], columns=['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Opening Price ($)'], high=df['High Price ($)'], low=df['Low Price ($)'], close=df['Closing Price ($)'])])
fig.update_layout(title='Sports and Entertainment Industry Financing Trend Overview', xaxis_title='Date', yaxis_title='Price ($)', width=1800, height=1000, yaxis_range=[9.3, 14.7], font=dict(family='Courier New, monospace', size=22))
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/2_202312270043.png')