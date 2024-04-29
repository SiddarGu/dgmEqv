
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Freshman Enrollment", "Sophomore Enrollment", "Junior Enrollment", "Senior Enrollment", "Graduates"],
    x = [1000, 800, 600, 400, 200],
    textinfo = "value+percent initial",
    textposition = "inside",
))

fig.update_layout(title_text="Student Enrollment in Social Sciences and Humanities Courses in 2021")

fig.write_image("../png/75.png", scale=5, width=800, height=400)