import plotly.graph_objects as go

data = [
    ['2018-01-01', 1000, 1050, 1060, 990],
    ['2018-01-02', 1050, 1090, 1120, 1040],
    ['2018-01-03', 1040, 1080, 1100, 1030],
    ['2018-01-04', 1070, 1040, 1085, 1025],
    ['2018-01-05', 1050, 1010, 1060, 1005]
]

fig = go.Figure(data=[go.Candlestick(
    x=[data[0][0]],
    open=[data[0][1]],
    high=[data[0][3]],
    low=[data[0][4]],
    close=[data[0][2]],
)])

for i in range(1, len(data)):
    fig.add_trace(go.Candlestick(
        x=[data[i][0]],
        open=[data[i][1]],
        high=[data[i][3]],
        low=[data[i][4]],
        close=[data[i][2]],
        increasing_line_color='green',
        decreasing_line_color='red'
    ))

fig.update_layout(
    title='Historical Funding Trends in Humanities Research Grants',
    width=900,
    height=600,
    xaxis_range=[data[0][0], data[-1][0]],
    yaxis_range=[min([d[4] for d in data]), max([d[3] for d in data])]
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/60_202312302255.png')