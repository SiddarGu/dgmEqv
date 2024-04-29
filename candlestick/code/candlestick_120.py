import plotly.graph_objects as go

# Data
data = [
    ['2020-02-10', 250000, 255000, 260000, 245000],
    ['2020-02-17', 255000, 265000, 267000, 250000],
    ['2020-02-24', 265000, 270000, 280000, 260000],
    ['2020-03-02', 270000, 275000, 285000, 265000],
    ['2020-03-09', 275000, 280000, 290000, 270000],
    ['2020-03-16', 280000, 285000, 295000, 275000],
    ['2020-03-23', 285000, 290000, 295000, 280000],
    ['2020-03-30', 290000, 295000, 300000, 285000]
]

# Extracting values
dates = [row[0] for row in data]
opening_prices = [row[1] for row in data]
closing_prices = [row[2] for row in data]
high_prices = [row[3] for row in data]
low_prices = [row[4] for row in data]

# Creating candlestick chart
fig = go.Figure(data=go.Candlestick(
    x=dates,
    open=opening_prices,
    close=closing_prices,
    high=high_prices,
    low=low_prices,
))

# Layout
fig.update_layout(
    title='Weekly House Price Fluctuations in the Real Estate Market',
    width=800,
    height=600,
    xaxis=dict(
        title='Date',
    ),
    yaxis=dict(
        title='Price ($)',
        range=[min(low_prices) - 10000, max(high_prices) + 10000]
    ),
    autosize=False,
)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/107_202312302255.png')