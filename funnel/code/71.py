
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Enrollment","Orientation","Course Selection","Classes","Exams","Graduation"],
    x = [100000,80000,70000,50000,30000,10000],
    textinfo = "value+percent initial",
    textfont_size = 15,
    marker = {"color": ["#AFE4EA","#87C2D7","#77B2C9","#4D90B9","#2D6799","#004F79"]},
    opacity = 0.9,
    connector = {"line":{"color":"rgba(63, 63, 63, 0.3)"}}
))
fig.update_layout(
    width = 900,
    height = 600,
    title = {"text":"Education Level Achievement in Academic Institutions in 2020",
             "y":0.9,
             "x":0.5,
             "xanchor":"center",
             "yanchor":"top"},
    font = {"family":"Times New Roman","size":15},
    legend_orientation = "h"
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/91.png")