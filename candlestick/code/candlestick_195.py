
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame({
    'Month': ['2020-05', '2020-06', '2020-07', '2020-08', '2020-09'],
    'Opening Price ($)': [250, 280, 290, 280, 270],
    'Closing Price ($)': [266, 272, 300, 280, 280],
    'High Price ($)': [270, 290, 310, 290, 295],
    'Low Price ($)': [240, 260, 270, 265, 255]
})

fig = go.Figure(data=[go.Candlestick(
    x=df['Month'],
    open=df['Opening Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)'],
    close=df['Closing Price ($)']
)])

fig.update_layout(
    title='Arts and Culture Industry Stock Performance - Monthly Overview',
    xaxis_title='Month',
    yaxis_title='Price ($)',
    yaxis_range=[230, 320],
    width=800,
    height=600,
    font=dict(size=16)
)

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/6_202312251608.png")