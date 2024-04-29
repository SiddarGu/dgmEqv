import plotly.graph_objects as go
import pandas as pd

# Data
data = {'Date': ['2020-06-01', '2020-06-02', '2020-06-03', '2020-06-04', '2020-06-05', '2020-06-06', '2020-06-07', '2020-06-08', '2020-06-09', '2020-06-10'],
        'Open Price ($)': [62.35, 65.11, 67.12, 69.75, 71.50, 70.40, 73.00, 75.50, 77.00, 76.00],
        'Close Price ($)': [64.50, 66.54, 68.75, 70.50, 70.20, 72.50, 74.50, 76.20, 75.50, 77.50],
        'High Price ($)': [65.23, 67.35, 69.00, 71.35, 72.15, 73.25, 75.35, 77.15, 77.75, 78.35],
        'Low Price ($)': [60.88, 64.80, 66.54, 68.99, 69.85, 69.99, 72.80, 74.90, 75.30, 75.99]}

df = pd.DataFrame(data)

# Candlestick Chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

# Figure Layout
fig.update_layout(title='Weekly Stock Price Range for a Major Hotel Chain',
                  xaxis_rangeslider_visible=False,
                  width=800,
                  height=600,
                  margin=dict(l=20, r=20, t=50, b=50),
                  yaxis=dict(range=[df['Low Price ($)'].min() - 5,
                                    df['High Price ($)'].max() + 5]))

# Save Figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/101_202312302255.png')
