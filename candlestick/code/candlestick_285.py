import plotly.graph_objects as go

data = [['2020-01-01', 320000, 325000, 330000, 315000],
        ['2020-02-01', 325000, 327000, 332000, 320000],
        ['2020-03-01', 327000, 330000, 335000, 325000],
        ['2020-04-01', 330000, 333000, 338000, 328000],
        ['2020-05-01', 333000, 335000, 340000, 330000]]

dates = [row[0] for row in data]
open_prices = [row[1] for row in data]
close_prices = [row[2] for row in data]
high_prices = [row[3] for row in data]
low_prices = [row[4] for row in data]

fig = go.Figure(data=[go.Candlestick(
    x=dates,
    open=open_prices,
    close=close_prices,
    high=high_prices,
    low=low_prices
)])

fig.update_layout(
    title='Monthly Real Estate Market Price Trend',
    autosize=False,
    width=800,
    height=600,
    yaxis_range=[min(low_prices) - 5000, max(high_prices) + 5000]
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/179_202312302255.png')