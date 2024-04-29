import plotly.graph_objs as go

data = [['2022-01-03', 120, 123.5, 125, 118],
        ['2022-01-10', 124, 127.6, 130, 122],
        ['2022-01-17', 126, 128, 129, 124],
        ['2022-01-24', 130, 131.8, 133, 126.5],
        ['2022-01-31', 134, 135, 137, 131],
        ['2022-02-07', 133, 131.5, 134.5, 130],
        ['2022-02-14', 132, 129, 133, 127],
        ['2022-02-21', 130, 131.4, 133, 128],
        ['2022-02-28', 132, 134, 136, 129],
        ['2022-03-07', 133, 135.5, 137.5, 131.5],
        ['2022-03-14', 136, 137, 139, 134],
        ['2022-03-21', 138, 140, 142, 136],
        ['2022-03-28', 141, 143, 145, 139],
        ['2022-04-04', 144, 146, 148, 142],
        ['2022-04-11', 147, 148.5, 150, 144.5],
        ['2022-04-18', 149, 151, 153, 146],
        ['2022-04-25', 151, 153.3, 155, 148]]

dates = [d[0] for d in data]
opening_prices = [d[1] for d in data]
closing_prices = [d[2] for d in data]
high_prices = [d[3] for d in data]
low_prices = [d[4] for d in data]

fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=opening_prices,
                                     close=closing_prices,
                                     high=high_prices,
                                     low=low_prices)])

fig.update_layout(title='Fluctuations in Value of Legal Services Firm Stocks over Time',
                  width=800,
                  height=600,
                  autosize=False,
                  margin=dict(l=40, r=40, t=40, b=40),
                  yaxis=dict(range=[min(low_prices)-5, max(high_prices)+5]),
                  showlegend=False)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/178_202312302255.png')