
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Recruitment", "Interview", "Offer", "On-Boarding", "Training", "Retention"],
    x = [1000, 800, 600, 400, 200, 150],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.65,
    marker_color="royalblue"
))

fig.update_layout(
    title = "Employee Management in Human Resources - 20XX",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    yaxis_title="Employee Stages",
    xaxis_title="Number of Employees",
    width=1000,
    height=750,
    showlegend=False,
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightSkyBlue')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightSkyBlue')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/85.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/85.png")