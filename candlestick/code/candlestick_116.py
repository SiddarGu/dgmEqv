import plotly.graph_objects as go

data = {
    'Month': ['2021-10', '2021-11', '2021-12', '2022-01', '2022-02', '2022-03', '2022-04'],
    'Starting Salary ($)': [4000, 4200, 4300, 4400, 4600, 4700, 4600],
    'Ending Salary ($)': [4200, 4300, 4400, 4600, 4700, 4600, 4800],
    'Highest Salary ($)': [4500, 4600, 4700, 5000, 5100, 5200, 5100],
    'Lowest Salary ($)': [3900, 4100, 4150, 4200, 4450, 4200, 4400]
}

fig = go.Figure(data=[go.Candlestick(
    x=data['Month'],
    open=data['Starting Salary ($)'],
    high=data['Highest Salary ($)'],
    low=data['Lowest Salary ($)'],
    close=data['Ending Salary ($)'])]
)

fig.update_layout(
    title="Monthly Salary Range Trend in Human Resources Department",
    xaxis_title="Month",
    yaxis_title="Salary ($)",
    width=1000,
    height=800,
    margin=dict(l=50, r=50, t=50, b=50),
    yaxis_range=[min(data['Lowest Salary ($)'])-100, max(data['Highest Salary ($)'])+100],
)

fig.update_traces(
    increasing_line_color='#00FF00',
    decreasing_line_color='#FF0000',
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/155_202312302255.png')