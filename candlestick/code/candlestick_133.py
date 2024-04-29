import plotly.graph_objects as go
import pandas as pd

# Creating the dataframe
data = {
    'Date': ['2019-04-25', '2019-04-26', '2019-04-27', '2019-04-28', '2019-04-30'],
    'Opening Price ($)': [71.8, 76.0, 78.5, 77.0, 75.0],
    'Closing Price ($)': [74.2, 78.3, 76.4, 75.1, 77.0],
    'High Price ($)': [76.0, 79.5, 80.0, 78.0, 79.0],
    'Low Price ($)': [70.0, 72.0, 75.0, 73.0, 73.0]
}

df = pd.DataFrame(data)

# Creating the candlestick chart
fig = go.Figure(data=go.Candlestick(
    x=df['Date'],
    open=df['Opening Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)'],
    close=df['Closing Price ($)']
))

# Updating the layout
fig.update_layout(
    title='Trends in the Energy and Utilities Sector',
    width=800,
    height=600,
    xaxis=dict(
        tickfont=dict(size=8)
    ),
    yaxis=dict(
        tickfont=dict(size=8),
        range=[min(df['Low Price ($)']) * 0.99, max(df['High Price ($)']) * 1.01]
    )
)

# Saving the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/100_202312302255.png')