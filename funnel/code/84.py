
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Initial Consultation", "Diagnosis", "Treatment", "Follow-up", "Referral"],
    x = [100, 80, 60, 40, 20],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["royalblue", "crimson", "lightseagreen", "orange", "lightgrey"]},
    hoverinfo = "text+y",
    hoverlabel = {"bgcolor": "white", "font": {"size": 16}}
))

fig.update_layout(
    title_text = "Healthcare & Health - Patient Journey in 2020",
    title_x = 0.5,
    font = {"family": "Times New Roman"},
    width = 800,
    height = 650,
    showlegend = False,
    paper_bgcolor = "whitesmoke",
    margin = {"t":60, "b":60, "l":100, "r":100},
    xaxis_showgrid = False,
    yaxis_showgrid = False,
    hovermode = "x",
    hoverdistance = 20
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/42.png")