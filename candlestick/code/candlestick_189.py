import pandas as pd
import plotly.graph_objects as go

# Data
data = {
    'Date': ['2019-05-06', '2019-05-07', '2019-05-08', '2019-05-09', '2019-05-10', '2019-05-11'],
    'Open Price ($)': [75, 76, 80, 85, 89, 96],
    'Close Price ($)': [76.5, 79, 83, 86.5, 92, 98],
    'High Price ($)': [78, 84, 94, 95, 98, 99],
    'Low Price ($)': [72.8, 75, 79, 81, 87, 93]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)'],
    close=df['Close Price ($)']
)])

# Title
fig.update_layout(title='Food and Beverage Stock Market: May Weekly Performance')

# Size parameters
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    width=1200,
    height=800
)

# Y-axis range
fig.update_layout(yaxis_range=[70, 100])

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/109_202312302255.png')