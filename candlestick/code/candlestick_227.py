import plotly.graph_objects as go

# Define the data
data = [
    ['2022-06-01', 105.5, 102, 108.2, 100.8],
    ['2022-06-02', 102, 104.1, 105.2, 100.9],
    ['2022-06-03', 104, 103, 105, 101],
    ['2022-06-04', 103, 108.7, 110.6, 102],
    ['2022-06-05', 108, 111.9, 112.2, 105],
    ['2022-06-06', 111, 112.8, 114.1, 108],
    ['2022-06-07', 112, 113, 114, 108.5],
    ['2022-06-08', 113, 120, 121, 112],
    ['2022-06-09', 120, 121, 122, 118],
    ['2022-06-10', 121, 125, 128, 120],
    ['2022-06-11', 125, 130, 132, 125],
    ['2022-06-12', 130, 134, 135, 129],
    ['2022-06-13', 134, 136, 138, 130],
    ['2022-06-14', 136, 138, 139, 135],
    ['2022-06-15', 138, 139, 140, 137]
]

# Extract the dates
dates = [row[0] for row in data]

# Extract the stock prices
open_prices = [row[1] for row in data]
close_prices = [row[2] for row in data]
high_prices = [row[3] for row in data]
low_prices = [row[4] for row in data]

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=open_prices,
                                     close=close_prices,
                                     high=high_prices,
                                     low=low_prices)])

# Set the title
fig.update_layout(title="Daily Energy and Utilities Stocks Price Trend in June 2022",
                  width=800,
                  height=600,
                  xaxis=dict(rangeslider=dict(visible=False)),
                  yaxis_range=[min(low_prices)-2, max(high_prices)+2])

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/142_202312302255.png')