
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [1000, 900, 800, 700, 600, 500],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"line": {"width": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
                "color": ["black","blue","red","yellow","green","violet"]}},
))

fig.update_layout(
    title = {"text": "Sports and Entertainment Participation in 2020",
            "y":0.9},
    showlegend = True,
    margin = {"l": 200, "r": 200, "t": 100, "b": 100},
    font = dict(
        family = "Courier New, monospace",
        size = 12,
        color = "#7f7f7f"
    ),
    template = "plotly_white",
    width = 800,
    height = 600,
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = 'rgba(0,0,0,0)',
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/5.png")