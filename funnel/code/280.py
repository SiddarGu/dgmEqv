
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Initial Assessment", "Due Diligence", "Legal Advice", "Litigation", "Settlement", "Others"], 
    x = [1000, 820, 660, 460, 220, 180], 
    textinfo = "value+percent initial", 
    textposition = "inside", 
    marker_color = 'dodgerblue', 
    opacity = 0.6, 
))

fig.update_layout(
    title= {
        'text': "Legal Disputes Resolution in Law and Legal Affairs in 2021",
        'y':0.9, 
        'x':0.5, 
        'xanchor': 'center', 
        'yanchor': 'top'},
    font=dict(
        family="Courier New, monospace",
        size = 12,
        color="#7f7f7f"
    ),
    legend=dict(
        x = 0.75,
        y = 1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)',
    ),
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)',
    width=900,
    height=600,
    margin=dict(
        l=50, 
        r=50, 
        b=50, 
        t=50, 
        pad=4
    ),
    showlegend = True,
    hovermode = "closest",
)

fig.write_image("../png/113.png")