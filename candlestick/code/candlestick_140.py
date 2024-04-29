import plotly.graph_objects as go
import pandas as pd

# Define the data
data = {'Date': ['2020-07-01', '2020-07-08', '2020-07-15', '2020-07-22', '2020-07-29', '2020-08-05', '2020-08-12', '2020-08-19'],
        'Open Price ($)': [34.7, 36, 38, 40, 42, 44, 46, 48],
        'Close Price ($)': [35.8, 37.9, 39.5, 41.9, 43.7, 45.8, 47.8, 49.9],
        'High Price ($)': [36.2, 38.5, 40.1, 42.5, 44.3, 46.5, 48.6, 50.5],
        'Low Price ($)': [33.9, 35.7, 37.6, 39.8, 41.8, 43.9, 46.1, 47.9]}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create the figure and axis
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

# Update the layout
fig.update_layout(title='Manufacturing and Production Sector Stock Trend Analysis',
                  height=600,
                  width=800,
                  yaxis_range=[30, 55],
                  font=dict(family='Arial'),
                  plot_bgcolor='white')

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/78_202312302255.png')