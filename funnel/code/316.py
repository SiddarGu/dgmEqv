

import plotly.graph_objects as go

fig = go.Figure(data=[go.Funnel(
    y = ["Collection","Delivery","Distribution","Logistics","Planning","Others"],
    x = [1000, 800, 600, 400, 200, 120],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_color = 'royalblue',
    opacity = 0.7,
    marker = dict(
        line = dict(
            color = 'royalblue',
            width = 1,
        )
    )
)])

fig.update_layout(title_text='Streamline Delivery System - Transportation and Logistics in 2021', title_x=0.5, font_family='Arial')
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', legend=dict(orientation="h", x=0, y=-0.2))
fig.update_layout(width=800, height=400, margin=dict(l=20, r=20, t=50, b=20))
fig.write_image("../png/38.png")