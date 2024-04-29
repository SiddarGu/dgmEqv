
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Education", "Actions", "Practices", "Awareness", "Global Commitment", "Change"],
    x = [1000, 800, 500, 300, 100, 50],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["royalblue", "mediumslateblue", "indigo", "dodgerblue", "lightsteelblue", "lightskyblue"]},
    connector = {"line":{"color":"royalblue", "dash":"dot", "width":3}}
))

fig.update_layout(
    title = {"text":"Encouraging Sustainable Living - Global Community in 2021"},
    font = {"color":"black", "family":"Calibri"},
    xaxis = {"showgrid":True, "showline":False, "zeroline":False},
    yaxis = {"showgrid":True, "showline":False, "zeroline":False},
    shapes = [{"type":"rect", "x0":0, "y0":0, "x1":1, "y1":1, "fillcolor":"LightGrey", "opacity":0.4, "layer":"below"}],
    width = 800,
    height = 800,
    margin = {"t":100, "b":100}
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/56.png")