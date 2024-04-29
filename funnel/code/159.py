
import plotly.graph_objects as go
import plotly.io as pio
fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Visits","Account Registration","Profile Set-up","Posting","Interaction","Retention"],
    x = [100000,70000,50000,30000,15000,10000],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker = {"color": ["#1A4E8F","#3F89D5","#6BC4FF","#B9DFFF","#EBF2FF","#F7F9FF"]},
    opacity = 0.7,
    connector = {"line":{"color":"rgb(63, 63, 63)"}}
))
fig.update_layout(
    title = {"text":"User Engagement on Social Media and the Web in 2020", "x":0.5, "y":0.9},
    font=dict(
        family="Arial",
    ),
    showlegend = False,
    width = 800,
    height = 500,
    margin={"l":100,"t":100,"b":100,"r":100},
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis=dict(showgrid=False,zeroline=False),
    yaxis=dict(showgrid=False,zeroline=False),
    annotations = [
        dict(
            x=0.5,
            y=0.1,
            xref="paper",
            yref="paper",
            text="Source: Social Media and Web",
            showarrow = False
        )        
    ]
) 
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/157.png")