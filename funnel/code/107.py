
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    name = "Project Development in Energy Sector in 2021",
    y = ["Initial Inquiry","Feasibility Study","Project Planning","Implementation","Operation"],
    x = [100,80,60,40,20],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_color = 'royalblue',
    opacity = 0.8))

fig.update_layout(
    title = {
        'text': "Project Development in Energy Sector in 2021",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(family="Times New Roman", size=18, color="Black"),
    showlegend=True,
    width=800,
    height=600,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_showgrid=False,
    yaxis_showgrid=False)
fig.write_image("../png/46.png")