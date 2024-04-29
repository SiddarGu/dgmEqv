
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [3000,2500,2000,1500,1000,750],
    textinfo = "value+percent initial",
    textposition="inside",
    marker_color="royalblue",
    opacity=0.7,
    ))

fig.update_layout(
    title={"text": "Increasing Participation of Volunteers in Charity and Nonprofit Organizations in 2020",
           "y":0.98,
           "x":0.5,
           "xanchor": "center",
           "yanchor": "top"},
    font=dict(
        family="Courier New, monospace",
        size=10,
        color="#7f7f7f"
    ),
    legend=dict(
        x=1,
        y=1
    ),
    width=800,
    height=800,
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False
    ),
    margin = dict(l=100, r=50, t=80, b=100)
)

fig.write_image("../png/35.png")