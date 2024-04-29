
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Promotion","Ticket Sales","Event Opening","Event Process","Event Closing","Follow-up"],
    x = [1000,800,600,400,200,100],
    textinfo = "value+percent initial",
    marker_color = "dodgerblue",
    opacity = 0.7,
    textposition = "inside",
    textfont_size = 15,
    connector = {"line":{"color":"royalblue","dash":"solid","width":2}},
    ))
    
fig.update_layout(
    font=dict(
        family="Courier New, monospace",
        size=18
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    title={
        'text':"Participation Rate in Arts and Culture Events in 2021",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=1000,
    height=800,
    showlegend=False
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/58.png")