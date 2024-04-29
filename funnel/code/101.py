
import plotly.offline as pyo
import plotly.graph_objs as go

data = [
    go.Funnel(
        y = ["Research & Development", "Design & Prototype", "Testing & Validation", "Production & Delivery", "After-sales Service"],
        x = [1000, 800, 600, 400, 200],
        textinfo = "value+percent initial",
        marker = {
            "color": ["#8FBC8F", "#3CB371", "#2E8B57", "#228B22", "#008000"],
            "line": {
                "color": ["#8FBC8F", "#3CB371", "#2E8B57", "#228B22", "#008000"],
                "width": 2
            }
        },
        opacity = 0.7
    )
]

layout = go.Layout(
    title = "Manufacturing and Production Performance in 2021",
    font = dict(
        size = 16
    ),
    xaxis = {
        "showgrid": False,
        "title": "Number of Products"
    },
    yaxis = {
        "showgrid": False,
        "title": "Stage"
    },
    legend = {
        "xanchor": "center",
        "yanchor": "top",
        "x": 0.5,
        "y": 1
    },
    width = 600,
    height = 600,
    autosize = False,
    margin = go.layout.Margin(
        l = 30,
        r = 30,
        b = 30,
        t = 30,
        pad = 0
    ),
    plot_bgcolor = "rgba(0, 0, 0, 0)",
    paper_bgcolor = "rgba(0, 0, 0, 0)"
)

fig = go.Figure(data = data, layout = layout)
pyo.plot(fig, filename="funnel.html")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/38.png")