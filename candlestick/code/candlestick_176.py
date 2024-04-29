import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame({
    'Date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10'],
    'Open Price ($)': [15, 17, 16, 19, 20, 22, 21, 23, 24, 26],
    'Close Price ($)': [17, 16, 18, 21, 22, 20, 23, 24, 26, 28],
    'High Price ($)': [20, 18, 19, 23, 24, 23, 25, 26, 28, 30],
    'Low Price ($)': [13, 15, 15, 16, 19, 17, 19, 20, 21, 23]
})

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)'],
    close=df['Close Price ($)']
)])

fig.update_layout(
    title='Trend Analysis of Green Technology Stocks',
    xaxis_title='Date',
    yaxis_title='Price',
    width=1200,
    height=800,
    yaxis_range=[min(df['Low Price ($)']) - 2, max(df['High Price ($)']) + 2],
    autosize=False,
    showlegend=False
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/225_202312302255.png')