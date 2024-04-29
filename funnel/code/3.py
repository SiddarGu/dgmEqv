
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [50000, 40000, 30000, 20000, 10000, 8000],
    textinfo = "value+percent previous",
    textfont_size = 15,
    opacity = 0.8,
    marker = {"color": ["#a3a7e4","#dcd1e0","#f8c1c3","#e79f91","#ae6b6b","#823e3e"]}
))
fig.update_layout(
    title = {
        'text': "Social Media Engagement - Web Trends in 2020",
        'y':0.97,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    showlegend = False,
    font = {"family": "Courier New, monospace"},
    width = 800,
    height = 600,
    paper_bgcolor = "#FFFFFF",
    margin=dict(l=20, r=20, t=30, b=20)
)
fig.write_image("../png/funnel_7.png")