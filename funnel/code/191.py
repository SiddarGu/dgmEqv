
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

stages = ['Inquiry','Research','Bookings','Delivery','Fulfillment','Follow-up']
number_of_orders = [120,96,72,56,36,18]
fig = make_subplots(
    rows=1, cols=1,
    specs=[[{"type": "funnel"}]],
    subplot_titles=['Transportation and Logistics Services in 2021']
)
fig.add_trace(go.Funnel(
    y = stages,
    x = number_of_orders,
    textinfo="value+percent initial",
    marker_color='#0099FF',
    opacity=0.9
))
fig.update_layout(
    width=800,
    height=800,
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/32.png")