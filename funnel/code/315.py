
import plotly.graph_objects as go
import plotly.io as pio

data = [
  ['Receiving', 1000],
  ['Checking', 800],
  ['Sorting', 600],
  ['Packaging', 400],
  ['Shipping', 200],
  ['Delivering', 100]
]

fig = go.Figure(data=[go.Funnel(
    y = [row[0] for row in data],
    x = [row[1] for row in data],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.5,
    marker_color='indianred',
    hoverinfo = "y+x"
    )])

fig.update_layout(
    title={
        'text': "Transportation and Logistics - Goods Flow in 2021",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/37.png",width=950, height=630, scale=2)