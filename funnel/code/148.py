
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Seeding","Planting","Fertilizing","Harvesting","Processing","Packaging"],
    x = [1000,800,600,400,200,100],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker = dict(
        color = ["#0092FF", "#FF9200","#1FDD1F","#FF6D6D","#006CFF","#B45F04"],
        line = dict(width = 0.5, color = "#000000")
    ),
    opacity = 0.8,
    connector = {"line":{"color":"#000000","dash":"dot","width":1.2}}
)])

fig.update_layout(
    title = "Food Production in Agriculture Sector in 2020",
    font = dict(family="sans-serif", size=12),
    xaxis = dict(showgrid=True, gridwidth=2, gridcolor="#F2F2F2"),
    yaxis = dict(showgrid=True, gridwidth=2, gridcolor="#F2F2F2"),
    width = 900,
    height = 600
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/136.png")