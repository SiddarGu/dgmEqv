

import plotly.graph_objects as go
import plotly.io as pio

# Create funnel chart
fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000, 888, 666, 462, 228],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont = dict(size = 14),
    marker = dict(color = ["#FFC2C2", "#FFA3A3", "#FF8A8A", "#FF7171", "#FF5858"])
))

# Set chart title
fig.update_layout(title_text = "Real Estate and Housing Market Overview in 2021")

# Set positioning of the legend
fig.update_layout(legend_orientation="h",
                  legend=dict(x=0.5, y=1.2))

# Set chart style
fig.update_traces(hovertemplate = None)

# Set background grid
fig.update_layout(
    xaxis = dict(showgrid = True, gridcolor = "#F2F2F2"),
    yaxis = dict(showgrid = True, gridcolor = "#F2F2F2")
)

# Set figsize
fig.update_layout(width=950, height=500)

# Save chart
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/39.png")