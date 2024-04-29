
import plotly.graph_objects as go

fig = go.Figure(data=[go.Funnel(
    y = ["Awareness", "Interest","Consideration","Intent","Conversion","Others"],
    x = [800,700,500,400,200,100],
    textposition = "inside",
    textinfo = "value+percent initial"
)])

fig.update_layout(
    title_text="Consumer Engagement in Food and Beverage Industry in 2020",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    paper_bgcolor="LightSteelBlue",
    width=800,
    height=600
)

fig.write_image(
    "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/26.png"
)