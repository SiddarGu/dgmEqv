import plotly.graph_objects as go

# Data
data = [
    ['2022-01-12', 10, 12, 14, 9],
    ['2022-01-19', 13, 14, 15, 12],
    ['2022-01-26', 15, 16, 17, 14],
    ['2022-02-02', 16, 18, 19, 15],
    ['2022-02-09', 18, 17, 20, 16],
    ['2022-02-16', 17, 16, 18, 14],
    ['2022-02-23', 15, 14, 16, 12]
]

# Create figure
fig = go.Figure(data=[go.Candlestick(
    x=[data[0][0], data[1][0], data[2][0], data[3][0], data[4][0], data[5][0], data[6][0]],
    open=[data[0][1], data[1][1], data[2][1], data[3][1], data[4][1], data[5][1], data[6][1]],
    close=[data[0][2], data[1][2], data[2][2], data[3][2], data[4][2], data[5][2], data[6][2]],
    high=[data[0][3], data[1][3], data[2][3], data[3][3], data[4][3], data[5][3], data[6][3]],
    low=[data[0][4], data[1][4], data[2][4], data[3][4], data[4][4], data[5][4], data[6][4]]
)])

# Update layout
fig.update_layout(
    title='Weekly Price Range of different crops in Agriculture and Food Production.',
    xaxis=dict(
        title='Date'
    ),
    yaxis=dict(
        title='Price ($/Bushel)',
        range=[0, 25]
    ),
    width=800,
    height=600
)

# Save image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/196_202312302255.png')