
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Preparation", "Planting", "Growth", "Harvesting", "Processing","Packaging"],
    x = [1000, 750, 500, 300, 100, 50],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.8,
    marker = {"line": {"width": [0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
                    "color": ["darkblue", "royalblue", "cornflowerblue","lightblue", "paleturquoise", "lightcyan"]}},
))

fig.update_layout(
    title_text="Growth of Agriculture and Food Production Industry in 2021",
    font=dict(family="sans-serif"),
    hovermode="x",
    plot_bgcolor="white",
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor="LightGray"),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor="LightGray"),
    width=1000,
    height=800
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/12.png")