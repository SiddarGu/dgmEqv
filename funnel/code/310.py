
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()

fig.add_trace(go.Funnel(
    # name="Real Estate Transactions in the Housing Market in 2021",
    y = ["Prospecting", "Researching", "Consulting", "Offering", "Negotiating", "Closing"],
    x = [30.4, 20.2, 10.1, 6.2, 3.1, 1.5],
    textinfo="value+percent initial",
    marker_color='deeppink',
    textposition="inside",
))

fig.update_layout(
    title="Real Estate Transactions in the Housing Market in 2021",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=False,
    legend_orientation="h",
    legend=dict(x=0.1, y=1.1),
    margin=dict(l=20, r=20, t=50, b=20),
    width=800,
    height=600
)

fig.write_image("../png/26.png")