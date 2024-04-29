
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["English Literature", "History", "Geography", "Psychology", "Sociology", "Others"],
    x = [1200, 1000, 800, 600, 400, 200],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["#0083FE", "#0051FF", "#4F00FF", "#A200FF", "#E100FF", "#FF00ED"]},
))

fig.update_layout(
    title = {"text": "Academic Book Distribution for Social Sciences and Humanities in 2019", "y":0.9, "x":0.5, "xanchor": "center", "yanchor": "top"},
    font=dict(
        size=14
    )
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/29.png", width=1500, height=1000, scale=2)