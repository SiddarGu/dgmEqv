
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Onboarding","Training","Performance Evaluation","Promotion","Retention","Exit"], 
    x = [1000,800,600,400,200,100],
    textinfo = "value+percent initial",
    marker_color="deepskyblue",
    opacity=0.8,
    connector = {"line":{"color":"black","dash":"solid","width":3}}
))
fig.update_layout(title_text="Strategic Employee Management in Human Resources in 2020",
    font=dict(
        size=14
    ),
    margin=dict(
        l=20,
        r=20,
        b=20,
        t=50
    )
)
fig.update_layout(legend=dict(
    yanchor="bottom",
    y=0.01,
    xanchor="left",
    x=1
))
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/65.png", scale=5, width=800, height=600)