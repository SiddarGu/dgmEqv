import plotly.graph_objects as go
import pandas as pd

# Define the data
data = {'Date': ['2022-01-03', '2022-01-10', '2022-01-17', '2022-01-24', '2022-01-31', '2022-02-07'],
        'Open Price ($/Bushel)': [4.17, 4.23, 4.20, 4.24, 4.27, 4.32],
        'Close Price ($/Bushel)': [4.19, 4.19, 4.25, 4.27, 4.31, 4.35],
        'High Price ($/Bushel)': [4.23, 4.26, 4.29, 4.33, 4.36, 4.40],
        'Low Price ($/Bushel)': [4.12, 4.18, 4.15, 4.20, 4.26, 4.28]}
df = pd.DataFrame(data)

# Create the candlestick chart
fig = go.Figure(data=go.Candlestick(x=df['Date'],
                                   open=df['Open Price ($/Bushel)'],
                                   high=df['High Price ($/Bushel)'],
                                   low=df['Low Price ($/Bushel)'],
                                   close=df['Close Price ($/Bushel)']))

# Update the figure layout
fig.update_layout(title='Weekly Corn Prices in Agriculture Market',
                  autosize=True,
                  width=800,
                  height=600,
                  xaxis_range=[df['Date'].min(), df['Date'].max()],
                  yaxis_range=[df[['Open Price ($/Bushel)', 'Low Price ($/Bushel)']].min().min(),
                               df[['Close Price ($/Bushel)', 'High Price ($/Bushel)']].max().max()])

# Save the figure as an image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/123_202312302255.png')