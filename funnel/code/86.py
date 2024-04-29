
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Recruitment", "Screening", "Interviewing", "Selection", "Hiring", "Onboarding"],
    x = [100, 80, 60, 40, 20, 10],
    textinfo = "value+percent previous",
    textposition = "inside",
    opacity = 0.65, 
    marker = {"color": ["deepskyblue", "royalblue", "cornflowerblue", "lightsteelblue", "lightcyan", "paleturquoise"]},
    connector = {"line": {"color": "royalblue", "dash": "solid", "width": 3}}
))

fig.update_layout(
    title={"text":"Employee Management in Human Resources in 2020", "y":0.9, "x":0.5, "xanchor":"center", "yanchor":"top"},
    font={"family":"Arial"},
    autosize=True,
    showlegend=True,
    legend=dict(x=0.95, y=0.95, traceorder="normal"),
    width=1000,
    height=800
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/33.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/33.png")