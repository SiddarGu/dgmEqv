import plotly.graph_objects as go
import pandas as pd

data = {'Date': ['2019-06-01', '2019-06-02', '2019-06-03', '2019-06-04', '2019-06-05', '2019-06-06', '2019-06-07',
                 '2019-06-08', '2019-06-09', '2019-06-10', '2019-06-11', '2019-06-12', '2019-06-13', '2019-06-14',
                 '2019-06-15', '2019-06-16'],
        'Open Price ($)': [150, 155, 157, 160, 165, 170, 175, 177, 180, 185, 187, 192, 197, 200, 205, 210],
        'Close Price ($)': [155.2, 157.4, 160.5, 165.7, 170.3, 175.1, 177.3, 180.4, 185.0, 187.2, 192.6, 197.8,
                            200.1, 205.2, 210.4, 215.5],
        'High Price ($)': [160, 165, 170, 175, 180, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240],
        'Low Price ($)': [145, 152, 156, 158, 160, 165, 170, 172, 175, 180, 182, 185, 190, 195, 200, 205]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

fig.update_layout(title='Healthcare Sector Stock Price Trend in June 2019', width=1000, height=600, autosize=False,
                  xaxis=dict(title='Date'), yaxis=dict(title='Price ($)'),
                  yaxis_range=[min(df['Low Price ($)']) * 0.9, max(df['High Price ($)']) * 1.1])

fig.update_layout(showlegend=False)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/58_202312302255.png')