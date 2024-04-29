import plotly.graph_objects as go

# Data
data = [
    ['2021-02-01', 100, 105, 110, 95],
    ['2021-02-02', 105, 110, 115, 100],
    ['2021-02-03', 110, 107, 114, 102],
    ['2021-02-04', 108, 107, 112, 104],
    ['2021-02-05', 107, 108, 110, 105],
    ['2021-02-06', 108, 110, 115, 107],
    ['2021-02-07', 110, 112, 118, 109],
    ['2021-02-08', 112, 115, 120, 110],
    ['2021-02-09', 115, 117, 122, 113],
    ['2021-02-10', 117, 119, 125, 116]
]

# Extracting data
dates = [row[0] for row in data]
opening_prices = [row[1] for row in data]
closing_prices = [row[2] for row in data]
high_prices = [row[3] for row in data]
low_prices = [row[4] for row in data]

# Creating candlestick chart
fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=opening_prices,
                                     high=high_prices,
                                     low=low_prices,
                                     close=closing_prices)])

# Setting layout parameters
fig.update_layout(width=800, height=600, title="February E-commerce Stock Performance Overview", showlegend=False)
fig.update_yaxes(range=[min(low_prices)-5, max(high_prices)+5])

# Save figure as image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/207_202312302255.png')