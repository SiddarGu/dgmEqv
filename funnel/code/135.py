
import plotly.graph_objects as go
import plotly.io as pio

data = [go.Funnel(
    y = ['Research and Development', 'Design and Prototyping', 'Production', 'Testing', 'Packaging', 'Shipping'],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = 'value+percent initial',
    textfont_size = 16,
    marker = dict(
        color = ['royalblue', 'deepskyblue', 'skyblue', 'lightskyblue', 'lightblue', 'aliceblue'],
        line = dict(
            color = '#000000',
            width = 2
        )
    ),
    opacity = 0.8,
    connector = dict(
        line = dict(
            color = '#000000',
            width = 2
        )
    )
)]

fig = go.Figure(data)
fig.update_layout(
    title = 'Manufacturing and Production Trends in 2021',
    margin = dict(
        l = 30,
        r = 30,
        b = 20,
        t = 40
    ),
    paper_bgcolor = '#FFFFFF',
    plot_bgcolor = '#FFFFFF',
    showlegend = False,
    font = dict(family = 'Arial', size = 12)
)

fig.update_yaxes(showgrid = True, gridwidth = 1, gridcolor = '#DCDCDC')
fig.update_xaxes(showgrid = True, gridwidth = 1, gridcolor = '#DCDCDC')

fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/96.png', width = 800, height = 600)
pio.write_image(fig, '/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/96.png')