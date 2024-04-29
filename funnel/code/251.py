
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

data_dict = {'Stage':['Awareness','Interest','Consideration','Intent','Conversion','Retention'],
             'Number of Customers':[100000,90000,80000,60000,40000,20000]}

df = pd.DataFrame(data_dict)
fig = go.Figure()
fig.add_trace(go.Funnel(
    y = df['Stage'],
    x = df['Number of Customers'],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity=0.6,
    marker = dict(
        color='royalblue',
    )
))

fig.update_layout(
    title_text = "Customer Journey in the Food and Beverage Industry in 2021",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    width=800,
    height=600,
    showlegend=True,
    legend=dict(x=-.1, y=1.2),
    margin=dict(l=20, r=20, t=40, b=20),
    hovermode = 'x'
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/47.png")