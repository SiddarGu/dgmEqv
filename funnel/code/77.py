
import plotly.graph_objects as go 
import plotly.io as pio 

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Retention"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent total",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["royalblue", "crimson", "orange", "green", "violet", "gray"]}))

fig.update_layout(
    title_text = "Retailing and E-commerce Growth in 2021",
    font = dict(
        family = "Roboto, sans-serif",
        size = 16,
        color = "#60606e"
    ),
    autosize = False,
    width = 800,
    height = 600,
    showlegend = True,
    legend_orientation = "h",
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)",
    margin=dict(l=20, r=20, t=50, b=20),
    xaxis_title = "Number of Customers",
    yaxis_title = "Stages"
)

fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/19.png')