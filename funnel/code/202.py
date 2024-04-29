
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry","Feasibility Study","Project Planning","Implementation","Operation"],
    x = [1000,888,666,462,228],
    textinfo = "value",
    textposition = "inside",
    textfont = dict(size = 20),
    opacity = 0.8,
    marker = {"color": ["lightblue","turquoise","blue","darkblue","navy"]},
    hoverinfo = "x+y+text",
    connector = {"line":{"color":"royalblue","dash":"dashdot","width":3}},
    orientation = "h",
))

fig.update_layout(
    title_text = "Business and Finance Project Development in 2021",
    showlegend = False,
    width = 800,
    height = 500,
    paper_bgcolor = "whitesmoke",
    plot_bgcolor = "white",
    margin = {"b":100,"t":100,"l":100,"r":100},
    xaxis = dict(
        showgrid = True,
        gridcolor = "lightgray",
        gridwidth = 1,
        showline = True,
        linecolor = "black",
        linewidth = 1,
        zeroline = True,
        zerolinecolor = "black",
        zerolinewidth = 1,
        mirror = False,
        visible = True,
        tickmode = "auto",
        nticks = 4
    ),
    yaxis = dict(
        showgrid = True,
        gridcolor = "lightgray",
        gridwidth = 1,
        showline = True,
        linecolor = "black",
        linewidth = 1,
        zeroline = False,
        mirror = False,
        visible = True,
        tickmode = "auto",
        nticks = 4
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/44.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/44.png")