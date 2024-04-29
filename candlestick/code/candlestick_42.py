
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame({'Date': ['2020-06-01', '2020-06-08', '2020-06-15', '2020-06-22', '2020-06-29', '2020-07-06', '2020-07-13'],
                   'Opening Price ($)': [20.6, 22.7, 22, 24.5, 23.4, 25.6, 27.5],
                   'Closing Price ($)': [22.3, 22.2, 24, 23.7, 26.3, 27.9, 26.2],
                   'High Price ($)': [23.4, 24.5, 25.3, 25.8, 26.7, 28, 28.1],
                   'Low Price ($)': [19, 19.9, 20.8, 21.2, 22.4, 24.7, 24.3]})

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                       open=df['Opening Price ($)'],
                       high=df['High Price ($)'],
                       low=df['Low Price ($)'],
                       close=df['Closing Price ($)'])])
fig.update_layout(title_text='Science and Engineering Stock Price Change Overview',
                  yaxis_range=[18, 29],
                  width=800,
                  height=400,
                  font=dict(size=12))
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/9_202312270043.png')