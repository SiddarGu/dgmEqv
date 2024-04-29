
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Research and Development", "Design", "Production", "Quality Control", "Distribution", "Others"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker = {"color": ["royalblue", "green", "teal", "orange", "red", "lightgray"]},
    opacity = 0.7
)])

fig.update_layout(
    title = "Manufacturing Output - Progress in 2021",
    font = {"family": "Times New Roman", "size": 18},
    legend_orientation="h",
    legend=dict(x=0.3, y=-0.2),
    width=800,
    height=600
)
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/9.png")