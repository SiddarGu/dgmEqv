import plotly.graph_objects as go
import pandas as pd

# Define the data
data = {'Date': ['2021-07-01', '2021-07-02', '2021-07-03', '2021-07-04', '2021-07-05', '2021-07-06'],
        'Open Price ($/Share)': [120, 114.8, 119.9, 117.3, 120, 123.5],
        'Close Price ($/Share)': [115.8, 118, 117.3, 119.7, 123, 124.1],
        'High Price ($/Share)': [122.5, 122.2, 121.4, 120.8, 124.2, 126.3],
        'Low Price ($/Share)': [113.9, 112.7, 115.6, 116.1, 119, 121.8]}

# Create a dataframe from the data
df = pd.DataFrame(data)

# Convert the date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($/Share)'],
                high=df['High Price ($/Share)'],
                low=df['Low Price ($/Share)'],
                close=df['Close Price ($/Share)'])])

# Set the title
fig.update_layout(title='Biotech Sector Stock Performance in July 2021')

# Set the layout parameters
fig.update_layout(
    width=800,
    height=600,
    autosize=False,
    margin=dict(t=30, b=30, l=30, r=30),
    paper_bgcolor="white",
)

# Set the yaxis range
fig.update_layout(yaxis_range=[min(df['Low Price ($/Share)']) - 5, max(df['High Price ($/Share)']) + 5])

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/211_202312302255.png')