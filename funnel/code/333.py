
import plotly.graph_objects as go

fig = go.Figure(data=[go.Funnel(
    y = ["Cultivation","Harvesting","Packaging","Distribution","Sales","Others"],
    x = [1000,800,600,400,200,100],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont = dict(size = 12, color = '#000000'),
    marker = dict(
        color = '#8d44ad',
        line = dict(
            color = '#8d44ad',
            width = 1
        )
    )
)])
fig.update_layout(
    title = {
        'text': 'Agriculture and Food Production - Farm Size in 2020',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    legend = dict(x=1,y=0.9),
    paper_bgcolor='#f5f5f5',
    width=800,
    height=800,
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="#000000"
    ),
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=50
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/20.png")