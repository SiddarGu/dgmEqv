import plotly.graph_objects as go
import pandas as pd

data = {
    'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01', '2020-10-01'],
    'Open Price ($/Piece)': [800, 840, 900, 930, 990, 1010, 1050, 1070, 1130, 1160],
    'Close Price ($/Piece)': [830, 880, 920, 980, 1020, 1030, 1070, 1110, 1150, 1180],
    'High Price ($/Piece)': [840, 910, 980, 1000, 1050, 1050, 1080, 1120, 1180, 1200],
    'Low Price ($/Piece)': [770, 810, 890, 910, 960, 980, 1020, 1060, 1050, 1120]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($/Piece)'],
                                     high=df['High Price ($/Piece)'],
                                     low=df['Low Price ($/Piece)'],
                                     close=df['Close Price ($/Piece)'])])

fig.update_layout(
    title='Artworks\' Price Trend in 2020',
    width=1000,
    height=500,
    xaxis=dict(
        tickfont=dict(size=8)
    ),
    yaxis=dict(
        tickfont=dict(size=8),
        range=[min(df['Low Price ($/Piece)']) - 10, max(df['High Price ($/Piece)']) + 10]
    )
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/120_202312302255.png')