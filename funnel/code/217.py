
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Visiting Website","Signing Up","Downloading App","Subscribing","Making Purchases","Others"],
    x = [3000,2000,1500,1000,500,250],
    textinfo = "value+percent initial",
    textposition = "outside",
    marker = dict(
        color = ["#7FCE55","#6D8CC7","#FFCA2F","#F18D9E","#D6C3E6","#9E9E9E"],
        line = dict(
            color = "white",
            width = 1.5
        ),
    ),
    opacity = 0.8,
    connector = dict(
        line = dict(
            color = "white",
            width = 1.5
        ),
    )
))

fig.update_layout(
    title = {"text":"Online Engagement - Social Media and the Web in 2021",
             "y":0.95,
             "x":0.5,
             "xanchor":"center",
             "yanchor":"top"},
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    font = dict(
        family = "Noto Sans",
        size = 12,
        color = "#212121"
    ),
    autosize = False,
    width = 800,
    height = 600,
    margin = dict(
        l = 0,
        r = 0,
        b = 0,
        t = 50,
        pad = 4
    ),
    legend = dict(
        x = 0.8,
        y = 1
    ),
    showlegend = True
)

fig.write_image("../png/217.png")