
import plotly.graph_objects as go
import plotly.io as pio

data = [go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000,888,666,462,228],
    textinfo = "value+percent initial",
    marker = {"color": ["#9A9A9A", "#FFC300", "#FFC300", "#FFC300", "#FFC300"]},
    opacity = 0.7,
    connector = {"line":{"color":"rgb(63, 63, 63)", "dash":"solid"}}
)]

fig = go.Figure(data=data)
fig.update_layout(
    title={"text": "Delivery Growth in Transportation and Logistics in 2021",
           "y": 0.95,
           "x": 0.5,
           "xanchor": "center",
           "yanchor": "top"},
    font = {"family": "Helvetica"},
    legend_orientation="h",
    legend=dict(x=0, y=1.2, traceorder="normal"),
    paper_bgcolor="white",
    plot_bgcolor="white",
    showlegend=True,
    height=600,
    width=600,
    margin=dict(l=20, r=20, t=100, b=40),
    hovermode="closest",
    xaxis=dict(showgrid=False, zeroline=False),
    yaxis=dict(showgrid=False, zeroline=False)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/49.png")