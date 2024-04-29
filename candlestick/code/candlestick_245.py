import pandas as pd
import plotly.graph_objects as go

data = {'Date': ['2021-01-03', '2021-01-10', '2021-01-17', '2021-01-24', '2021-01-31', '2021-02-07', '2021-02-14', '2021-02-21'],
        'Open Price ($)': [200000, 210500, 212000, 220500, 227500, 230500, 243000, 255500],
        'Close Price ($)': [210000, 213000, 220000, 227000, 230000, 240000, 255000, 260000],
        'High Price ($)': [215000, 220000, 225000, 230000, 235000, 245000, 260000, 265000],
        'Low Price ($)': [195000, 205000, 210000, 216000, 225000, 228000, 238000, 252000]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

fig.update_layout(title='Weekly Housing Market Price Trend in 2021.',
                  xaxis_title='Date',
                  yaxis_title='Price ($)',
                  width=1000,
                  height=600,
                  margin=dict(l=50, r=50, t=50, b=50),
                  yaxis_range=[190000, 270000])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/148_202312302255.png')