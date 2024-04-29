
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y=["Hiring","Training","Evaluation","Retention","Termination"],
    x=[500,400,300,200,100],
    textinfo="value+percent initial",
    textposition="inside",
    marker_color="#FFC72C",
    opacity=0.7,
    marker=dict(
        color="#FFC72C",
        line=dict(
            color="black",
            width=1
        )
    )
)])

fig.update_layout(
    title="Employee Management in Human Resources - 2021",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="#7f7f7f"
    ),
    paper_bgcolor="white",
    yaxis=dict(
        showgrid=True,
        gridcolor="lightgray",
        gridwidth=1,
        showline=True,
        linewidth=2,
        linecolor="black",
        ticks="outside",
        tickfont=dict(
            family="Courier New, monospace",
            size=12,
            color="black"
        ),
    ),
    xaxis=dict(
        showgrid=True,
        gridcolor="lightgray",
        gridwidth=1,
        showline=True,
        linewidth=2,
        linecolor="black",
        ticks="outside",
        tickfont=dict(
            family="Courier New, monospace",
            size=12,
            color="black"
        ),
    ),
    legend=dict(
        x=1,
        y=1
    ),
    width=800,
    height=400,
    margin=dict(
        l=50,
        r=50,
        b=50,
        t=50,
        pad=4
    ),
    showlegend=False,
    hovermode="closest",
    plot_bgcolor="white",
    dragmode="select"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/33.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/33.png")