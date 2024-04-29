import plotly.graph_objects as go

data = [
    ['2020-03-01', 100, 105, 110, 95],
    ['2020-03-02', 105, 102, 110, 100],
    ['2020-03-03', 102, 108, 110, 98],
    ['2020-03-04', 108, 112, 113, 105],
    ['2020-03-05', 112, 115, 118, 110],
    ['2020-03-06', 115, 120, 125, 112],
    ['2020-03-07', 120, 118, 125, 115],
    ['2020-03-08', 118, 121, 125, 115],
    ['2020-03-09', 121, 125, 130, 120],
    ['2020-03-10', 125, 127, 130, 125]
]

dates = [row[0] for row in data]
opens = [row[1] for row in data]
closes = [row[2] for row in data]
highs = [row[3] for row in data]
lows = [row[4] for row in data]

fig = go.Figure(data=[go.Candlestick(x=dates, open=opens, close=closes, high=highs, low=lows)])

fig.update_layout(
    title='Agriculture and Food Production Stock Performance - March 2020',
    width=800,
    height=500,
    margin=dict(l=50, r=50, b=50, t=80),
    font=dict(size=12),
    yaxis_range=[min(lows) - 5, max(highs) + 5]
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/203_202312302255.png')