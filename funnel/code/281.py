
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Knowledge", "Awareness", "Research", "Action", "Maintenance", "Improvement"],
    x = [900, 800, 700, 600, 500, 400], textinfo="value+percent initial", 
    marker_color='#2c2f73',
    opacity=0.8,
    marker={'line': {'color': '#2c2f73', 'width': 1.5 }})])

fig.update_layout(
    title_text="Environmental Sustainability - Promoting Engagement in 2020",
    font=dict(
        family="Courier New, monospace",
        size=10,
        color="#7f7f7f"),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=True,
    width=600,
    height=550,
    legend=dict(
        x=1.05,
        y=0.7,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=2
    )
)

fig.write_image("../png/12.png")