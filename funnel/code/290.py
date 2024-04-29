
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Research","Design","Development","Production","Inspection","Shipping"],
    x = [1000,900,800,700,600,500],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.7,
    marker_color='royalblue',
    connector = dict(
        line = dict(
            color="royalblue",
            width=1.5,
            dash="dot"
        )
    ))])

fig.update_layout(
    title_text="Manufacturing Efficiency in Production Process in 2021",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    autosize=False,
    width=600,
    height=500,
    margin=dict(
        l=40,
        r=40,
        b=40,
        t=50,
        pad=4
    ),
    paper_bgcolor="LightSteelBlue",
    showlegend=True,
    legend_orientation="h",
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/38.png")