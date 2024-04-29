import plotly.graph_objects as go

data = [['2020-01-01', 10000, 10500, 10800, 9800],
        ['2020-02-01', 10600, 11200, 12500, 10500],
        ['2020-03-01', 11300, 11500, 12000, 10900],
        ['2020-04-01', 11800, 13000, 14000, 11800],
        ['2020-05-01', 13100, 13500, 14400, 13000],
        ['2020-06-01', 13600, 14000, 15000, 13500]]

dates = [row[0] for row in data]
opens = [row[1] for row in data]
closes = [row[2] for row in data]
highs = [row[3] for row in data]
lows = [row[4] for row in data]

fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=opens,
                                     high=highs,
                                     low=lows,
                                     close=closes)])

fig.update_layout(title='Monthly Donation Trend in a Nonprofit Organization',
                  width=800, height=600,
                  showlegend=False,
                  xaxis=dict(title='Date'),
                  yaxis=dict(title='Donation ($)',
                             range=[min(lows) * 0.9, max(highs) * 1.1]))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/165_202312302255.png')