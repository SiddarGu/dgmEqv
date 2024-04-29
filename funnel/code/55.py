
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation","Operation"],
    x = [20000, 18000, 14000, 10000, 5000],
    textinfo = "value+percent initial",
    textfont_size = 15,
    marker_color = 'royalblue',
    opacity = 0.7,
    connector = {"line":{"color":"royalblue","dash":"solid","width":3}}
))
fig.update_layout(
    title_text = "Tourism and Hospitality - Visitor Profiles in 2020",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    width=900,
    height=800,
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    legend=dict(
        x=0.9,
        y=1
    ),
    grid=dict(columns=1, rows=1, pattern='independent'),
    showlegend=True
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/71.png")