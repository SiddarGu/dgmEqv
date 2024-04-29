
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ['Awareness','Interest','Consideration','Intent','Conversion','Others'],
    x = [20000,15000,10000,5000,3000,1500],
    textinfo = "value+percent initial",
    marker_color = 'royalblue',
    opacity = 0.7))
fig.update_layout(title_text = 'Audience Engagement in Sports and Entertainment in 2020',
                  font = dict(family = "Courier New, monospace",
                              size = 12,
                              color = "#7f7f7f"),
                  width = 800, 
                  height = 600, 
                  legend_orientation="h",
                  legend=dict(x=0.5, y=-.1),
                  paper_bgcolor='rgb(255,255,255)',
                  plot_bgcolor='rgb(255,255,255)',
                  xaxis_title="Number of Audience",
                  yaxis_title="Stage",
                  showlegend=True,
                  margin=dict(l=50, r=50, t=50, b=50)
                 )
fig.write_image("../png/40.png")