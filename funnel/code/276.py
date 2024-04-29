
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Research and Development", "Design and Planning", "Execution", "Delivery", "Evaluation"],
    x = [100, 88.8, 66.6, 46.2, 22.8],
    textinfo="value+percent initial",
    marker_color="royalblue",
    textposition="inside",
    opacity=0.7
))

fig.update_layout(
    title="Science and Engineering Projects in 2021",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    paper_bgcolor="LightSteelBlue",
    plot_bgcolor="LightSteelBlue",
    margin=dict(
        l=40,
        r=40,
        b=60,
        t=80,
        pad=4
    ),
    legend_orientation="h",
    legend_x=0,
    legend_y=-0.15,
    showlegend=True,
    width=800,
    height=500,
    grid=dict(
        rows=1,
        columns=1,
        pattern="independent",
        roworder="top to bottom"
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/98.png")