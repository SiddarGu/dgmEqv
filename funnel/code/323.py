
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()

fig.add_trace(go.Funnel(
    y = ["Planting","Fertilizing","Harvesting","Processing","Distribution","Consumption"],
    x = [100000,80000,60000,40000,20000,16000],
    textinfo = "value+percent initial",
    connector = {"line":{"color":"royalblue"}},
    marker_color = 'lightsalmon'
))

fig.update_layout(
    title_text = 'Agriculture and Food Production in 2020',
    font = dict(
        color = 'black'
    ),
    width = 600,
    height = 600
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/48.png")