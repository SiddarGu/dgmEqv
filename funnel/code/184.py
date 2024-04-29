
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Knowledge", "Understanding", "Engagement", "Participation", "Advocacy", "Mobilization"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    marker_color = ["#FF4F4F", "#FF8E4F", "#FFD24F", "#FFFF4F", "#CDF44F", "#89F44F"],
    textposition = "inside",
    textfont_size = 12,
    opacity = 0.7,
    hoverinfo = "text"
))

fig.update_layout(
    title = "Citizen Involvement in Government and Public Policy in 2021",
    font_family = "Times New Roman",
    showlegend = False,
    paper_bgcolor = "#FFFFFF",
    plot_bgcolor = "#FFFFFF",
    width = 800,
    height = 600,
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/22.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/22.png")