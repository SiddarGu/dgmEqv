
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [100000, 80000, 60000, 40000, 20000, 16000],
    textinfo = "value+percent initial",
    marker_color = "dodgerblue",
    textposition = "inside",
    opacity = 0.65,
    connector = {"line":{"color":"royalblue"}}
))

fig.update_layout(
    title_text = "Social Media Engagement in 2021",
    font = dict(size=14, color="#444444"),
    plot_bgcolor = "#f9f9f9",
    paper_bgcolor = "#f9f9f9",
    width=1000,
    height=800,
    legend_orientation="h",
    legend=dict(x=0.5, y=-0.1)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/17.png")