import plotly.graph_objects as go

data = [['2020-01-01', 123, 125, 130, 121],
        ['2020-02-01', 125, 128, 133, 122],
        ['2020-03-01', 129, 131, 135, 127],
        ['2020-04-01', 132, 135, 138, 130],
        ['2020-05-01', 136, 138, 142, 134],
        ['2020-06-01', 139, 142, 145, 137],
        ['2020-07-01', 143, 146, 149, 141],
        ['2020-08-01', 147, 150, 154, 145],
        ['2020-09-01', 151, 153, 157, 148],
        ['2020-10-01', 154, 157, 160, 152]]

dates = [x[0] for x in data]
open_prices = [x[1] for x in data]
close_prices = [x[2] for x in data]
high_prices = [x[3] for x in data]
low_prices = [x[4] for x in data]

fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=open_prices,
                                     close=close_prices,
                                     high=high_prices,
                                     low=low_prices)])

fig.update_layout(title='Cultural Industry Investment Trend in 2020',
                  xaxis=dict(title='Date'),
                  yaxis=dict(title='Price (USD)',
                             range=[min(low_prices), max(high_prices)]),
                  width=800,
                  height=600,
                  margin=dict(l=50, r=50, t=80, b=50))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/122_202312302255.png')