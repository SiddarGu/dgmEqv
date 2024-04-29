
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x = [1000,800,600,400,200,160],
    textinfo = "value+percent initial",
    marker = dict(
        color = ["#636EFA","#EF553B","#00CC96","#AB63FA","#FFA15A","#19D3F3"],
        line = dict(color = "black", width = 1.5)
    ),
    textfont = dict(
        color = "black"
    ),
    opacity = 0.65
))

fig.update_layout(
    title = {"text": "Social Media and Web User Engagement in 2021", "y":0.9},
    width = 700,
    height = 600,
    showlegend = True,
    margin = {"r":20, "t":60, "l":20, "b":60},
    legend_orientation="h",
    legend = dict(x=0.9, y=1.1),
    paper_bgcolor = "white", 
    plot_bgcolor = "white"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/72.png")