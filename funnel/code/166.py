
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y=["Knowledge", "Education", "Research", "Application", "Evaluation", "Others"],
    x=[1000, 800, 600, 400, 200, 100],
    textposition="inside",
    textinfo="value+percent initial"
))
fig.update_layout(
    title_text="Sustainable Development - Environment and Sustainability in 2020",
    font=dict(
        family="Courier New, monospace",
        size=10,
        color="#7f7f7f"
    ),
    width=800,
    height=600,
    paper_bgcolor="White",
    margin=dict(
        l=20,
        r=20,
        b=20,
        t=30,
        pad=4
    ),
    showlegend=False
)
fig.update_xaxes(showgrid=True, gridwidth=0.75, gridcolor='#DDDDDD')
fig.update_yaxes(showgrid=True, gridwidth=0.75, gridcolor='#DDDDDD')

pio.write_image(fig, "../png/169.png")