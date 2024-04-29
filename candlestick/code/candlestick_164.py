import plotly.graph_objects as go

data = [
    ['2021-12-01', 34, 35.8, 36.1, 32],
    ['2021-12-08', 37, 38, 39, 34],
    ['2021-12-15', 38.6, 39, 40, 35],
    ['2021-12-22', 40, 43, 45, 39],
    ['2021-12-29', 42.2, 44.1, 46.2, 41.6],
    ['2022-01-05', 40.6, 42.7, 44.2, 38.0],
    ['2022-01-12', 39, 41, 43.9, 36.5],
    ['2022-01-19', 36, 40, 42.2, 34]
]

dates = [row[0] for row in data]
opens = [row[1] for row in data]
closes = [row[2] for row in data]
highs = [row[3] for row in data]
lows = [row[4] for row in data]

fig = go.Figure(data=[go.Candlestick(x=dates,
                                    open=opens,
                                    close=closes,
                                    high=highs,
                                    low=lows)])
fig.update_layout(
    title="Weekly Price Trend of Engineering Tech stocks",
    xaxis_showticklabels=False,
    yaxis_showticklabels=False,
    width=1000,
    height=800,
    margin=dict(l=50, r=50, t=50, b=50),
    yaxis_range=[min(lows) - 1, max(highs) + 1],
)
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/116_202312302255.png')
