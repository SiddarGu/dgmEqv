
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(
    data=[go.Funnel(
        y=["Pre-screening", "Diagnosis", "Treatment", "Follow-up", "Observation", "Recovery"],
        x=[1000, 800, 600, 400, 200, 100],
        textinfo="value+percent initial",
        marker=dict(color="royalblue"),
        opacity=0.75
    )],
    layout=go.Layout(
        title="Healthcare and Health - Patient Outcome in 2020",
        font=dict(size=12),
        legend=dict(x=0.7, y=1.1),
        width=800,
        height=600,
        margin=dict(l=50, r=50, b=50, t=50),
        paper_bgcolor="LightSteelBlue",
        showlegend=True,
        hovermode="closest"
    )
)

fig.update_layout(
    xaxis_showgrid=True,
    yaxis_showgrid=True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/42.png")