
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [1000, 800, 600, 400, 200, 160],
    textinfo = "value+percent initial",
    marker = {"color": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]},
    textposition = "inside",
    opacity = 0.8
))

fig.update_layout(
    title = "Visitor Engagement - Tourism and Hospitality in 2020",
    font = dict(
        family="Courier New, monospace",
        size=16,
        color="#7f7f7f"
    ),
    width = 800,
    height = 700,
    xaxis = dict(
        visible=False
    ),
    yaxis = dict(
        visible=False
    ),
    showlegend = False,
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/15.png")