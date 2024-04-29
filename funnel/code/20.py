
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Reducing Carbon Emissions", "Reducing Air Pollution", "Supporting Sustainable Agriculture", "Protecting Biodiversity", "Creating Green Spaces"],
    x = [150, 90, 60, 30, 20],
    textinfo = "value",
    textposition = "inside",
    marker_color='rgb(63, 81, 181)',
))

fig.update_layout(
    title={
        'text': "Green Initiatives - Environment and Sustainability in 2020",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=800,
    height=500,
    font=dict(
        family="Arial, sans-serif"),
    paper_bgcolor="white",
    plot_bgcolor="white",
    showlegend=True,
    legend_orientation="h",
    legend=dict(x=0.9, y=0.9))

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/12.png")