
import plotly.graph_objects as go
import pandas as pd

data = [['2021-04-26', 50.5, 52.0, 54.2, 49.8], ['2021-04-27', 53.0, 52.1, 55.2, 51.9], ['2021-04-28', 53.0, 52.0, 53.0, 50.7], ['2021-04-29', 54.0, 55.7, 56.6, 53.4], ['2021-04-30', 55.0, 56.9, 57.2, 54.0], ['2021-05-01', 50.3, 55.1, 57.0, 50.2], ['2021-05-02', 54.2, 53.5, 54.7, 51.9], ['2021-05-03', 52.0, 51.2, 52.9, 50.5], ['2021-05-04', 51.1, 54.0, 54.6, 50.3]]
df = pd.DataFrame(data, columns = ['Date', 'Opening Price ($/MWh)', 'Close Price ($/MWh)', 'High Price ($/MWh)', 'Low Price ($/MWh)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($/MWh)'],
                high=df['High Price ($/MWh)'],
                low=df['Low Price ($/MWh)'],
                close=df['Close Price ($/MWh)'])])

fig.update_layout(title_text='Energy and Utilities Market Price Trend Analysis',
                  xaxis_rangeslider_visible=False,
                  yaxis_range=[min(df['Low Price ($/MWh)']), max(df['High Price ($/MWh)'])],
                  width=1200,
                  height=800,
                  font=dict(family='Courier New, monospace', size=20))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/25_202312270043.png')