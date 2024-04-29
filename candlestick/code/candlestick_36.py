
import plotly.graph_objects as go
import plotly.io as pio

candlestick = go.Candlestick(
    x=['2020-08-05', '2020-08-12', '2020-08-19', '2020-08-26', '2020-09-02', '2020-09-09', '2020-09-16', '2020-09-23'],
    open=[25.7, 27, 24.1, 24.4, 26.6, 25.3, 24.1, 26.6],
    high=[26.4, 27.2, 26.3, 27.9, 27.2, 26.2, 27.8, 27.7],
    low=[23.1, 23.6, 23.2, 23.5, 25.3, 23.8, 23.6, 24.9],
    close=[24.3, 24.2, 25.5, 26.8, 26.4, 24.9, 27.4, 26.1]
)

fig = go.Figure(data=[candlestick])

fig.update_layout(
    title="Trends of Academic Financing Over Time",
    xaxis_title="Date",
    yaxis_title="Price ($)",
    yaxis_range=[23.1, 27.9],
    width=940,
    height=500,
    font_size=10,
    template='plotly_white'
)

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/19_202312252244.png")