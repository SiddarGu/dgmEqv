import plotly.graph_objects as go
import pandas as pd

# Define the data
data = {'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01'],
        'Open Price ($)': [75.5, 78.5, 81.3, 83.5, 86.6, 89.6],
        'Close Price ($)': [78.2, 80.1, 82.8, 85.6, 88.9, 90.8],
        'High Price ($)': [80.3, 81.9, 84.6, 87.8, 90.2, 92.5],
        'Low Price ($)': [72.4, 76.8, 79.4, 81.5, 84.5, 87.9]}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     close=df['Close Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'])])

# Set the title
fig.update_layout(title='Market Status for Modern Art Auctions in 2020', width=800, height=600)

# Set the y-axis range
min_value = df['Low Price ($)'].min()
max_value = df['High Price ($)'].max()
fig.update_layout(yaxis_range=[min_value-5, max_value+5])

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/118_202312302255.png')
