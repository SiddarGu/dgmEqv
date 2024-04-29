
import plotly.graph_objects as go 
import plotly.io as pio 

fig = go.Figure(go.Funnel(
    y = ['Education', 'Research', 'Public Engagement', 'Policy Making', 'Funding', 'Others'],
    x = [3000, 2700, 2400, 2100, 1800, 1500],
    textposition = "inside",
    textinfo = "value+percent initial",
    orientation = "h",
    marker = dict(
        color = ["deepskyblue", "royalblue", "mediumblue", "dodgerblue", "cornflowerblue", "lightsteelblue"]
        )
    ))

fig.update_layout(
    title = 'Social Sciences and Humanities Development in 2020',
    font = dict(
        family = "Courier New, monospace",
        size = 16,
        color = 'black'
    ),
    width = 800,
    height = 600,
    showlegend = True,
    legend_orientation = "h",
    legend = dict(x=0.75, y=1.05),
    paper_bgcolor = 'white',
    plot_bgcolor = 'white',
    margin = dict(l=200, r=100, t=100, b=50)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/73.png")