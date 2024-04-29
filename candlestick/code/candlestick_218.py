
import plotly.graph_objects as go
import pandas as pd

data = [['2019-04-26', 50.5, 52, 54.2, 49.8],
        ['2019-04-27', 53, 52.1, 55.2, 51.9],
        ['2019-04-28', 53, 54, 56, 52],
        ['2019-04-29', 54, 55.7, 57.5, 53.4],
        ['2019-04-30', 55.2, 56.9, 58.2, 54],
        ['2019-05-01', 57, 59.2, 60.5, 56],
        ['2019-05-02', 59, 58.3, 60.2, 57.4],
        ['2019-05-03', 58.7, 59.3, 60, 58]]

df = pd.DataFrame(data, columns=['Date', 'Open Price ($)', 'Close Price ($)', 'High Price ($)', 'Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                    open=df['Open Price ($)'],
                                    high=df['High Price ($)'],
                                    low=df['Low Price ($)'],
                                    close=df['Close Price ($)'])])
fig.update_layout(title='Science and Engineering Stock Price Trend Overview',
                  yaxis_range=[min(df['Low Price ($)']), max(df['High Price ($)'])],
                  width=1800,
                  height=1000,
                  font=dict(family='Courier New, monospace', size=18, color='#7f7f7f'))
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/9_202312252244.png")