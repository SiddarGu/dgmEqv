
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x = [10000,8000,6000,4000,2000,1600],
    textinfo = "value+percent initial",
    textposition= "inside",
    opacity=0.65, 
    marker = {"color": ["#17b3e7","#17b3e7","#17b3e7","#17b3e7","#17b3e7","#17b3e7"]}
))

fig.update_layout(
    title_text="Conversion Funnel of E-commerce Customers in 2021",
    font_size=12,
    legend_orientation="h",
    legend=dict(x=0.1, y=1.1),
    width=800,
    height=600,
    showlegend=True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/41.png")