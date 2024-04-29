
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Candlestick(x=['2019-08-11','2019-08-12','2019-08-13','2019-08-14','2019-08-15','2019-08-16','2019-08-17'],
                                     open=[70.5,75.2,76.9,73.5,71.9,74,75],
                                     high=[77.2,79.1,77.9,74.7,76.1,75.7,75.5],
                                     low=[66.8,71.6,71.1,70.4,68.3,70.2,71.7],
                                     close=[75,78.5,72.1,72.2,74.3,75.1,72.9])])

fig.update_layout(title_text='Stock Performance of Transportation and Logistics Company - Weekly Overview',
                  width=1200,
                  height=800,
                  yaxis_range=[66.8, 79.1])

fig.update_layout(
    autosize=False,
    width=1200,
    height=800,
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="#7f7f7f"
    )
)

pio.write_image(fig, '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/41_202312252244.png')