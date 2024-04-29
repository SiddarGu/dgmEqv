import plotly.graph_objects as go

data = [
    ['2021-01-04', 120.5, 125.6, 127.1, 118.2],
    ['2021-01-11', 125, 126.7, 128.9, 124],
    ['2021-01-18', 127, 126, 128, 125],
    ['2021-01-25', 126, 125, 127, 123],
    ['2021-02-01', 125, 126, 128, 123],
    ['2021-02-08', 126, 125.5, 127, 121],
    ['2021-02-15', 125.5, 127.3, 129, 123],
    ['2021-02-22', 127, 130, 132, 124],
    ['2021-03-01', 130.5, 131.8, 133.4, 129],
]

dates = [row[0] for row in data]
opens = [row[1] for row in data]
closes = [row[2] for row in data]
highs = [row[3] for row in data]
lows = [row[4] for row in data]

fig = go.Figure(data=[go.Candlestick(x=dates, open=opens, close=closes, high=highs, low=lows)])

fig.update_layout(
    title='Market Trend of Legal Firm Stocks in Q1 2021',
    xaxis=dict(
        rangeslider=dict(
            visible=False
        )
    ),
    yaxis=dict(
        autorange=True
    ),
    width=800,
    height=600,
    margin=dict(
        l=50,
        r=50,
        b=50,
        t=80,
        pad=0
    ),
    paper_bgcolor='rgba(255,255,255,0)',
    plot_bgcolor='rgba(255,255,255,0)'
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/149_202312302255.png')
