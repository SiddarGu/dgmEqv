
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Awareness", "Research", "Interest", "Consideration", "Intent", "Donation"],
    x = [1000, 800, 600, 400, 200, 100], 
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.65, 
    marker_color='darkblue'))

fig.update_layout(
    title=go.layout.Title(
        text="Donor Journey in Charity and Nonprofit Organizations in 2020",
        y=0.9,
        x=0.5,
        xanchor="center",
        yanchor="top"
    ),
    font=dict(family="Courier New, monospace"),
    width=800,
    height=600,
    margin=go.layout.Margin(
        l=50,
        r=50,
        b=50,
        t=50,
        pad=4
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/120.png")