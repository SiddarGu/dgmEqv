
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "browser"

data = [['2019-05-01',160,150,170,150],
        ['2019-05-08',150,170,175,145],
        ['2019-05-15',170,165,178,165],
        ['2019-05-22',160,150,175,150],
        ['2019-05-29',140,170,176,140]]
fig = go.Figure(data=[go.Candlestick(x=[d[0] for d in data],
                    open=[d[1] for d in data],
                    close=[d[2] for d in data],
                    high=[d[3] for d in data],
                    low=[d[4] for d in data])])
fig.update_layout(title='Financial Expenditure on Social Sciences and Humanities - Trends Overview',
                  yaxis_range=[min([d[4] for d in data]), max([d[3] for d in data])],
                  width=800,
                  height=700,
                  font=dict(family="Arial"))
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/39_202312252244.png")