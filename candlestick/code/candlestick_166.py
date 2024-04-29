import plotly.graph_objects as go

data = [
    ['2021-01-05', 320, 340, 345, 310],
    ['2021-01-06', 345, 350, 355, 345],
    ['2021-01-07', 350, 355, 360, 340],
    ['2021-01-08', 355, 350, 360, 330],
    ['2021-01-09', 340, 335, 340, 320],
    ['2021-01-10', 330, 340, 345, 330],
    ['2021-01-11', 335, 350, 360, 335],
    ['2021-01-12', 350, 345, 350, 340],
    ['2021-01-13', 345, 340, 345, 330],
    ['2021-01-14', 335, 330, 335, 325]
]

dates = [row[0] for row in data]
opens = [row[1] for row in data]
closes = [row[2] for row in data]
highs = [row[3] for row in data]
lows = [row[4] for row in data]

fig = go.Figure(data=[go.Candlestick(x=dates, open=opens, close=closes, high=highs, low=lows)])

fig.update_layout(
    title="Stock Prices of a Major Tech Company in January 2021",
    width=800,
    height=600,
    xaxis=dict(
        title="Date"
    ),
    yaxis=dict(
        title="Price ($)",
        range=[min(lows) - 10, max(highs) + 10],
    )
)

fig.update_layout(
    font=dict(
        family="sans-serif",
        size=10,
    )
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/215_202312302255.png')
