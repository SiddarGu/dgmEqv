import plotly.graph_objects as go

data = [['2019-04-26', 48.6, 50.2, 52.8, 47.6],
        ['2019-04-27', 50.2, 51.8, 53.9, 49.5],
        ['2019-04-28', 51.8, 53.3, 54.7, 50.5],
        ['2019-04-29', 53.3, 54.0, 55.7, 52.3],
        ['2019-04-30', 54.0, 55.2, 57.0, 53.1],
        ['2019-05-01', 55.2, 57.8, 59.7, 54.8],
        ['2019-05-02', 57.8, 58.3, 60.2, 56.5],
        ['2019-05-03', 58.3, 59.7, 61.4, 57.2],
        ['2019-05-04', 59.7, 61.2, 62.7, 58.6],
        ['2019-05-05', 61.2, 63.8, 65.5, 60.4]]

dates = [row[0] for row in data]
open_prices = [row[1] for row in data]
close_prices = [row[2] for row in data]
high_prices = [row[3] for row in data]
low_prices = [row[4] for row in data]

fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=open_prices,
                                     close=close_prices,
                                     high=high_prices,
                                     low=low_prices)])

fig.update_layout(title='Tourism and Hospitality Industry Stock Trend in Ten Days',
                  width=800,
                  height=600)

fig.update_layout(xaxis_rangeslider_visible=False)
fig.update_layout(xaxis_title='Date')
fig.update_layout(yaxis_title='Price')

fig.update_layout(margin=dict(l=50, r=50, t=80, b=80))
fig.update_layout(font=dict(size=9))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/188_202312302255.png')