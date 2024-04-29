
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo="value+percent initial",
    marker = {"color": ["#00AB66", "#F8D51C", "#F68B2F", "#F14D4D", "#9F2A9D", "#5B1F6B"]},
    opacity = 0.7,
    orientation = "h",
))

fig.update_layout(
    title="Social Media and Web Engagement in 2020",
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        family="sans-serif",
        color="#424242"
    ),
    height=800,
    width=1000,
    legend_orientation="h",
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=0
    ),
    showlegend=True
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/30.png")