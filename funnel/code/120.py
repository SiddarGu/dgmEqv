
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000, 880, 666, 462, 228],
    textinfo = "value+percent initial",
    marker_color='#ffa100',
    textposition = "inside",
    textfont_size = 20,
    opacity = 0.8,
    connector = {"line":{"color":"#ffa100", "dash":"solid"}},
    hoverlabel = {"bgcolor":"#ffa100"}
))

fig.update_layout(
    title={
        'text': "Social Media and Web User Engagement in 2021",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family="sans-serif",
        size=20,
        color="#7f7f7f"
    ),
    legend_orientation="h",
    legend=dict(x=0.5, y=0.2),
    width=1200,
    height=800,
    paper_bgcolor="white",
    plot_bgcolor="white",
    margin=go.layout.Margin(l=250, r=50, b=50, t=50, pad=4),
    showlegend=True
)

fig.write_image("../png/68.png")