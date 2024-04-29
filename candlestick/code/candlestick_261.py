import plotly.graph_objects as go
import pandas as pd

# Define the data
data = {'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01'],
        'Open Price($)': [40, 51, 55, 62, 68, 78],
        'Close Price($)': [50, 58, 64, 70, 79, 85],
        'High Price($)': [55, 60, 67, 75, 82, 90],
        'Low Price($)': [35, 41, 52, 61, 65, 76]}

df = pd.DataFrame(data)

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open Price($)'],
    close=df['Close Price($)'],
    high=df['High Price($)'],
    low=df['Low Price($)']
)])

# Update the layout
fig.update_layout(
    title='Investment Trends in the Cultural Arts Sector',
    width=1000,
    height=500,
    margin=dict(l=50, r=50, t=50, b=50),
    yaxis_range=[30, 100],
)

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/218_202312302255.png')