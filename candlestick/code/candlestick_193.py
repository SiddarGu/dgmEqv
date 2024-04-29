import plotly.graph_objects as go

data = [
    ['2021-10-01', 150, 155, 160, 145],
    ['2021-10-02', 155, 160, 165, 150],
    ['2021-10-03', 165, 165, 170, 160],
    ['2021-10-04', 170, 175, 180, 165],
    ['2021-10-05', 175, 180, 185, 170],
    ['2021-10-06', 180, 185, 190, 175],
    ['2021-10-07', 185, 190, 195, 175],
    ['2021-10-08', 195, 200, 205, 190]
]

fig = go.Figure(data=[go.Candlestick(x=[row[0] for row in data],
                                     open=[row[1] for row in data],
                                     close=[row[2] for row in data],
                                     high=[row[3] for row in data],
                                     low=[row[4] for row in data])])

fig.update_layout(title='Performance of HealthCare Stocks in October 2021',
                  xaxis_title='Date',
                  yaxis_title='Price ($)',
                  width=800,
                  height=600,
                  yaxis_range=[140, 220],
                  showlegend=False,
                  paper_bgcolor='white',
                  plot_bgcolor='white',
                  font=dict(color='black'))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/177_202312302255.png')
