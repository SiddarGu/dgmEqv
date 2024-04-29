import plotly.graph_objects as go

# Data
data = [
    ['2023-05-01', 120, 123, 125, 118],
    ['2023-05-02', 123, 125, 130, 120],
    ['2023-05-03', 126, 128, 130, 125],
    ['2023-05-04', 128, 130, 134, 126],
    ['2023-05-05', 130, 133, 135, 128],
    ['2023-05-06', 132, 135, 139, 130],
    ['2023-05-07', 133, 136, 140, 132],
    ['2023-05-08', 135, 139, 143, 134],
    ['2023-05-09', 137, 141, 145, 136],
    ['2023-05-10', 139, 144, 148, 137]
]

# Create figure
fig = go.Figure(data=[
    go.Candlestick(
        x=[row[0] for row in data],
        open=[row[1] for row in data],
        close=[row[2] for row in data],
        high=[row[3] for row in data],
        low=[row[4] for row in data]
    )
])

# Configure figure
fig.update_layout(
    title="Biotech Stock Performance - Ten Day Overview",
    width=800,
    height=600,
    xaxis=dict(tickangle=-45, type='category'),
    yaxis=dict(fixedrange=True),
    yaxis_range=[min([row[4] for row in data]) - 5, max([row[3] for row in data]) + 5],
    margin=dict(t=50, b=50, l=50, r=50)
)

# Save figure
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/199_202312302255.png")