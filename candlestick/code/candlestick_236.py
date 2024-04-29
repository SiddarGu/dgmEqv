import plotly.graph_objects as go

data = [
    ['2020-11-10', 70, 75, 77, 68],
    ['2020-11-17', 75.5, 77, 78.5, 72],
    ['2020-11-24', 78, 80, 82, 76],
    ['2020-12-01', 80.5, 82.5, 85, 79],
    ['2020-12-08', 82, 84, 86, 80]
]

dates = [row[0] for row in data]
open_prices = [row[1] for row in data]
close_prices = [row[2] for row in data]
high_prices = [row[3] for row in data]
low_prices = [row[4] for row in data]

fig = go.Figure(data=[go.Candlestick(x=dates,
                open=open_prices, high=high_prices,
                low=low_prices, close=close_prices)])

fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Price ($)")
fig.update_layout(title="Humanities Publication Royalties - November and December 2020",
                  width=800,
                  height=600,
                  yaxis_range=[min(low_prices)-1, max(high_prices)+1])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/93_202312302255.png')