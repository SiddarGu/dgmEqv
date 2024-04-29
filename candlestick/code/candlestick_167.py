import pandas as pd
import plotly.graph_objects as go

data = {'Date': ['2022-01-01', '2022-01-08', '2022-01-15', '2022-01-22', '2022-01-29', '2022-02-05', '2022-02-12'],
        'Open Price ($)': [52.8, 60.2, 55, 57.5, 52, 53.4, 54],
        'Close Price ($)': [58.2, 54.8, 58, 55.2, 56, 55.9, 57.5],
        'High Price ($)': [61.3, 62.5, 59.7, 57.8, 58.5, 59.7, 60],
        'Low Price ($)': [47, 50.3, 49, 50, 51, 52.1, 51]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

fig.update_layout(title={'text': 'Manufacturing Sector Stock Prices Overview'},
                  width=800,
                  height=600,
                  margin={'l': 50, 'r': 50, 'b': 50, 't': 80},
                  yaxis_range=[40, 70])

fig.update_layout(autosize=False,
                  showlegend=False,
                  xaxis=dict(showgrid=False),
                  yaxis=dict(showgrid=False),
                  font=dict(family='sans-serif', size=12))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/64_202312302255.png')
