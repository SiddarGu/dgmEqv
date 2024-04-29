
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["First Contact", "Diagnosis", "Treatment Plan", "Follow-up", "Recovery"],
    x = [100000, 88800, 73280, 55400, 27700],
    textinfo = "value+percent initial",
    textfont = dict(
        size = 18,
        color = "black"
    ),
    hoverlabel = dict(
        bgcolor = "white", 
        font = dict(
            color = "black"
        )
    ),
    marker = dict(
        color = ["#008080","#3CB371","#FFD700","#FF8C00","#CD5C5C"],
        line = dict(
            color = "black",
            width = 0.5
        )
    ),
    connector = dict(
        line = dict(
            color = "black",
            width = 0.5
        )
    )
))

fig.update_layout(
    title = {
        'text': "Healthcare Journey - Healthcare and Health in 2021",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = dict(
        color = "black",
        size = 18
    ),
    paper_bgcolor = "#FFFFFF",
    plot_bgcolor = "#FFFFFF",
    yaxis = dict(
        showgrid = True,
        gridcolor = "lightgrey"
    ),
    legend = dict(
        x = 0.87,
        y = 0.95,
        font = dict(
            size = 18
        )
    ),
    margin = dict(
        l = 200,
        r = 20,
        b = 100,
        t = 100,
        pad = 4
    ),
    height = 500,
    width = 950
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/92.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/92.png")