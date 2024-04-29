
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y=["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x=[100000, 80000, 60000, 40000, 20000, 16000],
    textinfo="value+percent initial",
))
fig.update_layout(
    title="User Engagement on Social Media and the Web in 2021",
    font=dict(family='Courier New, monospace', size=12, color='black'),
    width=1000,
    height=800,
    legend=dict(
        x=1,
        y=0.5
    ),
    margin=dict(l=20, r=20, t=50, b=20),
    paper_bgcolor="LightSteelBlue",
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/17.png")