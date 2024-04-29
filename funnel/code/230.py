
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [10000, 8000, 6000, 4000, 2000, 1600],
    textinfo = "value+percent initial",
    textfont_size = 20,
    marker = {
        "color": ["#F8BE7D", "#F29E4C", "#E87D22", "#DE5C00", "#C43F00", "#AA2F00"],
        "line": {
            "width": [0, 0, 0, 0, 0, 0],
            "color": ["#F8BE7D", "#F29E4C", "#E87D22", "#DE5C00", "#C43F00", "#AA2F00"]
        }
    }
))

fig.update_layout(
    title = {
        "text": "Online Visitor Engagement - Social Media and the Web in 2020",
        "y": 0.97,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top"
    },
    font = {"family": "Times New Roman"},
    hovermode = "x",
    xaxis = {
        "ticks": "outside",
        "showgrid": True,
        "gridcolor": "#FFFFFF"
    },
    yaxis = {
        "ticks": "outside",
        "showgrid": True,
        "gridcolor": "#FFFFFF"
    },
    legend = {
        "x": 0.5,
        "y": 0.2,
        "xanchor": "center",
        "yanchor": "top"
    },
    width = 1200,
    height = 800,
    margin = dict(
        l = 0,
        r = 0,
        t = 30,
        b = 0
    ),
    showlegend = True
)

fig.write_image("../png/125.png")
pio.write_image(fig, "../png/125.png")