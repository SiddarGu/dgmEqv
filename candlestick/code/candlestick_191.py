
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Candlestick(
    x=['2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10'],
    open=[45, 46, 50, 51, 59, 60, 63],
    high=[49, 50, 53, 55, 62, 63, 66],
    low=[43, 44, 48, 49, 58, 59, 62],
    close=[47, 48, 51, 53, 61, 62, 64]
)])

fig.update_layout(title_text='Financial Trend in Social Sciences and Humanities - Monthly Overview',
                  xaxis_title='Month',
                  yaxis_title='Price ($)',
                  yaxis_range=[40,70],
                  width=800,
                  height=600,
                  font=dict(family="Arial", size=12))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/36_202312252244.png')