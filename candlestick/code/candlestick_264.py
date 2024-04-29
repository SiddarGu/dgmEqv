
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Candlestick(x=['2019-04-26','2019-04-27','2019-04-28','2019-04-29','2019-04-30'],
                    open=[100.5,103,103,104,105],
                    high=[104.2,105.2,103,106.6,107.2],
                    low=[99.8,101.9,100.7,103.4,104],
                    close=[102,102.1,102,105.7,106.9])])

fig.update_layout(title_text='Tourism and Hospitality Stock Performance - Week Overview',
                  width=1000,height=800,
                  yaxis_range=[99.8,107.2],
                  font=dict(family='Helvetica', size=18, color='#7f7f7f'))
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/35_202312252244.png')