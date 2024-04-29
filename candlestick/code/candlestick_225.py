
import plotly.graph_objects as go
import pandas as pd

data = [['June 2020', 20.3, 21.2, 21.4, 19.8],
        ['July 2020', 20.7, 21.4, 21.6, 20.0],
        ['August 2020', 21.3, 21.5, 21.8, 20.3],
        ['September 2020', 21.5, 22.2, 22.4, 21.3],
        ['October 2020', 22.3, 20.9, 22.4, 20.5],
        ['November 2020', 20.5, 21.1, 21.3, 20.2],
        ['December 2020', 21.3, 21.6, 21.8, 20.9]]

df = pd.DataFrame(data, columns=['Month', 'Open Price ($)', 'Close Price ($)', 'High Price ($)', 'Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Month'],
                       open=df['Open Price ($)'],
                       high=df['High Price ($)'],
                       low=df['Low Price ($)'],
                       close=df['Close Price ($)'])])

fig.update_layout(title_text='Agricultural Commodity Price Trend in 2020',
                  yaxis_range=[min(df['Low Price ($)'].min(), df['Open Price ($)'].min(), df['Close Price ($)'].min()),
                               max(df['High Price ($)'].max(), df['Open Price ($)'].max(), df['Close Price ($)'].max())],
                  width=800, height=600, font=dict(family='sans-serif', size=15))

fig.write_image(r'/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/33_202312252244.png')