
import plotly.graph_objects as go
from plotly.io import write_image

fig = go.Figure()

fig.add_trace(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [10000, 8000, 6000, 4000, 2000, 1600],
    textinfo = "value+percent initial",
    textposition="inside",
    opacity=0.65,
    marker = {"color": ["deepskyblue", "royalblue", "mediumpurple", "orchid", "violet", "plum"]}
))

fig.update_layout(
    title={"text":"Consumer Engagement - Sports and Entertainment in 2021",
            "y":0.95,
            "x":0.5,
            "xanchor":"center",
            "yanchor":"top"},
    font=dict(
        family="sans-serif",
        size=10,
        color="black"
    ),
    width=800,
    height=600,
    showlegend=False,
    bargap=0.2,
    bargroupgap=0.1
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/5.png")