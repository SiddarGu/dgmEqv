
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Sowing", "Growing", "Harvesting", "Processing", "Distribution"],
    x = [100, 80, 60, 40, 20],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.7,
    marker_color = ["royalblue", "crimson", "green", "darkorange", "mediumpurple"]
)])

fig.update_layout(
    title = {"text": "Food Production Cycle and Farming in 2021", "x": 0.5},
    width = 800,
    height = 600,
    xaxis = dict(
        tickmode = "linear",
        showgrid = True,
        gridcolor = "LightGrey",
        zeroline = False,
    ),
    yaxis = dict(
        showgrid = False,
        zeroline = False,
    ),
    font = dict(family = "Times New Roman"),
    legend = dict(
        x = 0.5,
        y = 1,
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/50.png")