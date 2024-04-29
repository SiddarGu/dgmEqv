import pandas as pd
import plotly.graph_objects as go

# Read the data
data = pd.DataFrame({
    'Date': ['2019-01-01', '2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01'],
    'Open Price': [32.5, 33, 35, 36, 38],
    'Close Price': [34, 35, 36, 37.7, 39.9],
    'High Price': [35.2, 37, 38, 39.6, 41.2],
    'Low Price': [30.8, 31.9, 33.7, 34.4, 36]
})

# Convert the date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                    open=data['Open Price'],
                                    high=data['High Price'],
                                    low=data['Low Price'],
                                    close=data['Close Price'])])

# Update the layout
fig.update_layout(
    title='Financial Trend in Humanities Publishing Industry',
    xaxis_title='Date',
    yaxis_title='Price',
    width=800,
    height=500,
    margin=dict(t=50, b=50),
    yaxis_range=[data['Low Price'].min() - 1, data['High Price'].max() + 1],
    autosize=False
)

# Save the figure as a png image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/97_202312302255.png')