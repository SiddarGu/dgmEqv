
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()

fig.add_trace(go.Funnel(
    y=["Initial Inquiry","Feasibility Study","Project Planning","Implementation","Operation"], 
    x=[1000,900,700,500,200],
    textposition="inside",
    textinfo="value+percent initial",
    opacity=0.65,
    marker_color='#0099cc',
))

fig.update_layout(
    title_text="Legal Case Resolution - Law and Legal Affairs in 2021",
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        family="Roboto, sans-serif"
    ),
    margin=dict(t=50,b=25,l=25,r=25),
    width=1100,
    height=400,
    xaxis=dict(
        showgrid=True,
        showline=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Roboto, sans-serif',
            size=14,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=True,
        showline=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Roboto, sans-serif',
            size=14,
            color='rgb(82, 82, 82)',
        ),
    ),
    funnelmode='group',
    hovermode="x"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/127.png")