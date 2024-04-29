
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Research", "Writing", "Editing", "Proofreading", "Publishing", "Distribution"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    marker = {"color": ["#006699","#339966","#996633","#CC9900","#CC6600","#FF9900"]},
    opacity = 0.7,
    textfont = {"size": 15},
))

fig.update_layout(
    title = "Publication of Social Sciences and Humanities Papers in 2020",
    font = {"family": "Times New Roman", "size": 16},
    margin = {'t': 150},
    width = 800,
    height = 800,
    showlegend = True,
    legend = {"x": 0.8, "y": 0.2},
    yaxis = {"tickfont": {"size": 15}},
    xaxis = {"showgrid": True, "showline": True},
    hovermode = "closest"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/75.png")