import plotly.graph_objs as go

data = [
    ['2022-07-01', 120, 130, 135, 118],
    ['2022-07-02', 133, 132, 135, 129],
    ['2022-07-03', 132, 140, 142, 130],
    ['2022-07-04', 142, 145, 147, 140],
    ['2022-07-05', 145, 147, 150, 142],
    ['2022-07-06', 147, 150, 152, 145],
    ['2022-07-07', 150, 155, 158, 145],
    ['2022-07-08', 157, 156, 160, 155],
    ['2022-07-09', 156, 160, 163, 154],
    ['2022-07-10', 161, 163, 165, 160],
    ['2022-07-11', 165, 172, 175, 162],
    ['2022-07-12', 170, 169, 172, 167],
    ['2022-07-13', 171, 174, 178, 166],
    ['2022-07-14', 175, 180, 182, 174],
    ['2022-07-15', 180, 182, 185, 178],
    ['2022-07-16', 185, 190, 193, 182],
    ['2022-07-17', 192, 200, 203, 190],
    ['2022-07-18', 198, 197, 200, 195],
    ['2022-07-19', 200, 205, 210, 198],
    ['2022-07-20', 210, 218, 220, 200]
]

x = [entry[0] for entry in data]
open_price = [entry[1] for entry in data]
close_price = [entry[2] for entry in data]
high_price = [entry[3] for entry in data]
low_price = [entry[4] for entry in data]

fig = go.Figure(data=[go.Candlestick(x=x,
                open=open_price, high=high_price,
                low=low_price, close=close_price)])

fig.update_layout(
    title='Manufacturing and Production Company Stock Performance in July 2022',
    width=800,
    height=600,
    xaxis=dict(
        title='Date',
        tickmode='auto',
        nticks=10,
        tickangle=45,
    ),
    yaxis=dict(
        title='Stock Price ($)',
        autorange=True,
        type='linear'
    )
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/76_202312302255.png')