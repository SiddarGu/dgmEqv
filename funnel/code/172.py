
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Initial Contact", "Awareness", "Interest", "Consideration", "Intent", "Conversion"],
    x = [10000, 8000, 6000, 4000, 2000, 1600],
    textinfo = "value+percent initial",
    marker = {'color': ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c']},
    opacity = 0.7,
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
))

fig.update_layout(
    title = "Donor Engagement in Charity and Nonprofit Organizations in 2020",
    font = dict(
        family = "Courier New, monospace",
        size = 12,
        color = "#7f7f7f"
    ),
    width = 800,
    height = 750,
    autosize = False,
    plot_bgcolor = 'rgba(240,240,240, 0.95)',
    paper_bgcolor = 'rgba(240,240,240, 0.95)',
    margin = dict(
        l=0,
        r=40,
        b=0,
        t=60
    ),
    legend_orientation="h",
    legend=dict(x=0.5, y=-0.3),
    showlegend=True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/181.png")