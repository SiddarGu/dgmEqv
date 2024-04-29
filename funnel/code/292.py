
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Discovery","Research","Comparison","Purchase","Follow Up","Loyalty"],
    x = [1000,800,600,400,200,150],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["#30A66B","#14BBF9","#F2BD30","#F1C43F","#D36FF3","#A926F5"]},
    connector = {"line":{"color":"rgba(255,255,255,0.5)"},
                 "visible":True}
))

fig.update_layout(
    title = {"text":"Customer Journey in Retail and E-commerce in 2021"},
    legend=dict(
        x=0.5,
        y=0.95,
    ),
    font = {"family":"Calibri", "size":8},
    plot_bgcolor = 'rgba(245, 246, 249, 1)',
    paper_bgcolor = 'rgba(245, 246, 249, 1)',
    height = 500,
    width = 800,
    margin = {"b":40, "l":60, "r":60, "t":50},
    # showlegend = False,
    # xaxis = {"showgrid":False},
    # yaxis = {"showgrid":False}
)

fig.write_image("../png/41.png")