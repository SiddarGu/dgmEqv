
import plotly.graph_objects as go
import plotly.io as pio

data = {'Stage':['Awareness','Interest','Consideration','Intent','Conversion','Others'],
        'Number of Visitors':[5000,4500,4000,3500,3000,2500]}

fig = go.Figure(go.Funnel(
    y = data['Stage'],
    x = data['Number of Visitors'],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont_size = 12,
    opacity = 0.8,
    marker = {"color": ["#00A6A6", "#00A680", "#60A0A6","#F07878", "#F07844", "#F0A044"]},
))
fig.update_layout(
    title = {"text":"Exploring Tourism and Hospitality in 2021"},
    font = {"size": 12},
    legend_orientation="h",
    legend=dict(x=-.1, y=1.2),
    autosize=False,
    width=500,
    height=500,
    margin=go.layout.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=5
    ),
    paper_bgcolor='LightSteelBlue'
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/88.png")