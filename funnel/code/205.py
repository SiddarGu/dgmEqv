
import plotly.graph_objects as go
import plotly.io as pio

data = [go.Funnel(
    y=["Initial Inquiry","Feasibility Study","Project Planning","Implementation","Operation"],
    x=[1200,1000,800,600,400],
    textinfo="value+percent initial",
    marker_color='deeppink',
    opacity=0.8)]

fig = go.Figure(data=data)

fig.update_layout(
    title_text="Business Expansion in the Financial Sector in 2021",
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        family="Courier New, monospace",
    ),
    legend=dict(x=0.2, y=1.1),
    width=800,
    height=650,
    margin=dict(l=0, r=0, t=50, b=10)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/49.png")