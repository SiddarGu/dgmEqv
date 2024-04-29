
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()

fig.add_trace(go.Funnel(
    y = ["Introduction", "Research", "Experimentation", "Analysis", "Presentation", "Conclusion"],
    x = [1000, 850, 700, 550, 350, 150],
    textposition = "inside",
    textinfo = "value+percent initial",
    opacity = 0.65,
    marker_color = '#636efa'))

fig.update_layout(
    title_text="Student Engagement in Science and Engineering in 2020",
    font = dict(
        family = "Calibri, sans-serif",
        size = 12,
        color = "#7f7f7f"
    ),
    legend_orientation="h",
    legend=dict(x=0.1, y=1.1),
    width=800,
    height=800,
    margin=dict(l=20, r=20, t=50, b=20),
    paper_bgcolor="LightSteelBlue",
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/55.png")
pio.write_image(fig,"/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/55.png")