import plotly.graph_objects as go


data = [
    ['2021-01-04', 75, 76.4, 78, 73.6],
    ['2021-01-11', 78, 76.5, 81.2, 74.9],
    ['2021-01-18', 79, 80.6, 81, 78],
    ['2021-01-25', 82.5, 84, 85.6, 80.4],
    ['2021-02-01', 85, 83, 86.5, 82.7],
    ['2021-02-08', 83, 84, 85, 80],
    ['2021-02-15', 81.5, 83.1, 84.7, 79.8],
    ['2021-02-22', 82, 79.8, 83.6, 77.5]
]

fig = go.Figure(data=[go.Candlestick(
    x=[row[0] for row in data],
    open=[row[1] for row in data],
    close=[row[2] for row in data],
    high=[row[3] for row in data],
    low=[row[4] for row in data]
)])

fig.update_layout(
    title='Public Policy Impact on Weekly Government Bond Yield',
    width=800,
    height=600,
    yaxis_range=[70, 90]
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/84_202312302255.png')