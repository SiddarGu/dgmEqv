
import plotly.graph_objects as go
import plotly.io as pio

data = {'Stage': ['Awareness', 'Consideration', 'Intent', 'Purchase', 'Post-purchase', 'Others'], 
        'Number of Customers': [1000, 800, 650, 450, 200, 100]}

fig = go.Figure(data=[go.Funnel(
    y = data['Stage'],
    x = data['Number of Customers'],
    textinfo = "value+percent initial",
    marker_color = 'deepskyblue',
    opacity = 0.4
)])

fig.update_layout(
    title={
        'text': "E-commerce Funnel - Retail and E-commerce in 2020",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family="Calibri, monospace",
        size=18,
        color="#7f7f7f"
    ),
    paper_bgcolor='rgba(255,255,255,1)',
    width=800,
    height=800,
    showlegend=False,
    margin=dict(
        l=50,
        r=50,
        b=50,
        t=50,
        pad=4
    ),
    xaxis_title="Number of Customers",
    yaxis_title="Stage"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/133.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/133.png")