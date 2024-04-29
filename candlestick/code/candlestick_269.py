
import plotly.graph_objects as go
import plotly.io as pio

x = ['2019-04-26', '2019-04-27', '2019-04-28', '2019-04-29', '2019-04-30', '2019-05-01', '2019-05-02', '2019-05-03', '2019-05-04', '2019-05-05']
open_data = [50.5, 53, 53, 54, 55, 56, 58, 56, 59, 60]
close_data = [52, 52.1, 52, 55.7, 56.9, 58.2, 57.5, 60.7, 61.9, 60.8]
high_data = [54.2, 55.2, 53, 56.6, 57.2, 59.7, 59.5, 62.2, 63.2, 62.4]
low_data = [49.8, 51.9, 50.7, 53.4, 54, 55.3, 54.3, 54.5, 57.5, 59]

fig = go.Figure(data=[go.Candlestick(x=x, open=open_data, high=high_data, low=low_data, close=close_data)])
fig.update_layout(title='Healthcare and Health Stock Trend - Week Overview', width=800, height=500, yaxis_range=[min(low_data)-2, max(high_data)+2], font=dict(family='Courier New, monospace', size=18, color='#000000'))
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/40_202312252244.png')