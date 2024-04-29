
import plotly.graph_objects as go   
fig = go.Figure(go.Funnel(
    y = ["Inquiry","Application","Admission","Enrollment","Graduation"],
    x = [1000,800,600,400,200],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont = dict(size=12),
    marker = dict(
        color = "royalblue",
        line = dict(color = "royalblue", width = 2)),
    opacity = 0.65))
fig.update_layout(
    title = "Student Journey in Education and Academics in 2020",
    width = 800,
    height = 500,
    showlegend = False,
    margin = dict(t=50, l=50, r=50, b=50))
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/89.png")