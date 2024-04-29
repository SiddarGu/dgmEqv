
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x = [1000,800,600,400,200,160],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    connector = {"line":{"color":"rgb(63, 63, 63)"}}
))

fig.update_layout(
    title = {"text": "Donor Engagement - Charity and Nonprofit Organizations in 2021", "y":0.9, "x":0.5, "xanchor":"center", "yanchor":"top"},
    font = dict(family = "Courier New, monospace", size = 12, color = "#7f7f7f")
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/35.png", width=1000, height=1000, scale=2)