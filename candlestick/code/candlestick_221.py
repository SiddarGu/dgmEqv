
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame([['2020-06-02', 25.7, 26.2, 27.1, 24.7],
                    ['2020-06-09',  26.3, 30.5, 31.2, 26],
                    ['2020-06-16',  30.8, 32.2, 33.1, 29.3],
                    ['2020-06-23',  32.1, 30.5, 34.2, 29.5],
                    ['2020-06-30',  29.8, 30.6, 31.2, 28.9],
                    ['2020-07-07',  31.2, 34.2, 34.5, 30.6],
                    ['2020-07-14',  33.5, 35.1, 36.2, 32.9],
                    ['2020-07-21',  35.2, 35.8, 37.2, 34]],
                    columns=['Date', 'Open Price ($)', 'Close Price ($)', 'High Price ($)', 'Low Price ($)'])

fig = go.Figure(data=[go.Candlestick( x=df['Date'],
                        open=df['Open Price ($)'],
                        high=df['High Price ($)'],
                        low=df['Low Price ($)'],
                        close=df['Close Price ($)'])])

fig.update_layout(title_text='Financial Trend in Social Sciences and Humanities - Weekly Overview',
                  width=1600, height=800,
                  yaxis_range=[24.7, 37.2],
                  font=dict(family="Courier New, monospace",
                  size=15,
                  color="#7f7f7f"))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/15_202312252244.png')