
import plotly
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Recruitment", "Selection", "Training", "Retention", "Rewards", "Others"],
    x = [1000, 800, 650, 400, 200, 100],
    textinfo = "value+percent initial",
    marker_color = 'dodgerblue',
    textposition = "inside",
    textfont_size = 15,
    opacity = 0.8,
))

fig.update_layout(
    title = {
        'text': "Employee Management - HR Strategies in 2021",
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = dict(
        size = 18,
        color = "black"
    ),
    legend_orientation="h",
    plot_bgcolor="white",
    paper_bgcolor="white",
    width=1200,
    height=800,
    margin=dict(
        l=50,
        r=50,
        b=50,
        t=50,
        pad=4
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/33.png")