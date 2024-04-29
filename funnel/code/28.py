
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Survey", "Research", "Analysis", "Development", "Deployment", "Maintenance"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = 'value+percent initial',
    textposition = "inside",
    orientation = "h",
    marker = {"color": ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3"]},
))

fig.update_layout(
    title = {
        'text': "Social Media and Web Adoption in 2021",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    legend_orientation="h",
    legend=dict(x=0.5, y=1.1),
    font=dict(
        family="Courier New, monospace",
        size=20,
        color="#7f7f7f"
    ),
    width=800,
    height=700,
    margin=dict(
        l=100,
        r=100,
        b=100,
        t=100,
        pad=4
    )
)

fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/30.png')