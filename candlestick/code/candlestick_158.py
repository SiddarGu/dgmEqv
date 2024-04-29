import plotly.graph_objects as go
import pandas as pd

data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10'],
        'Open Price ($)': [130, 137, 134, 133, 133, 138, 144, 150],
        'Close Price ($)': [135, 136, 132, 134, 137, 140, 147, 154],
        'High Price ($)': [137, 143, 138, 140, 141, 145, 152, 160],
        'Low Price ($)': [128, 134, 131, 130, 130, 136, 143, 148]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Close Price ($)'])])

fig.update_layout(
    title='Stock Trends for Major Legal Firms in the First Quarter of 2020',
    width=800,
    height=600,
    xaxis=dict(
        tickangle=45,
        title='Date',
        titlefont=dict(size=12),
        tickfont=dict(size=10)),
    yaxis=dict(
        title='Price ($)',
        titlefont=dict(size=12),
        tickfont=dict(size=10)),
    yaxis_range=[120, 170],
    showlegend=False)

fig.update_layout(autosize=False, margin=dict(l=20, r=20, t=30, b=20))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/125_202312302255.png')