
import plotly.graph_objects as go
import plotly.io as pio

stage = ["Inquiry","Quotation","Negotiation","Acceptance","Production","Delivery"]
number_of_order = [1000,800,600,400,200,100]

fig = go.Figure(go.Funnel(
    y = stage,
    x = number_of_order,
    textinfo="value+percent initial",
    textposition="inside",
    marker = dict(
        color = ["#f4f4f4","#f2f2f2","#f2f2f2","#f2f2f2","#f2f2f2","#f2f2f2"],
        line = dict(color="black", width=3),
    )
))

fig.update_layout(
    title = {
        'text': "Manufacturing and Production Trend in 2021",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    legend_orientation="h",
    legend=dict(x=0.15, y=-0.2),
    paper_bgcolor='#f4f4f4', 
    plot_bgcolor='#f4f4f4',
    font=dict(
        size=14
    ),
    width=800,
    height=400,
    margin=dict(
        l=50,
        r=50,
        b=50,
        t=80,
        pad=4
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/51.png")
pio.write_image(fig,"/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/51.png")