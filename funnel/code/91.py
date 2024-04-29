
import plotly.graph_objects as go
from plotly.offline import plot

labels = ['Research and Development','Design and Engineering','Production','Quality Assurance','Shipping','Others']
values = [1000,800,600,400,200,100]

fig = go.Figure(go.Funnel(
    name = "Process Optimization in Manufacturing and Production in 2021",
    y = labels, 
    x = values,
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_color = '#1f77b4',
))

fig.update_layout(
    title = {"text":"Process Optimization in Manufacturing and Production in 2021"}, 
    width = 1300,
    height = 800,
    plot_bgcolor = "white",
    paper_bgcolor = "white",
    font = dict(
        family = "Times New Roman",
        color = '#000000'
    ),
    margin = {'t':30},
    showlegend = True
)

fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/6.png')