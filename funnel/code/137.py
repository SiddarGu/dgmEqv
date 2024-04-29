
import plotly.graph_objects as go
import plotly.io as pio
import random

stage_list = ["Introduction", "Consideration", "Intent", "Evaluation", "Purchase", "Retention", "Advocacy"]
number_of_customers_list = [100000, 88800, 73280, 61184, 49347, 40078, 32262]

fig = go.Figure(data=[go.Funnel(
    y=stage_list, x=number_of_customers_list, textinfo="value+percent initial",
    marker_color='#7EC0EE',
    opacity=0.7,
    textposition="inside",
    textfont_size=20
)])

fig.update_layout(
    title={
        'text': "Growth of Food and Beverage Industry in 2021",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family="Calibri",
        size=18,
    ),
    width=1000,
    height=700,
    legend_orientation="h",
    legend=dict(x=-.1, y=1.2),
    shapes=[dict(
        type="rect",
        xref="paper",
        yref="paper",
        x0=0,
        y0=0,
        x1=1,
        y1=1,
        line=dict(
            width=2,
        ),
    )],

)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/99.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/99.png")