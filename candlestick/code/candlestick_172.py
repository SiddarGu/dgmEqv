import plotly.graph_objects as go

data = [
    ['2019-05-01', 71, 75, 78, 70],
    ['2019-05-02', 75, 73, 80, 72],
    ['2019-05-03', 73, 77, 81, 70],
    ['2019-05-04', 76, 78, 82, 75],
    ['2019-05-05', 78, 82, 84, 76],
    ['2019-05-06', 80, 83, 86, 79],
    ['2019-05-07', 81, 84, 87, 80],
    ['2019-05-08', 82, 86, 88, 81],
    ['2019-05-09', 85, 88, 90, 83],
    ['2019-05-10', 87, 89, 92, 85],
    ['2019-05-11', 88, 90, 94, 86]
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
    title='Energy and Utilities Sector Stock Performance - May 2019',
    width=800,
    height=600,
    yaxis_range=[min(lows)-1, max(highs)+1]
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/143_202312302255.png')