import plotly.graph_objects as go
import pandas as pd

# Create the data frame
data = {
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06'],
    'Opening Price ($)': [170.1, 175.2, 181.4, 188.2, 192.3, 198.5],
    'Closing Price ($)': [172.1, 180.1, 185, 190.7, 195, 200],
    'High Price ($)': [175.5, 182.3, 190.3, 192.5, 200, 205.7],
    'Low Price ($)': [168.2, 171, 179.7, 185.2, 190, 195.3]
}

df = pd.DataFrame(data)

# Convert the date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Opening Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Closing Price ($)'])])

# Set title
fig.update_layout(title='Weekly Price Trend for Tech Stocks')

# Set layout parameters
fig.update_layout(width=1000, height=800)

# Set the yaxis range
fig.update_layout(yaxis_range=[min(df['Low Price ($)']) - 5, 
                               max(df['High Price ($)']) + 5])

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/81_202312302255.png')