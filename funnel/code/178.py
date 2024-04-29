
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Retention"],
    x = [10000, 9000, 7500, 6500, 5000, 3000],
    textinfo = "value+percent initial",
    textposition = "inside",
    hoverinfo = "y+x",
    marker = dict(
        color = ["#0075D9", "#0075D9", "#0075D9", "#0075D9", "#0075D9", "#0075D9"]
    )
)])

fig.update_layout(
    title = "Customer Engagement in Retail and E-commerce in 2020",
    font = dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)",
    showlegend = True,
    legend = dict(x=0.9, y=0.9),
    margin=dict(l=20, r=20, t=40, b=20),
    width = 1000,
    height = 800,
    hovermode = 'closest'
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/19.png")