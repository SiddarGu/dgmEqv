
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Enrollment", "Orientation", "Course Selection", "First Semester", "End of Year Exam", "Graduation"],
    x = [1000, 900, 800, 700, 600, 500],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont_size = 10,
    opacity = 0.8))

fig.update_layout(
    title = "Academic Progress of Students in Education System in 2020",
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)",
    font_family = "Times New Roman",
    width = 1000,
    height = 600,
    margin = dict(l=50, r=50, t=50, b=50),
    legend_orientation = "h"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/39.png")