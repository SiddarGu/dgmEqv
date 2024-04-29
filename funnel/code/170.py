
import plotly.graph_objects as go
import plotly.io as pio

# Create figure
fig = go.Figure(go.Funnel(
    y = ["Homepage","Product Page","Shopping Cart","Checkout","Payment","Confirmation"],
    x = [1000, 900, 600, 500, 400, 200],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["royalblue","deepskyblue","cadetblue","lightblue","skyblue","teal"]},
))

# Set title
fig.update_layout(title_text="Online Shopping Funnel - Social Media and Web in 2021")

# Set legend
fig.update_layout(legend=dict(
    yanchor="bottom",
    y=0.01,
    xanchor="right",
    x=1
))

# Set figure size
fig.update_layout(
    width=1150,
    height=650,
    margin=dict(l=20, r=20, t=50, b=20),
    paper_bgcolor="LightSteelBlue",
)

# Set font
fig.update_layout(
    font=dict(
        family="Courier New, monospace",
        size=20,
        color="#7f7f7f"
    )
)

# Save figure
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/176.png")