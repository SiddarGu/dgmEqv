
import plotly.graph_objects as go
import plotly.io as pio

# set figure size
fig = go.Figure(
    layout=go.Layout(
        title="Transportation and Logistics Services in 2021",
        font=dict(family="Poppins"),
        autosize=False,
        width=900,
        height=700,
    )
)

# add funnel chart
fig.add_trace(
    go.Funnel(
        y=["Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
        x=[100.0, 80.0, 60.0, 40.0, 20.0],
        textinfo="value+percent initial",
        textposition="inside",
        opacity=0.7,
        orientation="h",
        marker=dict(
            color='rgb(55, 83, 109)'
        )
    )
)

# set background grid
fig.update_layout(
    paper_bgcolor='rgba(0, 0, 0, 0)',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    yaxis=dict(
        gridcolor='rgba(0, 0, 0, 0.2)',
        zerolinecolor='rgba(0, 0, 0, 0)',
        showgrid=True,
        showline=False,
    )
)

# set legend
fig.update_layout(
    legend=dict(
        yanchor="top",
        y=1,
        xanchor="left",
        x=1.02
    )
)

# save figure
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/2.png")