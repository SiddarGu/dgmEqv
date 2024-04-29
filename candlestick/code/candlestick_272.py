import plotly.graph_objects as go
import pandas as pd

# Create dataframe
data = {
    'Date': ['2021-08-01', '2021-08-08', '2021-08-15', '2021-08-22', '2021-08-29', '2021-09-05', '2021-09-12', '2021-09-19'],
    'Open Price ($)': [120.5, 123, 126, 123.5, 125, 126, 127.5, 129],
    'Close Price ($)': [122.3, 125.5, 123, 124.3, 125, 127.5, 128, 129.5],
    'High Price ($)': [125.6, 126.8, 126.2, 125, 128.5, 128, 130.7, 131.2],
    'Low Price ($)': [118.7, 119.5, 121, 121.4, 122.7, 125, 125.5, 126.5]
}

df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create trace for open price
trace_open = go.Candlestick(
    x=df['Date'],
    open=df['Open Price ($)'],
    close=df['Close Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)'],
    name='Open Price'
)

# Create layout
layout = go.Layout(
    title='Weekly Stock Trends of Major Tourism and Hospitality Companies',
    yaxis_range=[df['Low Price ($)'].min()-1, df['High Price ($)'].max()+1],
    width=1200,
    height=800,
    showlegend=True,
    xaxis=dict(
        title='Date',
        rangeslider=dict(
            visible=False
        )
    ),
    yaxis=dict(
        title='Price ($)'
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        size=10
    )
)

# Create figure
fig = go.Figure(data=[trace_open], layout=layout)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/145_202312302255.png')