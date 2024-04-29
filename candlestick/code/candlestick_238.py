import plotly.graph_objects as go

data = [['2022-01-01', 68.4, 68.6, 69.1, 67.8],
        ['2022-01-02', 68.6, 69, 70, 68.2],
        ['2022-01-03', 70, 71, 72, 69.6],
        ['2022-01-04', 70.5, 72.6, 73.1, 70.4],
        ['2022-01-05', 71, 73, 74, 70.6],
        ['2022-01-06', 72, 74.1, 74.6, 71.9],
        ['2022-01-07', 73.1, 75.2, 75.7, 73.0],
        ['2022-01-08', 73.9, 76, 76.5, 73.7],
        ['2022-01-09', 76, 75.7, 76.9, 74.5]]

dates = [row[0] for row in data]
opens = [row[1] for row in data]
closes = [row[2] for row in data]
highs = [row[3] for row in data]
lows = [row[4] for row in data]

fig = go.Figure(data=[go.Candlestick(x=dates, open=opens, close=closes, high=highs, low=lows)])

fig.update_layout(
    title="Global Hospitality Market - Daily Open, Close, High, and Low Prices",
    height=500,
    width=800,
    margin=dict(t=50, b=50, l=50, r=50),
    yaxis=dict(range=[min(lows)-1, max(highs)+1])
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/119_202312302255.png')