import plotly.graph_objects as go
import pandas as pd

data = {
    'Date': ['2021-05-01', '2021-05-08', '2021-05-15', '2021-05-22', '2021-05-29', '2021-06-05', '2021-06-12', '2021-06-19', '2021-06-26', '2021-07-03'],
    'Open Price ($)': [120, 130, 145, 140, 150, 148, 155.5, 166, 172, 180],
    'Close Price ($)': [123.2, 135, 138, 145.3, 155.7, 153.5, 165, 171.2, 175.6, 186],
    'High Price ($)': [125.3, 139.9, 146, 150, 160.2, 160, 170, 175, 182, 190.5],
    'Low Price ($)': [117, 127, 130, 136, 146, 142.5, 152, 162, 168, 176]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)'],
    close=df['Close Price ($)']
)])

fig.update_layout(
    title='Share Price Trends in Science and Engineering Field',
    width=1000,
    height=600,
    yaxis_range=[100, 200]
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/170_202312302255.png')