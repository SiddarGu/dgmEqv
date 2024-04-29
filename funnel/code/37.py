
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Order Placed","Production Started","Testing Completed","Packaging Finished","Shipping Out"],
    x = [100, 88.8, 66.6, 46.2, 22.8],
    textinfo = "value+percent initial",
    orientation = "h",
    textfont = dict(
        size=14,
        family="Courier New, monospace"
    ),
    marker = dict(
        color = "orange",
        line = dict(
            color = "gray",
            width = 0.5
        )
    )
))

fig.update_layout(
    title_text="Manufacturing and Production Process in 2020",
    showlegend = False,
    height=600,
    width=900,
    yaxis_title="Stages",
    xaxis_title="Number of Items"
)

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/6.png")
#pio.write_image(fig,"/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/6.png")