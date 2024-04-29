
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Contact", "Engagement", "Retention", "Advocacy", "Conversion"],
    x = [1000, 880, 660, 420, 220],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_color = "dodgerblue",
    opacity = 0.6
))

fig.update_layout(
    title = "Social Media and Web User Engagement in 2020",
    showlegend = False,
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    width = 800,
    height = 800,
    font = dict(
        size = 15,
        color = "#000000"
    )
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/161.png")