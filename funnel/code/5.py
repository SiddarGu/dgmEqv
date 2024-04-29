
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x = [100000,60000,30000,18000,8000,4000],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont = dict(
        size = 10,
        color = '#000000'
    ),
    marker = dict(
        color = '#ffc400',
        line = dict(
            color = '#ffc400',
            width = 1
        )
    ),
    opacity = 0.7
))

fig.update_layout(
    title = "Online Technology Adoption in 2020",
    font = dict(
        family = "Courier New, monospace",
        size = 15,
        color = "#7f7f7f"
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-26_05-57-56_simulation_num50/png/21.png", width=800, height=600)