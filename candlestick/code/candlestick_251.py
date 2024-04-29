import plotly.graph_objects as go
import pandas as pd

# Create dataframe
data = {'Date': ['2022-01-01', '2022-01-08', '2022-01-15', '2022-01-22', '2022-01-29', '2022-02-05', '2022-02-12', '2022-02-19', '2022-02-26'],
        'Open Price ($)': [85, 89, 90, 97, 103, 98, 95, 96, 93],
        'Close Price ($)': [87, 88, 95, 100, 99, 95, 97, 94, 92],
        'High Price ($)': [90, 92, 98, 105, 105, 100, 99, 101, 95],
        'Low Price ($)': [80, 86, 85, 90, 98, 90, 91, 90, 89]}
df = pd.DataFrame(data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create figure
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

# Set layout parameters
fig.update_layout(title='Sports and Entertainment Industry Stocks Trend for Q1 2022',
                  height=600,
                  width=800,
                  yaxis_range=[df['Low Price ($)'].min() - 5, df['High Price ($)'].max() + 5])
fig.update_layout(font=dict(family='sans-serif'))

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/85_202312302255.png')