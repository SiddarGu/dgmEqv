import plotly.graph_objects as go

# Data
data = [
    ['2019-11-01', 25.1, 21.5, 27.8, 20.7],
    ['2019-11-02', 22.3, 24.5, 26.9, 20.2],
    ['2019-11-03', 24.6, 23.2, 26.3, 21.4],
    ['2019-11-04', 22.5, 24.8, 28.1, 20.6],
    ['2019-11-05', 25.0, 28.6, 29.1, 22.4],
    ['2019-11-06', 28.0, 30.5, 33.6, 26.4],
    ['2019-11-07', 31.2, 34.9, 35.1, 29.6],
    ['2019-11-08', 34.2, 33.1, 36.9, 30.1],
    ['2019-11-09', 32.5, 34.8, 35.7, 30.2],
    ['2019-11-10', 34.6, 35.4, 38.5, 31.2],
    ['2019-11-11', 35.6, 37.1, 39.0, 33.8],
    ['2019-11-12', 37.8, 40.2, 43.0, 33.6],
    ['2019-11-13', 39.5, 39.0, 42.6, 36.0],
    ['2019-11-14', 39.2, 40.6, 42.7, 35.8],
    ['2019-11-15', 40.8, 42.3, 43.9, 37.6],
    ['2019-11-16', 42.0, 43.5, 45.8, 39.8],
    ['2019-11-17', 43.9, 45.4, 48.0, 40.6],
    ['2019-11-18', 45.5, 47.9, 50.6, 41.8],
    ['2019-11-19', 48.5, 47.1, 49.9, 43.5],
    ['2019-11-20', 47.3, 49.7, 51.5, 43.9]
]

# Extracting data
dates = [row[0] for row in data]
opening_prices = [row[1] for row in data]
closing_prices = [row[2] for row in data]
high_prices = [row[3] for row in data]
low_prices = [row[4] for row in data]

# Creating candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=dates,
    open=opening_prices,
    close=closing_prices,
    high=high_prices,
    low=low_prices
)])

# Setting layout parameters
fig.update_layout(
    title="Performance of Renewable Energy Stocks in November 2019",
    width=800,
    height=600,
    template="plotly_white",
    xaxis=dict(
       autorange=True,
       showgrid=False,
       zeroline=False,
       showline=False,
       ticks='',
       showticklabels=False
    ),
    yaxis=dict(zeroline=False),
    yaxis_range=[min(low_prices)-1, max(high_prices)+1]
)

# Saving the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/197_202312302255.png')