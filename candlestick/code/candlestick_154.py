import plotly.graph_objects as go

data = [
    ['2019-03-01', 120, 122, 125, 116],
    ['2019-03-02', 122, 123, 127, 119],
    ['2019-03-03', 125, 126, 130, 121],
    ['2019-03-04', 127, 129, 133, 124],
    ['2019-03-05', 130, 133, 135, 128],
    ['2019-03-06', 134, 136, 140, 131],
    ['2019-03-07', 138, 140, 144, 133],
    ['2019-03-08', 142, 144, 147, 138],
    ['2019-03-09', 145, 147, 150, 141],
    ['2019-03-10', 148, 150, 153, 144]
]

fig = go.Figure(data=[go.Candlestick(
    x=[row[0] for row in data],
    open=[row[1] for row in data],
    high=[row[3] for row in data],
    low=[row[4] for row in data],
    close=[row[2] for row in data]
)])

fig.update_layout(
    title='Entertainment Company Stock Trend in March 2019',
    height=800,
    width=1200,
    xaxis=dict(
        type='category',
        tickangle=45
    ),
    yaxis=dict(
        autorange=True,
        title='Price ($)'
    )
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/176_202312302255.png')
