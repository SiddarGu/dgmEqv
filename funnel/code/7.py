
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Research","Engagement","Conversion","Retention","Loyalty","Advocacy"],
    x = [1000, 800, 500, 200, 100, 50],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont = dict(
        color = "white"
    ),
    opacity = 0.65,
    marker = dict(
        color = ["#636efa","#ef553b","#00cc96","#ab63fa","#FFA15A","#19d3f3"],
        line = dict(
            color = "white",
            width =  2
        )
    )
))

fig.update_layout(
    title_text = "Social Media and Web Usage in 2020",
    plot_bgcolor = "rgb(255, 255, 255)",
    paper_bgcolor = 'rgb(255, 255, 255)',
    font = dict(
        family = "Open Sans",
        size = 12,
        color = "#000000"
    ),
    legend = {
        "x": 0.7,
        "y": 1
    },
    margin = {
        "l": 100
    },
    width = 800,
    height = 700,
    showlegend = True
)

fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-26_05-57-56_simulation_num50/png/17.png', width=800, height=700, scale=2)