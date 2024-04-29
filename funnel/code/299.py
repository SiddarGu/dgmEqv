
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000, 900, 700, 500, 300],
    textinfo = "value+percent initial",
    hoverinfo = "text",
    textfont_size = 16,
    marker_color = 'royalblue',
    opacity = 0.7
))

fig.update_layout(
    title = {
        'text': "Customer Engagement in Energy Sector in 2020",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    legend_orientation="h",
    legend_x = 0,
    legend_y = -0.25,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=50, r=50, t=50, b=50),
    width=700,
    height=400,
    showlegend=True,
    hovermode='closest',
    xaxis_title="Number of Customers",
    yaxis_title="Stage"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/1.png")