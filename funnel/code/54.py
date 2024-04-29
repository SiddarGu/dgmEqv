
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Enrolment","Orientation","Course Selection","Midterm","Final Exam","Certification"],
    x = [100000,80000,60000,40000,20000,15000],
    textinfo="value+percent initial",
    textposition="inside",
    textfont_size=14,
    marker=dict(
        color="royalblue",
        line=dict(color="mediumblue", width=2)
    ),
    opacity=0.7,
))

fig.update_layout(
    title="Academic Journey in Social Sciences and Humanities in 2020",
    font=dict(size=14),
    width=800,
    height=800,
    showlegend=False
)

pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/70.png")