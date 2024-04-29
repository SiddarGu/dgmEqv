
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Purchase", "Repeat Purchase"],
    x = [10000, 8000, 7000, 6000, 3000, 2000],
    textinfo = "value",
    orientation = "h"
))

fig.update_layout(
    title = {
        'text': "Customer Journey in Retail and E-commerce in 2021",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(family="Times New Roman"),
    width = 1000,
    height = 800,
    showlegend=True,
    xaxis_title = "Number of Customers",
    yaxis_title = "Stage",
    paper_bgcolor="LightSteelBlue"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/19.png")