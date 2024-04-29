
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x = [500,400,300,200,100,80],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["#f9af0a","#f9af0a","#f9af0a","#f9af0a","#17d1d6","#17d1d6"]},
))
fig.update_layout(title_text="Cultural Engagement - Arts and Culture in 2021", width=900, height=600, font=dict(family="sans-serif", size=14))
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/87.png")