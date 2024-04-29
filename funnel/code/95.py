
import plotly.graph_objects as go
from plotly.offline import plot

fig = go.Figure(go.Funnel(
    y = ["Knowledge","Attitude","Behaviour","Action","Influence","Impact"],
    x = [10000,7000,5000,3000,1000,400],
    textinfo = 'value+percent previous',
    textposition="inside",
    opacity=0.75,
    marker={'color': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                         '#9467bd', '#8c564b']},
))

fig.update_layout(title_text="Public Policy Impact on Citizens in 2021",
                  font=dict(family="Calibri", size=14))
fig.update_layout(
    margin=dict(l=0, r=0, b=50, t=100, pad=4),
    legend=dict(x=0.4, y=-0.2)
)

fig.write_image(r"/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/14.png",width=600, height=600, scale=2)