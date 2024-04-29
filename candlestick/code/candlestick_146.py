import plotly.graph_objects as go

data = [
    {'Date': '2021-01-04', 'Opening Price ($)': 120, 'Closing Price ($)': 123.5, 'High Price ($)': 128, 'Low Price ($)': 115},
    {'Date': '2021-01-11', 'Opening Price ($)': 125, 'Closing Price ($)': 130, 'High Price ($)': 135, 'Low Price ($)': 120},
    {'Date': '2021-01-18', 'Opening Price ($)': 130, 'Closing Price ($)': 134, 'High Price ($)': 137, 'Low Price ($)': 127},
    {'Date': '2021-01-25', 'Opening Price ($)': 135, 'Closing Price ($)': 139, 'High Price ($)': 142, 'Low Price ($)': 130},
    {'Date': '2021-02-01', 'Opening Price ($)': 140, 'Closing Price ($)': 145, 'High Price ($)': 150, 'Low Price ($)': 135},
    {'Date': '2021-02-08', 'Opening Price ($)': 145, 'Closing Price ($)': 150, 'High Price ($)': 155, 'Low Price ($)': 140},
    {'Date': '2021-02-15', 'Opening Price ($)': 150, 'Closing Price ($)': 155, 'High Price ($)': 160, 'Low Price ($)': 145},
    {'Date': '2021-02-22', 'Opening Price ($)': 155, 'Closing Price ($)': 160, 'High Price ($)': 165, 'Low Price ($)': 150},
    {'Date': '2021-03-01', 'Opening Price ($)': 160, 'Closing Price ($)': 165, 'High Price ($)': 170, 'Low Price ($)': 155},
    {'Date': '2021-03-08', 'Opening Price ($)': 165, 'Closing Price ($)': 170, 'High Price ($)': 175, 'Low Price ($)': 160},
    {'Date': '2021-03-15', 'Opening Price ($)': 170, 'Closing Price ($)': 175, 'High Price ($)': 180, 'Low Price ($)': 165},
    {'Date': '2021-03-22', 'Opening Price ($)': 175, 'Closing Price ($)': 180, 'High Price ($)': 185, 'Low Price ($)': 170},
    {'Date': '2021-03-29', 'Opening Price ($)': 180, 'Closing Price ($)': 185, 'High Price ($)': 190, 'Low Price ($)': 175}
]

fig = go.Figure(data=[go.Candlestick(
    x=[row['Date'] for row in data],
    open=[row['Opening Price ($)'] for row in data],
    close=[row['Closing Price ($)'] for row in data],
    high=[row['High Price ($)'] for row in data],
    low=[row['Low Price ($)'] for row in data]
)])

fig.update_layout(
    title='Law and Legal Affairs Sector Stock Performance in Q1 2021',
    width=1000,
    height=800,
    xaxis_range=['2021-01-01', '2021-04-01'],
    yaxis_range=[100, 200],
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/138_202312302255.png')