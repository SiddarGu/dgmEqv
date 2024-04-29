
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()

fig.add_trace(go.Funnel(
    y = ["For Sale", "Open House", "Negotiation", "Closing", "Sold"],
    x = [400, 300, 200,100, 50],
    textinfo = "value+percent initial",
    textposition="inside",
    opacity = 0.7,
    marker = {"color": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"],
              "line": {"width": [0, 0, 0, 0, 0],
                       "color": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]}
    }
))

fig.update_layout(title_text="Real Estate Market - Houses Sold in 2021",
                  margin=dict(l=0,r=0,b=0,t=70,pad=0),
                  font=dict(family="Courier New, monospace",
                            size=13,
                            color="#7f7f7f"))

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/81.png", width=800, height=600, scale=2)
# or pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/81.png", width=800, height=600, scale=2)