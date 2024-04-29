
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Event Promotion","Ticket Booking","Event Attendance","Post-Event Follow-up","Others"],
    x = [5000,4000,3000,2000,1000],
    textinfo = "value+percent initial",
    marker_color = 'royalblue',
    opacity = 0.7,
    textposition = "inside",
    textfont_size = 10
))

fig.update_traces(textposition='inside')
fig.update_layout(
    title={
        'text':"Sports and Entertainment Event Engagement in 2020",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    width = 1000,
    height = 800,
    showlegend = True,
    legend_orientation="h",
    legend=dict(x=0.3, y=1.1),
    margin=dict(l=0, r=0, t=50, b=50),
    paper_bgcolor='white',
    plot_bgcolor='white'
)
fig.write_image("../png/109.png")