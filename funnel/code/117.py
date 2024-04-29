
import plotly.graph_objects as go

fig = go.Figure(data=[go.Funnel(
    y=["Research", "Development", "Testing", "Production", "Delivery"],
    x=[1000, 800, 650, 450, 200],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.8,
    marker=dict(
        color="orange",
    )
)])

fig.update_layout(
    title=go.layout.Title(text="Progress in Science and Engineering Projects in 2021",
                          font=dict(family="Georgia, serif")),
    font=dict(family="Georgia, serif"),
    legend_orientation="h",
    legend=dict(x=0.4, y=1, traceorder="normal",
                font=dict(family="Georgia, serif")),
    margin=dict(l=0, r=0, t=50, b=50),
    paper_bgcolor="white",
    plot_bgcolor="white",
    width=800,
    height=600,
    showlegend=True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/64.png")