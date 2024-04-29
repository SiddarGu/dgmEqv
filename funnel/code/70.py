
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x = [1000,900,750,600,500,400],
    textinfo="value+percent initial",
    textposition="inside",
    opacity = 0.65,
    connector = {"line":{"color":"rgba(63, 63, 63, 0.7)"}},
))

fig.update_layout(
    title = {"text":"Environmental Sustainability Engagement in 2021", "yanchor":"top","xanchor":"center","x":0.5},
    legend_orientation="h",
    font=dict(family="Courier New, monospace", size=12, color="#7f7f7f"),
    width = 800,
    height = 800,
    autosize = False
)

pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/90.png")