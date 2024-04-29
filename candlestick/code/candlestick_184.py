import plotly.graph_objects as go
import pandas as pd

data = {
    "Date": ['2020-05-22', '2020-05-29', '2020-06-05', '2020-06-12', '2020-06-29', '2020-07-06', '2020-07-13'],
    "Open Price ($)": [114.5, 125, 121, 130, 138, 145, 153],
    "Close Price ($)": [122.3, 117.9, 127, 136.8, 143.9, 152, 158.7],
    "High Price ($)": [124.1, 129, 132.5, 140, 146, 155.5, 160],
    "Low Price ($)": [112.8, 115, 118, 128.8, 135, 142.3, 150]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open Price ($)'],
    close=df['Close Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)']
)])

fig.update_layout(
    title="Seven Week Financial Service Sector Stock Trend",
    xaxis_title="Date",
    yaxis_title="Price ($)",
    width=800,
    height=600,
    yaxis_range=[100, 170],
    showlegend=False
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/219_202312302255.png')