
import plotly.graph_objects as go

fig = go.Figure(data=[go.Funnel(
    y = ["Education", "Advocacy", "Awareness", "Action", "Sustainability"],
    x = [200, 160, 120, 80, 40],
    textinfo="value+percent initial",
    textposition="inside",
    marker_line_width=2,
)])

fig.update_layout(
    title="Environmental Sustainability in 2020",
    font=dict(family="sans-serif")
)

fig.update_layout(
    margin=dict(l=10, r=10, t=50, b=50),
    width=800,
    height=600,
    paper_bgcolor="LightSteelBlue",
    plot_bgcolor="White",
    yaxis=dict(tickfont_size=16),
    xaxis=dict(tickfont_size=16),
    legend=dict(x=0.05, y=1, font_size=16, orientation="h"),
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/76.png")