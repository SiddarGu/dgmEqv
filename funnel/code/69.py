
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y=["Inquiry", "Quotation", "Negotiation", "Order Placed", "Manufacturing", "Delivery"],
    x=[1000, 800, 600, 400, 200, 100],
    textposition="inside",
    textinfo="value+percent initial+percent previous",
))

fig.update_layout(
    title={"text": "Manufacturing and Production Orders in 2021"},
    font={"family": "Times New Roman"},
    legend_orientation="h",
    legend=dict(x=0.3, y=1.1),
    margin=dict(l=20, r=20, t=50, b=20),
    width=800,
    height=600,
    paper_bgcolor="LightSteelBlue",
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/9.png")