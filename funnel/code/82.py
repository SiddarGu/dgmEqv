
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Enrollments", "Attendance", "Involvement", "Engagement", "Completion", "Graduation"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.8,
    marker_color = 'royalblue'
))

fig.update_layout(
    title = "Student Enrollment in Social Sciences and Humanities in 2020",
    font = dict(
        family = "Times New Roman"
    ),
    width = 800,
    height = 600,
    showlegend = False
)

fig.write_image("../png/37.png")
pio.write_image(fig, "../png/37.png")