import plotly.graph_objects as go
import pandas as pd

# Define the data
data = {'Date': ['2022-01-12', '2022-01-19', '2022-01-26', '2022-02-02', '2022-02-09', '2022-02-16', '2022-02-23', '2022-03-02'],
        'Open Price ($)': [120, 134, 140, 145, 160, 155, 140, 150],
        'Close Price ($)': [135, 132, 150, 160, 156, 145, 145, 165],
        'High Price ($)': [145, 145, 155, 178, 180, 160, 168, 180],
        'Low Price ($)': [110, 131, 131, 145, 140, 140, 135, 130]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

# Set plot title
fig.update_layout(title='Legal Services Industry Stock Price Movement')

# Set size parameters
fig.update_layout(width=800, height=600)
fig.update_layout(margin=go.layout.Margin(
    l=50,
    r=50,
    b=50,
    t=50,
    pad=4
))

# Adjust yaxis range
fig.update_layout(yaxis_range=[min(df['Low Price ($)'])-10, max(df['High Price ($)'])+10])

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/183_202312302255.png')