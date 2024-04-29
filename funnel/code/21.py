
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Promotion","Order Placed","Order Processing","Order Shipping","Order Received"], 
    x = [1000,800,600,400,200],
    textinfo = "value",
    orientation = "h",
    marker_color = "#f9cbe8")
)

fig.update_layout(title_text='Order Fulfillment - Food and Beverage Industry in 2020')
fig.update_layout(font={'family':'Times New Roman'})
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/26.png", width=800, height=600)