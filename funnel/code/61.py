
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x = [1000,800,600,400,200,160],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont_size = 12,
    opacity = 0.8,
    marker = {"color" : ["#ffd700","#e6beff","#f0b7a4","#f2f2f2","#87ceeb","#d3d3d3"]},
    connector = {"line":{"color":"#f2f2f2","dash":"solid","width":4}}
))

fig.update_layout(
    title = {"text":"Tourism and Hospitality - Funnel Chart in 2021","font":{"size": 14}},
    font = {"family": "Courier New, monospace", "size": 12},
    width = 800,
    height = 600,
    showlegend = False
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/8.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/8.png")