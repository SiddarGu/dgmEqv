
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x = [100000,90000,80000,70000,60000,55000],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity=0.7,
    marker = {"line": {"width": 0.5, "color": "black"}},
    connector = {"line": {"color": "rgb(63, 63, 63)", "dash":"dot", "width": 0.5}}
))

fig.update_layout(
    title_text="Technology Adoption - Internet Usage in 2020",
    font=dict(
        family="sans serif",
        size=12,
        color="black"
    ),
    margin=go.layout.Margin(
        l=50,
        r=50,
        b=50,
        t=50,
        pad=4
    ),
    legend=dict(
        xanchor="right",
        yanchor="top",
        x=1,
        y=1
    ),
    width=1000,
    height=800,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.write_image(f"/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/50.png")