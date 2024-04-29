

import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Initial Research", "Market Analysis", "Risk Assessment", "Contract Negotiation", "Investment", "Others"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker_color = 'royalblue',
))

fig.update_layout(title = "Investment Trends in Business and Finance in 2021",
    font=dict(size=14))

fig.update_yaxes(gridcolor = 'lightgray')
fig.update_xaxes(gridcolor = 'lightgray')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/44.png", width = 800, height=600)