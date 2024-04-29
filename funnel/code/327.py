
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Pre-Production","Production","Post-Production","Distribution","Consumption","Waste Disposal"],
    x = [1000,800,600,400,200,100],
    textinfo = "value+percent initial",
    textposition="inside",
    opacity = 0.7,
    marker = {"color": ["#00AF50","#00AF50","#FFC000","#FFC000","#FF3D00","#FF3D00"]},
    connector = {"line":{"color":"rgb(63, 63, 63)", "dash":"solid", "width":3}}
))
fig.update_layout(
    title_text="Growing Agriculture and Food Production in 2020",
    font=dict(
        family="Calibri, sans-serif",
        size=14,
        color="black"
    ),
    legend_title_text="",
    legend=dict(
        x=0,
        y=1.1
    ),
    width=800,
    height=800,
    paper_bgcolor="white",
    plot_bgcolor="white",
    showlegend=True,
    margin=dict(
        l=10,
        r=10,
        b=10,
        t=50
    )
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/9.png")