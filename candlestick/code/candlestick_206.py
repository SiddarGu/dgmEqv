import plotly.graph_objects as go
import pandas as pd

data = {'Date': ['2020-01-06', '2020-01-13', '2020-01-20', '2020-01-27', '2020-02-03', '2020-02-10', '2020-02-17', '2020-02-24', '2020-03-02', '2020-03-09', '2020-03-16', '2020-03-23', '2020-03-30', '2020-04-06', '2020-04-13'], 'Open Price ($)': [120, 130, 125, 130, 135, 140, 145, 140, 145, 150, 155, 160, 155, 160, 165], 'Close Price ($)': [130, 125, 130, 135, 140, 145, 140, 145, 150, 155, 160, 155, 160, 165, 160], 'High Price ($)': [135, 135, 135, 140, 145, 150, 150, 150, 155, 160, 165, 165, 165, 170, 170], 'Low Price ($)': [115, 120, 120, 125, 130, 135, 135, 135, 140, 145, 150, 150, 150, 155, 155]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Close Price ($)'])])

fig.update_layout(
    title='Sustainability Stock Price Trend in First Quarter of 2020',
    width=800,
    height=600,
    yaxis_range=[110, 175]
)

fig.update_layout(
    autosize=False,
    margin=dict(t=50, b=50, l=50, r=50)
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/169_202312302255.png')