

import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=1, specs=[[{"type": "funnel"}]])
fig.add_trace(go.Funnel(
    y = ["Research","Legislation","Referendum","Implementation","Monitoring","Evaluation"],
    x = [1000,800,550,400,150,90],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_color='darkslateblue',
    opacity=0.7,
    name="Projects"
))

fig.update_layout(
    title_text="Government and Public Policy Projects in 2021",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    showlegend=True,
    width=800,
    height=600,
    paper_bgcolor="LightSteelBlue"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/101.png")