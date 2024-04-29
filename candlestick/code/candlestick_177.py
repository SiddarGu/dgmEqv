import plotly.graph_objects as go

# Data
data = [
    ['2022-01-03', 125, 128, 130, 120],
    ['2022-01-10', 130, 135, 138, 128],
    ['2022-01-17', 138, 140, 145, 135],
    ['2022-01-24', 142, 145, 150, 139],
    ['2022-01-31', 150, 155, 160, 148],
    ['2022-02-7', 155, 160, 165, 153],
    ['2022-02-14', 162, 165, 170, 160],
    ['2022-02-21', 165, 170, 175, 162],
    ['2022-02-28', 172, 175, 180, 169],
    ['2022-03-07', 180, 185, 190, 178]
]

# Extract data
dates = [row[0] for row in data]
open_price = [row[1] for row in data]
close_price = [row[2] for row in data]
high_price = [row[3] for row in data]
low_price = [row[4] for row in data]

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=open_price,
                                     close=close_price,
                                     high=high_price,
                                     low=low_price)])

# Customize layout
fig.update_layout(title='Weekly Stock Performance of a major Hospitality Company',
                  width=800,
                  height=600,
                  yaxis_range=[min(low_price)*0.95, max(high_price)*1.05])

# Save image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/224_202312302255.png')