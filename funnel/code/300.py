
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Inquiry", "Research", "Booking", "Arrive", "Departure"],
    x = [1000, 800, 500, 300, 100],
    textinfo="value+percent initial",
    opacity=0.8,
    marker=dict(
        color="MediumPurple",
        line=dict(color="MediumPurple", width=3)
    )
)])

fig.update_layout(
    title_text="Tracking Tourist Flow in Tourism and Hospitality Industry in 2020",
    font=dict(
        family="Helvetica",
        size=16,
    ),
    showlegend=False,
    width=800,
    height=600,
    margin=dict(t=60, l=60, r=60, b=60),
    paper_bgcolor="LightSteelBlue",
    plot_bgcolor="white"
)

fig.write_image("../png/15.png")
pio.write_image(fig, "../png/15.png")