import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Define the data
data = {'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01', '2020-10-01', '2020-11-01', '2020-12-01'],
        'Open Donation ($)': [25000, 27000, 29500, 32000, 32500, 33000, 35000, 36500, 38500, 39500, 40000, 42500],
        'Close Donation ($)': [26000, 29000, 31500, 33000, 33000, 34500, 36000, 37500, 39000, 40000, 41500, 43500],
        'High Donation ($)': [26500, 30000, 32000, 33500, 33500, 35000, 37000, 38000, 39500, 40500, 42500, 44500],
        'Low Donation ($)': [24000, 26000, 28500, 31000, 32000, 32500, 34500, 36000, 38000, 38500, 39000, 42000]}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Donation ($)'],
                                     high=df['High Donation ($)'],
                                     low=df['Low Donation ($)'],
                                     close=df['Close Donation ($)'])])

# Set the title of the figure
fig.update_layout(title_text='Monthly Donation Trend in Nonprofit Organizations')

# Set the size parameter
fig.update_layout(width=800, height=600)
fig.update_layout(margin=dict(l=50, r=50, t=50, b=50))

# Adjust the yaxis range
y_range = [df['Low Donation ($)'].min()-1000, df['High Donation ($)'].max()+1000]
fig.update_layout(yaxis_range=y_range)

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/75_202312302255.png')