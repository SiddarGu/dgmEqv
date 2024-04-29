import plotly.graph_objects as go

# Define the data
data = [
    ['2021-01-10', 1200, 1220, 1240, 1180],
    ['2021-01-17', 1230, 1210, 1240, 1210],
    ['2021-01-24', 1220, 1240, 1250, 1210],
    ['2021-01-31', 1250, 1240, 1270, 1230],
    ['2021-02-07', 1240, 1260, 1270, 1230],
    ['2021-02-14', 1260, 1270, 1290, 1250],
    ['2021-02-21', 1270, 1280, 1300, 1260],
    ['2021-02-28', 1280, 1290, 1310, 1270],
    ['2021-03-07', 1290, 1300, 1320, 1280],
    ['2021-03-14', 1300, 1320, 1330, 1290],
    ['2021-03-21', 1320, 1330, 1340, 1300],
    ['2021-03-28', 1330, 1340, 1350, 1310]
]

# Extract the data columns
dates = [row[0] for row in data]
opens = [row[1] for row in data]
closes = [row[2] for row in data]
highs = [row[3] for row in data]
lows = [row[4] for row in data]

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=dates,
                    open=opens, high=highs,
                    low=lows, close=closes)])

# Set the layout parameters
fig.update_layout(
    title="Weekly Donation Trends in a Charity Organization",
    width=800,
    height=600,
    xaxis=dict(
        title="Date"
    ),
    yaxis=dict(
        title="Donation ($)",
        range=[min(lows) - 50, max(highs) + 50]
    ),
    showlegend=False
)

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/124_202312302255.png')