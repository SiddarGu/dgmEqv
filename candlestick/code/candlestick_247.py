
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame([['2021-06-01', 43.5, 44.7, 45.8, 42],
                   ['2021-06-08', 45.4, 47.4, 48.2, 43.7],
                   ['2021-06-15', 47.2, 45.7, 48.5, 43.3],
                   ['2021-06-22', 45.8, 46.3, 47.4, 44.1],
                   ['2021-06-29', 45.2, 43.5, 45.5, 42.9]],
                  columns = ['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)']
                 )

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Opening Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)'],
    close=df['Closing Price ($)']
)])

fig.update_layout(title='Financial Trend in Agriculture and Food Production Market',
                  yaxis_range=[min(df['Low Price ($)']),max(df['High Price ($)'])],
                  width=800, height=800,
                  font=dict(family="Verdana, monospace"))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/6_202312270043.png')