
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

fig = make_subplots(rows=1, cols=1, specs=[[{"type": "funnel"}]])
fig.add_trace(go.Funnel(
    y = ["Initial Screening", "Diagnosis", "Treatment", "Follow-up", "Discharge"],
    x = [100000, 90000, 70000, 50000, 30000],
    textinfo = "value+percent initial",
    textposition = "inside",
    texttemplate = "<b>%{text}</b><br>%{value}<br>%{percentInitial}",
    marker_color = "royalblue"),
    row=1, col=1
)
fig.update_layout(
    title="Healthcare and Health Outcomes in 2020",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    showlegend=True,
    legend_orientation="h",
    legend=dict(x=0.1, y=1.1)
)
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_layout(width=800, height=600, margin=dict(l=100, r=100, t=100, b=100))
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/186.png")