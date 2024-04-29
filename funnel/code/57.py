
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y=["Exposure", "Engagement", "Interest", "Consideration", "Conversion", "Retention"],
    x=[100000, 8000, 6000, 4000, 2000, 1600],
    orientation="h",
    marker_color="royalblue")
)
fig.update_layout(
    title="Social Media and Web Engagement in 2020",
    font=dict(
        size=12
    ),
    width=600,
    height=400,
    showlegend=False
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/72.png")