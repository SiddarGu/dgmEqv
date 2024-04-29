
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()

fig.add_trace(go.Funnel(
    y = ["Inquiry","Research","Booking","Arrival","Departure","Review"],
    x = [1000,800,600,400,200,100],
    textinfo = "value+percent initial",
    marker_color = "RoyalBlue",
    opacity=0.8,
    connector = {"line":{"color":"RoyalBlue","dash":"solid"}}
))

fig.update_layout(
    title="Tourism and Hospitality Funnel in 2020",
    font=dict(family="Courier New, monospace",size=18,color="RebeccaPurple"),
    height=600,
    width=1000,
    yaxis_title_text="Stage",
    xaxis_title_text="Number of Visitors",
    margin=dict(l=50,r=50,b=100,t=100,pad=4),
    showlegend = False
)

fig.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/23.png")