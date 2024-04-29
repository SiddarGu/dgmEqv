
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y=["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x=[1000, 800, 600, 400, 200, 160],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.65,
    marker=dict(
    color="royalblue",
    line=dict(
        color="royalblue",
        width=2
    )
))])

fig.update_layout(
    title="User Engagement - Social Media and the Web in 2020",
    showlegend=False,
    autosize=False,
    width=1000,
    height=600,
    margin=dict(l=20, r=20, t=50, b=20),
    paper_bgcolor="LightSteelBlue",
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/24.png")