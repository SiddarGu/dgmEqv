
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Introduction", "Research", "Knowledge Building", "Commitment", "Adoption", "Growth"],
    x = [10000, 9000, 7000, 5000, 3000, 1000],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_color = '#00AEEF',
    opacity = 0.7
))

fig.update_layout(
    title = {
        'text': "Technology Adoption - An Overview of the Internet in 2020",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font = dict(
        family = "Roboto",
        size = 14,
        color = "#000000"
    ),
    width = 800,
    height = 600,
    showlegend = False,
    margin = dict(
        l = 10,
        r = 10,
        t = 50,
        b = 10,
        pad = 4
    ),
    paper_bgcolor = "rgba(255,255,255,1)"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/175.png")