
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [10000, 8000, 6000, 4000, 2000],
    textinfo = "value+percent initial",
    textfont_size = 17,
    opacity = 0.7,
    marker = {'color': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']},
    connector = {'line': {'color': '#e377c2', 'dash': 'solid', 'width': 3}}
))

fig.update_layout(
    title = {
        'text': "Health Improvement Plan - Healthcare and Health in 2020",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = dict(family = "Roboto", size = 18, color = "#7f7f7f"),
    legend = dict(orientation="h"),
    width = 1000,
    height = 800,
    showlegend = True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=300, r=300, t=50, b=50),
    xaxis_title="Number of Patients"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/144.png")