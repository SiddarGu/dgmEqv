import plotly.graph_objects as go

# Data
data = [
    ['2021-01-01', 120, 128, 130, 117],
    ['2021-01-02', 129, 137, 139, 126],
    ['2021-01-03', 137, 142, 148, 134],
    ['2021-01-04', 143, 148, 152, 139],
    ['2021-01-05', 150, 155, 160, 145],
    ['2021-01-06', 156, 158, 161, 153],
    ['2021-01-07', 159, 164, 170, 153],
    ['2021-01-08', 165, 177, 180, 162],
    ['2021-01-09', 180, 185, 190, 174],
    ['2021-01-10', 186, 181, 188, 180],
    ['2021-01-11', 182, 185, 190, 174],
    ['2021-01-12', 186, 190, 192, 180],
    ['2021-01-13', 191, 195, 200, 180],
    ['2021-01-14', 197, 201, 205, 190],
    ['2021-01-15', 202, 210, 212, 198],
    ['2021-01-16', 213, 208, 215, 200],
    ['2021-01-17', 210, 215, 220, 205]
]

# Extracting data
dates = [row[0] for row in data]
opening_prices = [row[1] for row in data]
closing_prices = [row[2] for row in data]
high_prices = [row[3] for row in data]
low_prices = [row[4] for row in data]

# Create Figure and Candlestick trace
fig = go.Figure(data=[go.Candlestick(
    x=dates,
    open=opening_prices,
    close=closing_prices,
    high=high_prices,
    low=low_prices
)])

# Update layout
fig.update_layout(
    title="Monthly Tech Stocks Average Price Trend Analysis",
    width=1000,
    height=600,
    xaxis_range=[min(dates), max(dates)],
    yaxis_range=[min(low_prices)-10, max(high_prices)+10],
    showlegend=False
)

# Save Figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/140_202312302255.png')