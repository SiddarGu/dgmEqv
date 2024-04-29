

import plotly.graph_objects as go

# Data
Stage = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"]
Number_of_Users = [1000, 750, 500, 250, 125, 100]

# Create funnel plot
fig = go.Figure(data=[go.Funnel(
    y=Stage, 
    x=Number_of_Users,
    textinfo="value+percent initial",
    textposition="inside",
    marker=dict(
        color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"],
        line=dict(
            color="black",
            width=2
        )
    )
)])

# Set figure title, font, legend and grid
fig.update_layout(
    title="User Engagement in Social Media and the Web in 2021",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="#7f7f7f"
    ),
    showlegend=False,
    xaxis=dict(showgrid=True, zeroline=True, showticklabels=True),
    yaxis=dict(showgrid=True, zeroline=True, showticklabels=True),
    width=1000,
    height=800
)

# Write image
fig.write_image("../png/191.png")