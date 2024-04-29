import pandas as pd
import plotly.graph_objects as go

# Create DataFrame from data
data = {'Date': ['2021-05-01', '2021-05-02', '2021-05-03', '2021-05-04', '2021-05-05', '2021-05-06', '2021-05-07', '2021-05-08', '2021-05-09', '2021-05-10'],
        'Open Price ($)': [100.2, 102.8, 103, 105.5, 106, 107.2, 106.5, 107.8, 108, 109.2],
        'Close Price ($)': [102.5, 104.5, 105, 106, 107.3, 106.5, 107.9, 108.1, 109.3, 110.1],
        'High Price ($)': [105.5, 106.7, 107.5, 108, 108.7, 109.2, 110.2, 111.3, 112.5, 113],
        'Low Price ($)': [98.8, 100, 99.5, 102, 103.2, 105.4, 105.8, 106.7, 107.5, 108.6]}
df = pd.DataFrame(data)

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open Price ($)'],
    close=df['Close Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)']
)])

# Configure the layout
fig.update_layout(
    title='Pharmaceutical Company Stock Performance - 10-Day Overview',
    width=1200,
    height=800,
    xaxis=dict(
        title='Date',
        tickmode='linear'
    ),
    yaxis=dict(
        title='Stock Price ($)',
        tickmode='linear',
        range=[df['Low Price ($)'].min() - 1, df['High Price ($)'].max() + 1]
    )
)

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/160_202312302255.png')