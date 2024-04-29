import plotly.graph_objects as go
import pandas as pd

# Create dataframe from data
data = {'Date': ['2021-09-01', '2021-09-02', '2021-09-03', '2021-09-04', '2021-09-05', '2021-09-06'],
        'Open Price ($)': [131.1, 138.8, 143.1, 152.5, 151.7, 156.3],
        'Close Price ($)': [135.9, 140.6, 152.6, 150.2, 154.3, 153.2],
        'High Price ($)': [138.2, 143.1, 158.2, 155, 158, 157.9],
        'Low Price ($)': [127, 135.7, 140.3, 144.1, 146.5, 149.9]}
df = pd.DataFrame(data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     close=df['Close Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'])])

# Update layout
fig.update_layout(title='Freight Shipping Company Financial Analysis of a Week',
                  width=800,
                  height=600,
                  xaxis_range=['2021-09-01', '2021-09-06'],
                  yaxis_range=[120, 160],
                  margin=dict(l=50, r=50, t=50, b=50))

# Save figure as image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/59_202312302255.png')