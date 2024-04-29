
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [300000, 240000, 180000, 120000, 60000, 48000],
    textinfo = "value+percent initial",
))

fig.update_layout(title_text="Customer Acquisition in Food and Beverage Industry in 2021", 
    width=800, height=500,
    font=dict(family="Courier New, monospace", size=12, color="#7f7f7f"),
    legend=dict(orientation="h", x=-0.1, y=1.2)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/94.png")