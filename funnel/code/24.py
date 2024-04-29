
import plotly.graph_objects as go

values=[10000,8000,6000,4000,2000,1000]
labels=["Interest","Research","Comparison","Purchase","Downloads","Subscriptions"]
fig = go.Figure(go.Funnel(
    y=labels,
    x=values,
    textinfo="value",
    orientation="h",
    opacity=0.8))
fig.update_layout(title_text="Online Shopping Habits - Technology and the Internet in 2021",
                font=dict(family="Courier New, monospace",size=14))
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/21.png")