
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [100000, 80000, 60000, 40000, 20000, 16000],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker = {"color": ["#9400D3","#4B0082","#0000FF","#00FF00","#FFFF00","#FF7F00"]},
    opacity = 0.7,
    connector = {"line":{"color":"rgb(63, 63, 63)","dash":"solid","width":3}},
))

fig.update_layout(
    title = {
        'text':'Audience Engagement - Sports and Entertainment in 2021',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font = dict(
        family = "Courier New, monospace",
        size = 12,
        color = "#7f7f7f"),
    autosize = False,
    width = 800,
    height = 600,
    margin = go.layout.Margin(
        l = 50,
        r = 50,
        b = 100,
        t = 100,
        pad = 4
    ),
    showlegend = True,
    legend_orientation = "h",
    legend=dict(
        x=0,
        y=1.1
    )
)

fig.write_image(r"/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/5.png")