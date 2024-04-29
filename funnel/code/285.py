
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Intake", "Investigation", "Pre-trial","Trial","Resolution"],
    x = [1000, 800, 600, 400, 200],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.7,
    marker=dict(
        color=["deepskyblue","royalblue","mediumblue","darkblue","navy"],
    ),
))

fig.update_layout(
    title = {"text": "Resolution of Legal Cases in Law and Legal Affairs in 2020",
            "x":0.5,
            "y":0.96,
            "xanchor": "center",
            "yanchor": "top"},
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    legend=dict(
        x=1.0,
        y=1.0,
    ),
    autosize=False,
    width=800,
    height=600,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=True,
    margin=dict(l=20, r=20, t=50, b=30),
)

fig.write_image("../png/145.png")