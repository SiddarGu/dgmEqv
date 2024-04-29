
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [1000, 900, 700, 500, 300, 100],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.7,
    marker = {"line": {"width": 3, "color": "royalblue"}},
    connector = {"line": {"color": "royalblue", "dash": "dot", "width": 2}}
))

fig.update_layout(
    title = {"text": "Arts and Culture Engagement in 2021",
            "y": 0.9,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top"},
    showlegend = False,
    width = 800,
    height = 600,
    template = "plotly_white"
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/143.png")