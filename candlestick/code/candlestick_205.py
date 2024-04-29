import plotly.graph_objects as go

# Data
data = [
    ['2021-01-01', 15000, 18000, 20000, 14000],
    ['2021-02-01', 17000, 20000, 23000, 16500],
    ['2021-03-01', 19000, 21000, 25000, 18500],
    ['2021-04-01', 20000, 23000, 25000, 19000],
    ['2021-05-01', 22000, 24000, 26000, 20000],
    ['2021-06-01', 23000, 27000, 28000, 22000],
    ['2021-07-01', 25000, 28000, 30000, 24000],
    ['2021-08-01', 27000, 29000, 32000, 26000],
    ['2021-09-01', 28000, 31000, 33500, 27000],
    ['2021-10-01', 29000, 32500, 35000, 28000],
    ['2021-11-01', 30000, 33000, 36000, 29000],
    ['2021-12-01', 32000, 35000, 37000, 31000]
]

# Extract data
dates = [row[0] for row in data]
opening_donation = [row[1] for row in data]
closing_donation = [row[2] for row in data]
high_donation = [row[3] for row in data]
low_donation = [row[4] for row in data]

# Create figure
fig = go.Figure(data=[go.Candlestick(
    x=dates,
    open=opening_donation,
    close=closing_donation,
    high=high_donation,
    low=low_donation
)])

# Update layout
fig.update_layout(
    title="Monthly Donation Trend in Charity and Nonprofit Organizations in 2021",
    width=800,
    height=600,
    showlegend=False,
    yaxis_range=[12000, 38000],
    font=dict(size=10),
    margin=dict(l=20, r=20, t=50, b=50)
)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/50_202312302255.png')
