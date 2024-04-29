

import plotly.graph_objects as go 
fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Online Ads","Social Media","Email","Events","Word of Mouth","Others"],
    x = [1000,800,600,400,200,100],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.9,
    marker = {"color": ['#0080FF','#00FFFF','#00FF00','#FFFF00','#FF8000','#FF0000']},
    name = "Stage"))
fig.update_layout(title = {"text": "Increasing Audience Engagement in Arts and Culture in 2021",
                          "y":0.9,
                          "x":0.5,
                          "xanchor": "center",
                          "yanchor": "top"},
                  font = {"family": "Times New Roman"},
                  width = 800,
                  height = 800,
                  showlegend = True,
                  legend = {'x': 0.7, 'y': 0.9},
                  margin = {"t":50, "b":50, "l":50, "r":50},
                  plot_bgcolor = "rgba(0,0,0,0)")

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/131.png")