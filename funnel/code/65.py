
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Researching","Booking","Preparing","Traveling","Returning","Others"],
    x = [20000,15000,10000,7500,4000,2500],
    textinfo = "value+percent initial",
    textposition="inside",
))
fig.update_layout(
    title_text="Tourism Growth in Hospitality in 2023",
    font=dict(
        family="Courier New, monospace"
    ),
    width=800,
    height=400
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/15.png")