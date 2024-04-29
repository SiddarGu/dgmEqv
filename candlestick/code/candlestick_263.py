import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame({'Date': ['2020-11-02', '2020-11-03', '2020-11-04', '2020-11-05', '2020-11-06', '2020-11-07', '2020-11-08', '2020-11-09', '2020-11-10', '2020-11-11', '2020-11-12'],
                   'Open Price ($)': [70, 73, 76, 78, 79, 80.5, 83, 84, 86, 89, 90],
                   'Close Price ($)': [72.5, 75, 77, 79, 80, 83, 85, 86, 89, 90, 92],
                   'High Price ($)': [75, 76, 78.5, 81, 82, 84, 86.5, 87, 90.5, 91.5, 93.7],
                   'Low Price ($)': [68, 70, 74.8, 76.1, 77.6, 80, 82, 82.5, 85.6, 87.5, 89]})

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

fig.update_layout(title='Food and Beverage Industry Stock Prices (November 2020)',
                  width=800,
                  height=600,
                  margin=dict(l=50, r=50, t=50, b=50),
                  xaxis_rangeslider_visible=False,
                  font=dict(size=12),
                  yaxis=dict(range=[df['Low Price ($)'].min() - 5, df['High Price ($)'].max() + 5]))

fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Price ($)')

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/52_202312302255.png')
