
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Planting", "Harvesting", "Processing", "Distribution", "Consumption", "Other"],
    x = [1000, 800, 600, 400, 200, 160],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont_size = 18,
    opacity=0.8,
    marker = dict(
        color = ['#FFCE54', '#FFA41B', '#F07E10', '#C75B12', '#9A3B1B', '#6D2C1D']
    )
))

fig.update_layout(
    title="Food Production in Agriculture Sector in 2020",
    font=dict(
        size=20,
    ),
    width = 800,
    height = 800,
    margin=dict(
        l=50,
        r=50,
        b=50,
        t=50,
        pad=4
    ),
    showlegend=True,
    legend=dict(
        x=0,
        y=1.1
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/42.png")