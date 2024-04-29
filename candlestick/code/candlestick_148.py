import plotly.graph_objects as go

data = [['2020-01-02', 120, 130, 150, 115],
        ['2020-01-09', 130, 135, 155, 120],
        ['2020-01-16', 140, 145, 155, 105],
        ['2020-01-23', 150, 155, 165, 140],
        ['2020-01-30', 145, 150, 165, 120],
        ['2020-02-06', 148, 152, 165, 120],
        ['2020-02-13', 155, 160, 170, 130],
        ['2020-02-20', 158, 165, 170, 135],
        ['2020-02-27', 170, 175, 180, 150],
        ['2020-03-05', 160, 165, 185, 150]]

dates = [row[0] for row in data]
opening_prices = [row[1] for row in data]
closing_prices = [row[2] for row in data]
high_prices = [row[3] for row in data]
low_prices = [row[4] for row in data]

fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=opening_prices,
                                     close=closing_prices,
                                     high=high_prices,
                                     low=low_prices)])

fig.update_layout(title='Sport and Entertainment Industry Stock Trends',
                  width=800,
                  height=600,
                  yaxis_range=[min(low_prices)-10, max(high_prices)+10],
                  margin=dict(t=100, l=20, r=20, b=20))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/96_202312302255.png')