import plotly.graph_objects as go

# Data
data = [['2021-05-03', 80, 83, 85, 75],
        ['2021-05-10', 83, 88, 91, 80],
        ['2021-05-17', 90, 93, 95, 85],
        ['2021-05-24', 94, 96, 98, 90],
        ['2021-05-31', 96, 98, 101, 94],
        ['2021-06-07', 99, 101, 103, 97],
        ['2021-06-14', 102, 105, 107, 100],
        ['2021-06-21', 107, 108, 110, 105],
        ['2021-06-28', 109, 110, 113, 107],
        ['2021-07-05', 111, 114, 116, 109]]

# Extracting data
dates = [row[0] for row in data]
open_prices = [row[1] for row in data]
close_prices = [row[2] for row in data]
high_prices = [row[3] for row in data]
low_prices = [row[4] for row in data]

# Creating candlestick chart
fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=open_prices,
                                     close=close_prices,
                                     high=high_prices,
                                     low=low_prices)])

# Updating layout
fig.update_layout(
    title='HR Management Company Share Prices Trends',
    width=800,
    height=600,
    showlegend=False,
    xaxis=dict(
        title='Date',
        tickangle=45,
        tickfont=dict(size=8),
    ),
    yaxis=dict(
        title='Price ($)',
        range=[min(low_prices) - 5, max(high_prices) + 5],
    ),
    margin=dict(l=50, r=50, t=50, b=50),
)

# Saving the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/168_202312302255.png')