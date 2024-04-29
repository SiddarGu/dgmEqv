
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000, 800, 640, 512, 410],
    textinfo = "value+percent initial",
    textposition = "inside",
    hovertext = "Number of Customers",
    name = "Food and Beverage Industry Growth in 2020"
))

fig.update_layout(title_text="Food and Beverage Industry Growth in 2020",
                  font=dict(family="Courier New, monospace",
                            size=20,
                            color="#7f7f7f"),
                  height=1000,
                  width=1000,
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)')

pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-26_05-57-56_simulation_num50/png/47.png")