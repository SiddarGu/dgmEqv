import plotly.graph_objects as go
import pandas as pd

data = {'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01', '2020-10-01', '2020-11-01', '2020-12-01'],
        'Open Price ($)': [100, 101, 110, 105, 115, 110, 120, 115, 125, 120, 130, 125],
        'Close Price ($)': [104, 105, 114, 109, 119, 114, 124, 119, 129, 124, 134, 129],
        'High Price ($)': [106, 108, 116, 111, 121, 116, 126, 121, 131, 126, 136, 131],
        'Low Price ($)': [97, 99, 105, 100, 110, 105, 115, 110, 120, 115, 125, 120]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     close=df['Close Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'])])

fig.update_layout(title='Monthly Investment Trends in Science and Engineering Sector',
                  width=800,
                  height=600,
                  xaxis_title='Date',
                  yaxis_title='Price ($)',
                  yaxis_range=[90, 140],
                  margin=dict(l=50, r=50, t=50, b=50),
                  autosize=False,
                  plot_bgcolor='white')

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/213_202312302255.png')
