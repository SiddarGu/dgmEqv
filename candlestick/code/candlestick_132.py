import plotly.graph_objects as go

data = [
    ['2021-07-05', 34.2, 35.1, 36.5, 33.8],
    ['2021-07-12', 35.6, 36.5, 37.3, 34.7],
    ['2021-07-19', 37.1, 36.2, 38, 35.7],
    ['2021-07-26', 36.5, 37.8, 38.5, 36],
    ['2021-08-02', 38.4, 39.2, 40.2, 37.8],
    ['2021-08-09', 39.9, 40.7, 41.5, 39.2],
    ['2021-08-16', 41.2, 42.3, 43, 40.8],
    ['2021-08-23', 42.8, 43.7, 44.5, 42.3],
    ['2021-08-30', 44.3, 45.2, 46, 43.8]
]

fig = go.Figure(data=[go.Candlestick(
    x=[row[0] for row in data],
    open=[row[1] for row in data],
    high=[row[3] for row in data],
    low=[row[4] for row in data],
    close=[row[2] for row in data]
)])

fig.update_layout(
    title='Stock Performance of a Bioengineering Company in Q3 2021',
    xaxis_title='Date',
    yaxis_title='Price ($)',
    width=800,
    height=600,
    yaxis_range=[min([row[4] for row in data])-1, max([row[3] for row in data])+1],
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/191_202312302255.png')
