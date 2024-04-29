
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Recruitment","Training","Performance Evaluation","Retention","Termination"],
    x = [1000,800,600,400,200],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_color = "royalblue",
    opacity = 0.7,
    marker = {"line": {"color": "darkblue", "width": 3}}))

fig.update_layout(
    title = {"text": "Employee Management in Human Resources in 2021"},
    font = {"family": "Courier New, monospace", "size": 15},
    margin = {"l": 250, "r": 250, "t": 100, "b": 100},
    width = 1000,
    height = 800,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/54.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/54.png")