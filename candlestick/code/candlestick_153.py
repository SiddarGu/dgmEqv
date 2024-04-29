import plotly.graph_objects as go

# Define the data
dates = ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05']
open_prices = [101, 114, 125, 156, 165]
close_prices = [105, 120, 135, 160, 180]
high_prices = [111, 130, 145, 170, 195]
low_prices = [99, 110, 125, 150, 165]

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=dates,
                open=open_prices,
                high=high_prices,
                low=low_prices,
                close=close_prices)])

# Update the layout
fig.update_layout(title='Stock Prices Trend for a Sports and Entertainment Company',
                  width=800,
                  height=600,
                  autosize=False,
                  margin=dict(l=20, r=20, t=40, b=40),
                  yaxis_range=[min(low_prices)-10, max(high_prices)+10])

# Save the figure as PNG
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/163_202312302255.png')