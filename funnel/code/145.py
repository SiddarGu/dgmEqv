
import plotly.graph_objects as go
import plotly.io as pio
fig = go.Figure(go.Funnel(
    y = ["Recruitment", "Onboarding", "Training Program", "Performance Evaluation", "Retention", "Exit"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"line": {"width": [0, 0, 0, 0], "color": ["white"] * 4}},
))
fig.update_layout(
    title={"text": "Employee Management Strategies in Human Resources in 2020"},
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ),
    width=1000,
    height=800,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/129.png")