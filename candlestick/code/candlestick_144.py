import plotly.graph_objects as go
import pandas as pd

# Create the candlestick chart
data = [['2020-01-02', 45.2, 47.8, 48, 42.8],
        ['2020-01-03', 47.9, 47.6, 48, 46.2],
        ['2020-01-04', 47, 48.3, 49.5, 45.8],
        ['2020-01-05', 49, 50, 50.2, 46.5],
        ['2020-01-06', 50.1, 51, 52, 49],
        ['2020-01-07', 51, 51.5, 52.8, 50.9],
        ['2020-01-08', 51.6, 53, 53.5, 51],
        ['2020-01-09', 53, 52.7, 53.4, 51.8],
        ['2020-01-10', 52, 53.2, 54, 51.9],
        ['2020-01-11', 53, 52.5, 53, 51.9]]

df = pd.DataFrame(data, columns=['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Opening Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Closing Price ($)'])])

# Update layout properties
fig.update_layout(title='Movie Theater Chain Stock Prices Trend in January 2020',
                  width=800,
                  height=600,
                  font=dict(family='Arial', size=12),
                  yaxis_range=[40, 55])

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/121_202312302255.png')
