import plotly.graph_objects as go
import pandas as pd

# Define the data
data = {'Date': ['2023-03-01', '2023-03-02', '2023-03-03', '2023-03-04', '2023-03-05', '2023-03-06', '2023-03-07', '2023-03-08', '2023-03-09', '2023-03-10'],
        'Open Price ($)': [120, 125, 127, 131, 137, 139, 140, 143, 146, 151],
        'Close Price ($)': [123.5, 124, 130, 134, 138, 140, 142, 145, 148, 153],
        'High Price ($)': [130, 132, 135, 141, 145, 147, 148, 150, 155, 160],
        'Low Price ($)': [117, 120, 124, 130, 133, 136, 139, 140, 144, 150]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'], high=df['High Price ($)'],
                low=df['Low Price ($)'], close=df['Close Price ($)'])])

# Set the title of the figure
fig.update_layout(title='Trends in Technology Company Stock Prices')

# Set the layout parameters
fig.update_layout(width=800, height=600)
fig.update_layout(margin=dict(l=50, r=50, t=50, b=50))

# Set the y-axis range
fig.update_layout(yaxis_range=[min(df['Low Price ($)'])-5, max(df['High Price ($)'])+5])

# Save the figure as an image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/72_202312302255.png')