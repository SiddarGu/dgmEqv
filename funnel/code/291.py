
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y=["Initial Inquiry","Feasibility Study","Project Planning","Implementation","Operation"],
    x=[1000,888,666,462,228],
    textinfo="value+percent initial",
    textposition="inside",
    marker_color='royalblue',
    opacity=0.7
)])

fig.update_layout(
    title="Real Estate and Housing Market Trends in 2020",
    font_size=14,
    plot_bgcolor='white',
    legend=dict(
        x=1.05,
        y=0.5
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/39.png")
pio.write_image(fig,"/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/39.png")