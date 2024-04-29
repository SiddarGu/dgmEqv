
import plotly.graph_objects as go
import plotly.io as pio

# Data
stage = ["Awareness","Interest","Consideration","Intent","Conversion","Others"] 
users = [1000,900,800,700,500,300]

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = stage,
    x = users,
    textinfo = "value+percent initial",
    orientation = "h",
    marker = dict(color = "royalblue", line = dict(color = "royalblue", width = 2.5)),
    opacity = 0.8))

fig.update_layout(
    title = {"text": "User Engagement on Social Media and the Web in 2020", 
             "y":0.95, "x":0.5, 
             "xanchor": "center", "yanchor": "top"},
    font = dict(family = "Courier New, monospace", size = 20))

fig.update_layout(height=800, width=1000,
                  margin=dict(l=0, r=0, t=50, b=0),
                  paper_bgcolor="LightSteelBlue",
                  plot_bgcolor='rgba(0,0,0,0)')

# Save Image
fig.write_image("../png/152.png")