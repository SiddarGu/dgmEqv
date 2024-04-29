
import plotly.offline as pio
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Inquiry","Booking","Payment","Shipment","Delivery","Feedback"],
    x = [1000,800,620,400,220,160],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity=0.9,
    marker = {"color": ["#26abd2", "#f5a623", "#f8e71c", "#a4e608", "#83bb23", "#4dbb2f"]},
    connector = {"line": {"color": "#636363", "dash": "dot", "width": 4}}
))

fig.update_layout(
    title={
        'text': "Logistics and Transportation - Number of Trips in 2020",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font=dict(family="Droid Sans"),
    legend_orientation="h",
    legend=dict(x=0.5, y=1.1),
    margin={"l": 150, "r": 150, "t": 0, "b": 0},
    plot_bgcolor='white',
    paper_bgcolor='white',
    width=800,
    height=600,
    dragmode=False,
    showlegend=True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/32.png")