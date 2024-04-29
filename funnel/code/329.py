

import plotly.graph_objects as go
import plotly.io as pio

# Data
Stage = ["Initial Inquiry","Feasibility Study","Project Planning","Implementation","Operation"]
Number_of_Homebuyers = [1000,888,666,462,228]

# Create figure
fig = go.Figure()

# Add trace
fig.add_trace(
    go.Funnel(
        y=Stage,
        x=Number_of_Homebuyers,
        textinfo="value+percent initial",
        textposition="inside",
        width=0.4,
        hoverinfo="text",
        marker_color='royalblue',
        marker_line_color='dodgerblue',
        marker_line_width=2
    )
)

# Layout
fig.update_layout(
    title_text="Homebuyers Journey - Real Estate and Housing Market in 2021",
    font=dict(
        family="Courier New, monospace",
        size=10,
        color="#7f7f7f"
    ),
    width=700,
    height=400,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=True,
    legend=dict(
        x=0.85,
        y=1
    ),
    margin=dict(
        l=20,
        r=20,
        b=20,
        t=40
    )
)

# Save image
pio.write_image(fig, "../png/329.png")