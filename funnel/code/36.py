
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["High School Diploma", "Associate Degree", "Bachelor's Degree", "Master's Degree", "Doctorate Degree"],
    x = [100, 80, 60, 40, 20],
    textinfo = "value+percent initial",
    orientation = "h",
    marker_color = 'darkblue'
))
fig.update_layout(
    title_text = 'Education Level in Social Sciences and Humanities in 2020',
    font = dict(
        size = 12
    )
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/20.png")