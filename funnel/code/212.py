
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Design","Production","Quality Control","Packaging","Delivery","Installation"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    marker_line_color="darkblue",
    marker_line_width=3,
))

fig.update_layout(
    title={"text":"Manufacturing and Production Process in 2021"},
    showlegend=False,
    paper_bgcolor="lavender",
    plot_bgcolor="whitesmoke",
    font_family="Merriweather Sans",
    margin={"t":20},
    height=600
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/6.png")