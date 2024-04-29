
import plotly.graph_objs as go
import plotly.io as pio

fig = go.Figure()

fig.add_trace(go.Funnel(
    y = ["Promotion", "Ticket Purchase", "Event Attendance", "Post-Event Survey", "Follow-Up Survey"],
    x = [1000, 800, 500, 300, 100],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.7,
    marker_color = "mediumseagreen"
))

fig.update_layout(
    title_text = "Sports and Entertainment Event Attendance in 2021",
    font = dict(
        size = 16
    ),
    legend_font = dict(
        size = 12
    ),
    width = 800,
    height = 800,
    showlegend = True,
    legend_orientation="h",
    legend=dict(x=-.1, y=1.2)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/5.png")