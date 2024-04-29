
import plotly.graph_objects as go
import plotly.io as pio

# Create figure
fig = go.Figure()

# Add data
fig.add_trace(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000, 900, 800, 700, 600],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["royalblue", "lime", "orange", "crimson", "lightblue"]},
    showlegend = False
))

# Set title
fig.update_layout(title_text="Real Estate and Housing Market Development in 2021")

# Set figure size
fig.update_layout(
    width=800,
    height=700,
)

# Set background grid
fig.update_layout(
    xaxis = {
        'showgrid': True,
        'gridcolor': 'LightPink',
    },
    yaxis = {
        'showgrid': True,
        'gridcolor': 'LightPink',
    },
)

# Save figure
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/62.png")