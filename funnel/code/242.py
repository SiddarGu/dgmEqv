
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

fig = make_subplots(
    rows=1, cols=1,
    specs=[[{"type": "funnel"}]],
    subplot_titles=("Employee Growth in Human Resources Management in 2021",)
)

fig.add_trace(
    go.Funnel(
        y = ["Recruitment","Interviewing","Hiring","Onboarding","Training","Retention","Promotion"],
        x = [100,90,80,70,60,50,40],
        textinfo = "value+percent initial"
    ),
    row=1, col=1
)

fig.update_layout(
    showlegend=False,
    width=800,
    height=400,
    margin=dict(t=50, l=50, r=50, b=50),
    paper_bgcolor="white",
    plot_bgcolor="white",
    font=dict(
        family="Courier New, monospace",
        size=10,
        color="black"
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/123.png")