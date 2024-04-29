
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Research and Development", "Production Planning", "Manufacturing", "Quality Control", "Packaging", "Shipping"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = 'value+percent initial',
    textposition = 'inside',
    marker_color = 'mediumturquoise'))

fig.update_layout(title_text='Manufacturing Output in the Production Industry in 2021',
                  xaxis_title_text='Number of Products',
                  yaxis_title_text='Stage',
                  font=dict(
                      family="sans-serif",
                      size=12,
                      color="Black"
                      ),
                  width=800,
                  height=600,
                  paper_bgcolor='rgb(255, 255, 255)',
                  margin=dict(l=50, r=50, t=50, b=50),
                  legend_orientation="h",
                  legend=dict(x=0.5, y=-0.2))

fig.write_image(file='../png/96.png')