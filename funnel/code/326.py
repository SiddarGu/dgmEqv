
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y=['Planting', 'Growing', 'Harvesting', 'Processing', 'Marketing'],
    x=[5000, 4500, 3500, 2500, 1500],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.7,
    marker_color='royalblue')])

fig.update_layout(
    title_text="Agriculture and Food Production - A Statistical View in 2020",
    font=dict(
        family="Courier New, monospace",
        size=10,
        color="#7f7f7f"
    ),
    plot_bgcolor='#E5E5E5',
    paper_bgcolor='#E5E5E5',
    autosize=True,
    margin=dict(
        l=10,
        r=10,
        t=50,
        b=50
    ),
    legend_orientation="h",
    legend=dict(x=0.5, y=-0.2),
)

fig.write_image("../png/7.png")
pio.write_image(fig, "../png/7.png")