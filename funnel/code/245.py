
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [100000, 80000, 60000, 40000, 20000, 16000],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["#f8f325", "#f9f871", "#f3f8e7", "#ddf8f4", "#b7f8ed", "#aaf8f4"]},
))

fig.update_layout(
    title = "Food and Beverage Industry Growth in 2020",
    showlegend = True,
    autosize = True,
    width = 700,
    height = 500,
    margin = dict(l=0, r=0, t=50, b=0),
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)",
    font=dict(family="arial")
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/105.png")