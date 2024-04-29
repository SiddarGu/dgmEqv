
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Seeding", "Growth", "Harvesting", "Processing", "Distribution", "Consumption"],
    x = [800, 600, 450, 250, 200, 100],
    textinfo="value+percent initial",
    orientation="h",
    marker = {"color": ["#f2c914", "#f2c914", "#f2c914", "#f2c914", "#f2c914", "#f2c914"]}
))
fig.update_layout(title_text="Agricultural Production Cycle in 2020",
                  font=dict(family="Times New Roman"),
                  width=800,
                  height=500,
                  legend_orientation="h")
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/31.png")