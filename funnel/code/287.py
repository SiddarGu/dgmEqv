
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    name="Agricultural Output Growth in Food Production in 2021",
    y = ["Planting", "Growing", "Harvesting", "Storing", "Processing", "Packaging", "Distribution"],
    x = [1000, 900, 800, 700, 600, 500, 400],
    textposition="inside",
    textinfo="value+percent initial",
    marker_line_color="darkgray",
    marker_line_width=1.5))

fig.update_layout(title_text="Agricultural Output Growth in Food Production in 2021")

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/31.png", width=900, height=900, scale=2)