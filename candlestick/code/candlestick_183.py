
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame([
    ['2019-07-20', 25, 28, 30, 21], 
    ['2019-07-27', 25, 27, 29, 22], 
    ['2019-08-03', 24, 30, 31, 23], 
    ['2019-08-10', 27, 29, 32, 26], 
    ['2019-08-17', 30, 31, 35, 28], 
    ['2019-08-24', 32, 34, 36, 30], 
    ['2019-08-31', 35, 31, 37, 29]
], columns=['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(
    x=df.Date,
    open=df['Opening Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)'],
    close=df['Closing Price ($)'])
])

fig.update_layout(
    title='Financial Trend of Arts and Culture - Weekly Overview',
    width=800,
    height=600,
    yaxis_range=[20, 40]
)

fig.write_image(r'/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/28_202312252244.png')