
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [4500, 3900, 2900, 1950, 900],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker_color = "darkblue"))

fig.update_layout(
    title = {
        'text': "Donor Engagement in Charity and Nonprofit Organizations in 2020",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"),
	legend_orientation="h",
    legend=dict(x=0.2, y=1.1),
    annotations=[dict(
        x=0.5,
        y=-0.1,
        xref="paper",
        yref="paper",
        text="Source: Plotly",
        showarrow = False)],
    width = 800,
    height = 600,
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = 'rgba(0,0,0,0)',
    margin=dict(l=20, r=20, t=50, b=20),
    showlegend=True
)

fig.write_image("../png/204.png")