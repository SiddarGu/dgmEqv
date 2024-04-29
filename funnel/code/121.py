
import plotly.graph_objects as go
import plotly.io as pio

fig=go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [1000, 800, 500, 400, 300, 200],
    textinfo = "value+percent initial",
    textposition = "inside",
    hoverinfo = "none",
    marker = {"color": ["royalblue", "mediumseagreen", "orange", "gold", "plum", "violet"]}
))

fig.update_layout(
    title={"text": "Tourist Flow in Hospitality Industry in 2020", "x": 0.5, "y": 0.95},
    font={"family": "Courier New, monospace", "size": 11},
    legend={"x": 0.2, "y": 0.9},
    margin={"l": 80, "r": 80, "t": 80, "b": 80},
    width=900,
    height=600,
    paper_bgcolor = "white",
    plot_bgcolor = "white"
)

fig.write_image(r"/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/69.png")