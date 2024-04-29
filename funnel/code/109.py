
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y=["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x=[100000,80000,60000,40000,20000,16000],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.65,
    marker={'color': ['#aec7e8','#c4b9bb','#f7b6d2','#e377c2','#c5b0d5','#dbdb8d']},
    connector={'line': {'color': 'rgb(63, 63, 63)', 'dash': 'solid'}}))

fig.update_layout(
    title="Food and Beverage Industry Growth in 2021",
    barmode='overlay',
    height=600,
    width=800,
    shapes=[
        {
            'type': 'rect',
            'xref': 'paper',
            'yref': 'paper',
            'x0': 0,
            'y0': 0,
            'x1': 1,
            'y1': 1,
            'fillcolor': '#f2f2f2',
            'opacity': 0.4,
            'layer': 'below',
            'line': {
                'width': 1,
            }
        }
    ]
)
fig.update_xaxes(showgrid=True, gridcolor='#F2F2F2')
fig.update_yaxes(showgrid=True, gridcolor='#F2F2F2')
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/47.png")