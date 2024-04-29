
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Candlestick(x=['2019-05-15','2019-05-22','2019-05-29','2019-06-05','2019-06-12','2019-06-19','2019-06-26'], open=[20.5, 20.8, 19.5, 19.5, 19.5, 20.2, 20.7], high=[21.2, 22.9, 19.6, 21.2, 21.5, 20.8, 22], low=[18.8, 20.2, 17.2, 19, 18.4, 18.7, 20.2], close=[19.5, 22, 18, 20.5, 20.8, 19.7, 21.2])])
fig.update_layout(title_text='Financial Trend of Arts and Culture Industry - Weekly Overview', width=800, height=800, yaxis_range=[17,23], font=dict(family="Courier New, monospace", size=18, color="black"))
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/22_202312270043.png')