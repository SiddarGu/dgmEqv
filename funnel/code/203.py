
import plotly.graph_objects as go

fig = go.Figure(data=[go.Funnel(
    y = ["Research", "Development", "Testing", "Production", "Maintenance", "Others"],
    x = [1000, 800, 600, 400, 200, 160], 
    textinfo = "value+percent initial",
    marker = {'color': ['#d6d6d6', '#f2f2f2', '#fdb8c0', '#fddbc7', '#c0c0c0', '#ffd9b3']},
    opacity = 0.6,
    connector = {"line":{"color":"#000000"}},
)])

fig.update_layout(
    title =  "Science and Engineering Advancement in 2021",
    font = {"family": "Times New Roman", "size": 14},
    autosize = False,
    width = 1000, 
    height = 600
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/45.png")