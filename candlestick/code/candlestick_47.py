

import plotly.graph_objects as go
import pandas as pd

data = [['2019-11-01',45,50,53,41], ['2019-11-08',51,52,54,49], ['2019-11-15',50,51.5,54,47], ['2019-11-22',51,48,52,45], ['2019-11-29',49,50.5,52,47], ['2019-12-06',51,50,53,48], ['2019-12-13',50,47,50,44], ['2019-12-20',48,50,53,45]]

df = pd.DataFrame(data, columns = ['date', 'open', 'close', 'high', 'low'])
fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])
fig.update_layout(title='Financial Trends in Tourism and Hospitality - Weekly Overview',
                  yaxis_range=[df['low'].min(), df['high'].max()],
                  width=800,
                  height=600,
                  font=dict(
                      size=12,
                      color="black"
                  ))
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/Full/candlestick/png_val/candlestick_47.png')