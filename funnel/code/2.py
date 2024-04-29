
import plotly.graph_objects as go

fig=go.Figure(go.Funnel(
    y = ["Research", "Development", "Analysis", "Evaluation", "Dissemination", "Others"], 
    x = [500, 400, 300, 200, 100, 50], 
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont_size = 12,
    opacity = 0.7,
    connector = {"line":{"color":"royalblue","dash":"solid","width":3}},
    marker_color = ['deepskyblue', 'mediumslateblue', 'royalblue', 'dodgerblue', 'cadetblue', 'lightsteelblue']
))
fig.update_layout(
    title = {"text":"Social Sciences and Humanities in 2021", "x":0.5, "y":0.9},
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="black"
    ),
    xaxis_title="Number of Participants",
    yaxis_title="Stage",
    width=900,
    height=700,
    showlegend=False
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-26_05-57-56_simulation_num50/png/37.png")