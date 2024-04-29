
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x = [1000,800,600,400,200,160],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.65,
    marker = {"color": ["#1f77b4", "#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b"]}
)])

fig.update_layout(title_text="Online Engagement - Social Media and the Web in 2020", font=dict(family="Courier New, monospace", size=14))
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

fig.write_image("../png/68.png", width=800, height=600, scale=2)