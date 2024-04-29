
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Funnel(
    name='Arts and Culture',
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [100000, 80000, 60000, 40000, 20000, 15000],
    textinfo = "value+percent initial"
))

fig.update_layout(
    title="Arts and Culture - Engagement Funnel Analysis in 2020",
    showlegend = True,
    legend_orientation="h",
    font = dict(
        size = 12
    ),
    plot_bgcolor = '#fff',
    paper_bgcolor = '#fff',
    margin = dict(
        l = 0,
        r = 0,
        t = 50,
        b = 0
    ),
    xaxis = dict(
        showgrid = True,
        gridcolor = '#ddd'
    ),
    yaxis = dict(
        showgrid = False
    ),
    width=800,
    height=400,
    hovermode = 'x'
)

fig.write_image(r'/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/58.png')