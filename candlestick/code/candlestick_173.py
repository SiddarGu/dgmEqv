import plotly.graph_objs as go

data = [
    ['2022-01-01', 72, 75.8, 78, 69.5],
    ['2022-01-08', 76, 77, 80, 75],
    ['2022-01-15', 79, 80, 82, 77],
    ['2022-01-22', 82.5, 85, 87, 82],
    ['2022-01-29', 88, 90, 92, 85],
    ['2022-02-05', 90, 92, 95, 89],
    ['2022-02-12', 95, 97, 99, 94],
    ['2022-02-19', 99, 101, 103, 97],
    ['2022-02-26', 100, 102, 104, 99]
]

# Extract data for easier manipulation
dates = [d[0] for d in data]
open_prices = [d[1] for d in data]
close_prices = [d[2] for d in data]
high_prices = [d[3] for d in data]
low_prices = [d[4] for d in data]

# Create candlestick chart
fig = go.Figure(data=go.Candlestick(
    x=dates,
    open=open_prices,
    close=close_prices,
    high=high_prices,
    low=low_prices
))

# Set title
fig.update_layout(title="Trends in the Energy and Utilities Sector Stock Prices")

# Set size parameters
fig.update_layout(
    autosize=False,
    width=1200,
    height=800,
    margin=dict(l=0, r=0, t=100, b=0)
)

# Adjust yaxis range
fig.update_layout(yaxis_range=[min(low_prices) - 5, max(high_prices) + 5])

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/208_202312302255.png')