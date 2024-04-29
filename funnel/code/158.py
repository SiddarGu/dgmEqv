
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

fig = make_subplots(
    rows=1, cols=1,
    specs=[[{"type": "funnel"}]],
    subplot_titles=["Legal Cases in Law and Legal Affairs in 2021"]
)

fig.add_trace(go.Funnel(
    y=["Initial Inquiry", "Feasibility Study", 
       "Project Planning", "Implementation", "Operation"],
    x=[1000, 900, 700, 500, 300],
    textinfo="value+percent initial",
    textposition="inside",
    marker_color="royalblue"
))

fig.update_layout(
    showlegend=False,
    paper_bgcolor="white",
    plot_bgcolor="white",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    width=800,
    height=800
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/156.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/156.png")