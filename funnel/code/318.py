
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Inquiry","Ordering","Delivery","Logistics","Final Delivery","Follow-up"],
    x = [3000,2500,2000,1500,1000,800],
    textinfo = "value+percent initial",
    textposition="inside",
    opacity = 0.8,
    marker = {"color": ["red","orange","yellow","green","blue","purple"]}
))

fig.update_layout(
    title = {"text":"Transportation and Logistics in 2020",
             "x":0.5,
             "xanchor":"center"},
    font = {"family":"sans-serif"},
    width=800,
    height=800,
    paper_bgcolor="LightSteelBlue",
    plot_bgcolor="LightSteelBlue",
    showlegend=True,
    legend_orientation="h",
    margin=dict(l=20, r=20, t=50, b=20)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/10.png")