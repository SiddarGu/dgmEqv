
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y=["Design", "Research & Development", "Production", "Quality Control", "Delivery"],
    x=[100, 80, 60, 40, 20],
    textinfo="value+percent initial",
    textposition="inside",
    marker_color='deeppink',
    opacity=0.7
)])

fig.update_layout(
    title_text="Manufacturing and Production in 2021",
    showlegend=False,
    width=600,
    height=700,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/118.png')