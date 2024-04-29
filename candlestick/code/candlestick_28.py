
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Candlestick(x=['2019-04-26','2019-04-27','2019-04-28','2019-04-29','2019-04-30'],
                open=[90.5,93,93,94,95],
                high=[94.2,95.2,92,96.6,97.2],
                low=[87.8,91.9,90.7,93.4,94],
                close=[92,92.1,92,95.7,96.9])])

fig.update_layout(title_text='Market Performance of Social Media and the Web Stocks - Weekly Overview', width=800, height=600, yaxis_range=[87.8,97.2])
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/48_202312252244.png')