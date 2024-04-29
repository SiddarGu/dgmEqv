
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Research", "Development", "Testing", "Iteration", "Finalization"],
    x = [100.0, 75.0, 50.0, 25.0, 15.0],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["royalblue", "crimson", "lightseagreen", "orange", "lightgrey"]},
    hoverinfo = "text",
    text = ["100.0%", "75.0%", "50.0%", "25.0%", "15.0%"]
))
fig.update_layout(
    title = {"text": "Scientific and Engineering Project Progression in 2021",
            "x": 0.5,
            "y": 0.9,
            "xanchor": "center",
            "yanchor": "top"},
    font = dict(size=14),
    legend = {"x": 0.02,
              "y": 0.98},
    width = 600,
    height = 600,
    margin = {"l": 50, "r": 50, "b": 50, "t": 50},
    paper_bgcolor="white",
    plot_bgcolor="white"
    )
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/25.png")