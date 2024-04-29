

import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Research","Design","Prototype","Testing","Finalization"],
    x = [100,80,60,40,20],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont_size = 20,
    opacity = 0.8,
    marker = {"line": {"width": [3, 3, 3, 3, 3],
                   "color": ["#000000",
                            "#000000",
                            "#000000",
                            "#000000",
                            "#000000"]}},
    connector = {"line": {"color": "#000000",
                         "dash": "solid",
                         "width": 3}}
))

fig.update_layout(
    title = {"text": "Science and Engineering Projects Development in 2021",
             "y":0.95,
             "x":0.5,
             "xanchor": "center",
             "yanchor": "top"},
    font = {"family":"Courier New, monospace"},
    margin = {"l":200, "r":200, "t":100, "b":100},
    width = 800,
    height = 500,
    showlegend = False
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/103.png")