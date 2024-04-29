import plotly.graph_objects as go

# Data
date = ['2022-03-01', '2022-03-08', '2022-03-15', '2022-03-22', '2022-03-29',
        '2022-04-05', '2022-04-12', '2022-04-19', '2022-04-26']
open_price = [70.2, 75.5, 76.3, 78.1, 77, 80, 82.5, 85, 88]
close_price = [75, 76, 78, 79, 80, 82.2, 85, 88, 91]
high_price = [77, 78.9, 80, 81, 82, 84, 87, 90, 93]
low_price = [68, 73, 74, 76, 75.5, 78, 80, 83, 86.5]

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=date,
    open=open_price,
    close=close_price,
    high=high_price,
    low=low_price
)])

# Set title
fig.update_layout(
    title="Monthly Price Trend in Energy and Utilities Sector"
)

# Set size parameters
fig.update_layout(
    autosize=False,
    width=800,
    height=600,
    margin=dict(t=50, b=50, l=50, r=50),
)

# Adjust y-axis range
min_price = min(low_price)
max_price = max(high_price)
y_axis_range = [min_price - 2, max_price + 2]
fig.update_layout(
    yaxis_range=y_axis_range
)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/55_202312302255.png')