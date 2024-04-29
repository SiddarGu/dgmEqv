
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Inquiries","Research","Offers","Negotiation","Closing","Follow-up"],
    x = [1000,900,800,700,500,400],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont_size = 14,
    opacity = 0.8,
    marker = {"color": ["#ba68c8","#f06292","#4fc3f7","#ff8a65","#90a4ae","#ffd54f"]},
    connector = {"line":{"color":"#999","dash":"solid"}}
))

fig.update_layout(
    title = "Real Estate Market Performance in 2020",
    font = {"family":"sans-serif"},
    plot_bgcolor = "white",
    paper_bgcolor = "white",
    margin = {"t":50,"b":50,"l":50,"r":50},
    width = 800,
    height = 650,
    showlegend = True,
    legend_orientation = "h"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/39.png")