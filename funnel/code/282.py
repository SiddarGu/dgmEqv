
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    name="Enrollment Growth in Education Sector in 2021",
    y=["Inquiry", "Admissions", "Testing", "Orientation", "Registration", "Others"],
    x=[500, 400, 300, 200, 100, 50],
    textposition="inside",
    textinfo="value+percent initial",
))

fig.update_layout(
    title="Enrollment Growth in Education Sector in 2021",
    font=dict(size=14),
    showlegend=True,
    width=1000,
    height=1000
)

fig.update_xaxes(title_text="Number of Students")
fig.update_yaxes(title_text="Stage")

pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/137.png")