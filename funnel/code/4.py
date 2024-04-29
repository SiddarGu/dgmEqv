
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

fig = make_subplots(rows=1, cols=1, specs=[[{"type": "funnel"}]])

fig.add_trace(go.Funnel(
    name="Consumer Journey",
    y=["Exploration", "Research", "Comparison", "Decision", "Purchase","Use"],
    x=[3000, 2500, 2000, 1500, 1000, 500],
    textinfo="value+percent total",
    textposition="inside",
    textfont=dict(
        size=10,
    ),
    opacity=0.8,
    marker=dict(
        color='#F78F1E',
        line=dict(
            color='#F78F1E',
            width=2
        )
    )
))

fig.update_layout(
    title_text="Consumer Journey - Technology and the Internet in 2020",
    showlegend=True,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="#7f7f7f"
    ),
    width=800,
    height=800,
    margin=dict(l=20, r=20, t=50, b=20),
    hovermode="closest",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    autosize=False,
    template="plotly_dark"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-26_05-57-56_simulation_num50/png/34.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-26_05-57-56_simulation_num50/png/34.png")