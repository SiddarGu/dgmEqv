

import plotly.graph_objects as go
import plotly.io as pio

labels = ['Symptoms Observation','Diagnostic Tests','Diagnosis','Treatment','Follow-up','Recovery']
values = [20000, 18000, 15000, 10000, 5000, 2500]

fig = go.Figure(data=[go.Funnel(
    y=labels, 
    x=values,
    textinfo="value+percent initial",
    marker_color='royalblue',
    opacity=0.8
)])

fig.update_layout(
    title_text="Healthcare Journey - Healthcare and Health in 2021",
    font=dict(
        size=14,
        family='Courier New, monospace'
    ),
    width=800,
    height=600,
    xaxis_title="Number of Patients",
    yaxis_title="Stage",
    showlegend=False,
    margin=dict(l=200, r=50, t=80, b=100)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/3.png")