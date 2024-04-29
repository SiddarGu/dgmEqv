
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000, 888, 666, 462, 228],
    textinfo="value+percent initial",
    marker_color="darkblue",
    opacity=0.8,
    connector = {"line":{"color":"royalblue","dash":"solid","width":1.5}},
    textposition="inside"
))

fig.update_layout(
    template="plotly_white",
    title = {
        'text': 'Shipments in Transportation and Logistics Sector in 2021',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    legend={"x":0.8,"y":1,"xanchor":"right","yanchor":"top"},
    font={"size":14},
    autosize=True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/2.png", width=600, height=800, scale=2)
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/2.png", width=600, height=800, scale=2)