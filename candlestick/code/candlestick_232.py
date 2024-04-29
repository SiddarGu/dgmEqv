import plotly.graph_objects as go

data = {
    'Date': ['2021-01-05', '2021-01-12', '2021-01-19', '2021-01-26', '2021-02-02', '2021-02-09', '2021-02-16', '2021-02-23', '2021-03-02', '2021-03-09', '2021-03-16', '2021-03-23', '2021-03-30'],
    'Open Price ($)': [75, 78, 72.5, 71, 74, 76, 80, 82, 81, 85, 88, 80, 82],
    'Close Price ($)': [77, 75.5, 70, 73, 78.1, 78, 82, 80.5, 83, 88, 85.5, 82, 80],
    'High Price ($)': [80, 81, 75.3, 76, 80.2, 82, 84.5, 86, 86.2, 90.5, 89.2, 84, 84.5],
    'Low Price ($)': [70, 73, 67, 69, 72.5, 74, 77.5, 78, 80.5, 82, 84, 78, 77]
}

fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                     open=data['Open Price ($)'],
                                     high=data['High Price ($)'],
                                     low=data['Low Price ($)'],
                                     close=data['Close Price ($)'])])

fig.update_layout(
    title='Financial Trend of Sports and Entertainment Company',
    width=1200,
    height=800,
    xaxis=dict(
        title='Date',
        showticklabels=True
    ),
    yaxis=dict(
        title='Price ($)',
        autorange=True
    )
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/192_202312302255.png')
