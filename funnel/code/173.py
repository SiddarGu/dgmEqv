
import plotly.graph_objects as go 
fig = go.Figure(go.Funnel(
    y = ["Planting","Harvesting","Processing","Packaging","Shipping","Retail"],
    x = [1000,800,600,400,200,100],
    textinfo = "value+percent initial",
    opacity = 0.8,
    marker_color = '#f7f1e3',
    textposition = "inside",
    textfont_size = 12
))
fig.update_layout(
    title = {
        'text':"Agricultural Productivity - Food Production in 2020",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = {
        'family':"Courier New, monospace",
        'size':14
    },
    shapes=[
        dict(
            type="rect",
            xref="paper",
            yref="paper",
            x0=0,
            y0=0,
            x1=1,
            y1=1,
            line_width=2,
        )
    ],
    showlegend = False,
    width = 800,
    height = 800,
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/183.png")