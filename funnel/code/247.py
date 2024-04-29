
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Education", "Research", "Support", "Advocacy", "Development", "Maintenance"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker = {"color": ["#7b68ee", "#6b486b", "#a05d56", "#d0743c", "#ff8c00", "#98abc5"]},
    opacity = 0.7,
))

fig.update_layout(
    title = {"text": "Social Sciences and Humanities Engagement in 2020"},
    font = {"family": "Times New Roman"},
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = 'rgba(0,0,0,0)',
    autosize = False,
    width = 800,
    height = 800,
    margin = {"l": 80, "r": 80, "t": 80, "b": 80},
    showlegend = False
)

fig.update_xaxes(showgrid = True, gridwidth = 1, gridcolor = 'LightGray')
fig.update_yaxes(showgrid = True, gridwidth = 1, gridcolor = 'LightGray')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/43.png")