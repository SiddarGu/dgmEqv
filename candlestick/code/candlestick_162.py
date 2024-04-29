import plotly.graph_objects as go

# Data
data = {
    'Date': ['2022-01-03', '2022-01-10', '2022-01-17', '2022-01-24', '2022-01-31', '2022-02-07', '2022-02-14'],
    'Open Price ($)': [1200, 1250, 1300, 1275, 1280, 1300, 1325],
    'Close Price ($)': [1250, 1300, 1275, 1280, 1300, 1325, 1315],
    'High Price ($)': [1300, 1350, 1325, 1330, 1340, 1350, 1360],
    'Low Price ($)': [1150, 1200, 1250, 1250, 1260, 1275, 1300]
}

# Candlestick Chart
fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                            open=data['Open Price ($)'],
                            high=data['High Price ($)'],
                            low=data['Low Price ($)'],
                            close=data['Close Price ($)'])])

# Layout
fig.update_layout(
    title='Weekly Funding Trends in Academia',
    height=500,
    width=800,
    yaxis_range=[1100, 1400],
    font=dict(
        family='Arial',
    )
)

# Save Figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/216_202312302255.png')