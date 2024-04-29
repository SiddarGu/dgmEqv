import plotly.graph_objects as go
import pandas as pd

# Data
data = {
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08', '2021-01-09', '2021-01-10'],
    'Opening Price ($)': [20, 21.7, 21.5, 22.7, 23.5, 24.5, 26.2, 27, 28.2, 28.5],
    'Closing Price ($)': [21.5, 21, 22.5, 24, 25.5, 26, 25.5, 28, 27, 28.5],
    'High Price ($)': [22, 24, 23, 25, 26, 27, 29, 28.5, 30, 30.5],
    'Low Price ($)': [18.5, 20, 20, 21.5, 23, 24.5, 24.3, 25.5, 26.7, 27]
}

# DataFrame
df = pd.DataFrame(data)

# Create figure and add traces
fig = go.Figure(data=[
    go.Candlestick(
        x=df['Date'],
        open=df['Opening Price ($)'],
        close=df['Closing Price ($)'],
        high=df['High Price ($)'],
        low=df['Low Price ($)']
    )
])

# Update layout
fig.update_layout(
    title='Agriculture and Food Production Stock Price Trend',
    xaxis_rangeslider_visible=False,
    width=1000,
    height=500,
    margin=dict(l=50, r=50, t=50, b=50),
    yaxis=dict(
        title='Stock Price ($)',
        range=[min(df['Low Price ($)']) - 1, max(df['High Price ($)']) + 1]
    )
)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/180_202312302255.png')