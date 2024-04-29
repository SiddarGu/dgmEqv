import pandas as pd
import plotly.graph_objects as go

# Data
data = {
    'Date': ['2022-03-01', '2022-03-02', '2022-03-03', '2022-03-04', '2022-03-05', '2022-03-06', '2022-03-07', '2022-03-08'],
    'Open Price ($)': [100, 105, 107, 110, 115, 112, 113, 114],
    'Close Price ($)': [105, 107, 110, 115, 112, 113, 114, 117],
    'High Price ($)': [108, 110, 114, 118, 117, 116, 117, 120],
    'Low Price ($)': [99, 104, 106, 109, 110, 111, 112, 113]
}

df = pd.DataFrame(data)

# Candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open Price ($)'],
    close=df['Close Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)']
)])

# Layout
fig.update_layout(
    title='Pharmaceutical Company Share Performance - Weekly Overview',
    xaxis_rangeslider_visible=False,
    xaxis_title='Date',
    yaxis_title='Price ($)',
    width=1000,
    height=600,
    autosize=False,
    margin=dict(l=10, r=10, b=10, t=60)
)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/150_202312302255.png')