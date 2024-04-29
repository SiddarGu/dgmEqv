
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Raw Material", "Assembly", "Quality Control", "Packaging", "Shipping", "Others"],
    x = [1000, 800, 600, 400, 200, 160],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.8,
    marker = {"color": ["royalblue", "crimson", "green", "darkorange", "lightseagreen", "mediumpurple"]},
    connector = {"line":{"color":"royalblue", "dash": "dot", "width": 3}}
))

fig.update_layout(
    title = {
        "text": "Manufacturing and Production Output in 2020",
        "y": 0.9,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top"
    },
    font = dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    legend = dict(x=0.1, y=0.03),
    plot_bgcolor = 'rgb(243, 243, 243)',
    paper_bgcolor = 'rgb(243, 243, 243)',
    height = 650,
    width = 650,
    margin = dict(l=50, r=50, b=50, t=50, pad=4)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/6.png")