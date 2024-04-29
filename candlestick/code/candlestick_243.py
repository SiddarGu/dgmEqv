import plotly.graph_objects as go
import pandas as pd

data = {
    'Date': ['2020-05-04', '2020-05-05', '2020-05-06', '2020-05-07', '2020-05-08', '2020-05-09', '2020-05-10', '2020-05-11'],
    'Open Price ($)': [103.2, 102.4, 101.5, 105.2, 104.3, 105.2, 105.1, 103.9],
    'Close Price ($)': [104.1, 101.5, 105.8, 106.4, 103.1, 104.1, 107.6, 102.3],
    'High Price ($)': [106.5, 103.8, 106.2, 107.7, 105.6, 106.8, 108.3, 105.3],
    'Low Price ($)': [101.1, 100.2, 101.2, 104.5, 101.8, 104.1, 104.8, 100.6]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Close Price ($)'])])

fig.update_layout(
    width=1200,
    height=800,
    title='Government Bonds Market Trend Analysis',
    xaxis_rangeslider_visible=False,
    yaxis_range=[min(df['Low Price ($)']) - 2, max(df['High Price ($)']) + 2],
    showlegend=False
)

fig.update_xaxes(
    tickangle=45,
    tickfont=dict(size=8)
)

fig.update_yaxes(
    tickfont=dict(size=8)
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/185_202312302255.png')
