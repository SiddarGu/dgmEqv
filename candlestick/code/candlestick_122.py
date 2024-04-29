import plotly.graph_objects as go
import pandas as pd

# Create DataFrame
data = {
    'Date': ['2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-09', '2022-01-10', '2022-01-11'],
    'Open Price ($)': [75.5, 76.1, 77, 78.3, 79, 80.1, 81.2, 82.5],
    'Close Price ($)': [76.2, 75.6, 78.2, 78.8, 80.2, 80.7, 82, 83.2],
    'High Price ($)': [79.9, 78, 80.3, 81.5, 82.5, 83.4, 85, 85.7],
    'Low Price ($)': [73.8, 73.7, 76.1, 77.2, 78.1, 78.9, 80.2, 81.3]
}

df = pd.DataFrame(data)

# Create figure
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open Price ($)'],
    close=df['Close Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)']
)])

# Update layout
fig.update_layout(
    title='Government Spending for Public Policy - Weekly Overview',
    width=800,
    height=600,
    xaxis_rangeslider_visible=False,
    xaxis=dict(tickangle=-45),
    yaxis=dict(range=[70, 90]),
    margin=dict(l=20, r=20, t=50, b=20),
    font=dict(size=10),
)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/108_202312302255.png')