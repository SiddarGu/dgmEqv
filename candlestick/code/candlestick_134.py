import plotly.graph_objects as go

# Data
data = [
    ['2021-07-01', 220, 240, 250, 215],
    ['2021-08-01', 240, 260, 270, 235],
    ['2021-09-01', 260, 280, 285, 255],
    ['2021-10-01', 275, 290, 300, 270],
    ['2021-11-01', 285, 295, 310, 280],
    ['2021-12-01', 300, 320, 330, 295],
    ['2022-01-01', 305, 325, 340, 300],
    ['2022-02-01', 315, 335, 345, 310],
    ['2022-03-01', 325, 345, 355, 320],
    ['2022-04-01', 335, 355, 365, 330],
    ['2022-05-01', 345, 365, 375, 340],
    ['2022-06-01', 355, 375, 385, 350]
]

# Extracting data
dates = [x[0] for x in data]
open_prices = [x[1] for x in data]
close_prices = [x[2] for x in data]
high_prices = [x[3] for x in data]
low_prices = [x[4] for x in data]

# Candlestick chart
fig = go.Figure(data=[go.Candlestick(x=dates,
                                    open=open_prices,
                                    close=close_prices,
                                    high=high_prices,
                                    low=low_prices)])

# Chart layout
fig.update_layout(
    title='Monthly Housing Market Price Trends',
    width=800,
    height=600,
    yaxis_range=[min(low_prices)-10, max(high_prices)+10],
    font=dict(family='Arial'),
    margin=dict(l=50, r=50, t=80, b=80),
    showlegend=False,
    xaxis=dict(title='Date'),
    yaxis=dict(title='Price ($)'),
)

# Save image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/221_202312302255.png')