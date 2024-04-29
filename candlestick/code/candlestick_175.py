import plotly.graph_objects as go
import pandas as pd

# Data
data = {
    'Date': ['2021-06-01', '2021-06-02', '2021-06-03', '2021-06-04', '2021-06-05'],
    'Opening Price ($)': [75.5, 80, 83, 85, 90],
    'Closing Price ($)': [79.2, 82.3, 84, 90.7, 95.9],
    'High Price ($)': [81.4, 85.2, 86, 91.6, 96.2],
    'Low Price ($)': [73.8, 77.9, 81.7, 83.4, 88]
}

df = pd.DataFrame(data)

# Create Candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Opening Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)'],
    close=df['Closing Price ($)']
)])

# Set layout parameters
fig.update_layout(
    title='Antique Art Auction Market - Week Overview',
    plot_bgcolor='white',
    autosize=False,
    width=1000,
    height=600,
    font=dict(
        size=10
    ),
    margin=dict(l=40, r=40, b=40, t=40),
    yaxis=dict(
        autorange=True,
        fixedrange=False
    ),
    yaxis_range=[70, 100]
)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/110_202312302255.png')