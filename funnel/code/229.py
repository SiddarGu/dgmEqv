
import plotly.graph_objects as go
import plotly.io as pio

# Data
Stage = ["Germination", "Cultivation", "Fertilization", "Harvest", "Processing", "Distribution"]
Number_of_Farms = [1000, 800, 600, 400, 200, 100]

# Create figure
fig = go.Figure(go.Funnel(
    y = Stage,
    x = Number_of_Farms,
    textinfo = "value+percent initial",
    marker = {'color': ['#d3d3d3', '#f4c430', '#f3722c', '#f8961e', '#f9c74f', '#90be6d']},
    opacity = 0.7,
))

# Style
fig.update_layout(
    title = {"text": "Agricultural Outputs in 2021", "y":0.95, "x":0.5, "xanchor": "center", "yanchor": "top"},
    font = {"family": "Courier New, monospace", "size": 12},
    width = 800,
    height = 800,
    showlegend = True,
    legend_orientation = "h",
    legend = dict(x=0.5, y=-0.1),
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = 'rgba(0,0,0,0)',
    xaxis = dict(showgrid = True, gridcolor = '#D3D3D3'),
    yaxis = dict(showgrid = True, gridcolor = '#D3D3D3')
)

# Saving figure
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/10.png")