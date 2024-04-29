
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Research","Experimentation","Analysis","Refinement","Publication","Impact"],
    x = [10000,8000,6000,4000,2000,1000],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont_size = 10,
    marker = {'color': ['royalblue', 'crimson', 'green', 'orange', 'lightgray', 'violet']},
    opacity = 0.6,
    connector = {"line":{"color":"rgba(63, 63, 63, 0.5)","dash":"solid","width":2}},
    )
)

fig.update_layout(
    title = {'text':"Scientific Achievement in Science and Engineering in 2021",
             'y':0.9,
             'x':0.5,
             'xanchor':'center',
             'yanchor':'top'},
    showlegend = False,
    plot_bgcolor = "white",
    paper_bgcolor = "white",
    font = dict(
        size = 12,
        color = "black"
    ),
    width = 800,
    height = 600,
    margin = {"r":0,"t":40,"b":0,"l":0},
    yaxis = dict(
        showgrid = True,
        gridcolor = 'rgb(255, 255, 255)',
        zeroline = False
    ),
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/45.png")