
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [1000, 800, 600, 400, 200, 160],
    textinfo = "value+percent initial",
    textposition = "inside",
    hoverinfo = "y+x",
    marker_color = 'skyblue'
))

fig.update_layout(
    title = {"text": "Shopping Funnel in Retail and E-commerce in 2020",
            "y": 0.9,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top"},
    font = {"family": "Times New Roman"},
    autosize = False,
    width = 800,
    height = 500,
    margin = {"t": 50, "b": 0, "l": 0, "r": 0},
    showlegend = False,
    xaxis = {"showgrid": True},
    yaxis = {"showgrid": True},
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/133.png")