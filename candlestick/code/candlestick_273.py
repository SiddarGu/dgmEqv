import plotly.graph_objects as go

data = {'Date': ['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05', '2019-01-06', '2019-01-07'],
        'Open Price ($)': [28700, 26850, 30100, 30500, 33800, 35000, 38300],
        'Close Price ($)': [29500, 27500, 32100, 33700, 35000, 37600, 40000],
        'High Price ($)': [30300, 28100, 32500, 34000, 35000, 38000, 40500],
        'Low Price ($)': [28000, 26000, 30000, 30000, 33000, 34500, 37700]}

fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                     open=data['Open Price ($)'],
                                     high=data['High Price ($)'],
                                     low=data['Low Price ($)'],
                                     close=data['Close Price ($)'])])

fig.update_layout(
    title='Modern Art Market Tendencies - Weekly Overview',
    width=800,
    height=600,
    xaxis_rangeslider_visible=False,
    font=dict(family='Arial', size=12),
    yaxis=dict(range=[min(data['Low Price ($)']), max(data['High Price ($)'])]),
    margin=dict(l=0, r=0, t=30, b=30),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/128_202312302255.png')