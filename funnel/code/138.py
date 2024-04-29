
import plotly.graph_objects as go

fig = go.Figure(data=[go.Funnel(
    y = ["Initial Consultation","Investigation","Negotiation","Court Hearing","Resolution","Others"],
    x = [1200, 950, 750, 550, 350, 250], 
    textinfo="value+percent initial",
    textposition="inside",
    marker=dict(
        color="rgb(255,197,89)",
        line=dict(
            color="rgb(255,255,255)",
            width=3
        )
    ),
    opacity=0.75
)])

fig.update_layout(
    title_text="Case Resolution for Legal Matters in 2021",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    shapes=[
        dict(
            type="rect",
            xref="paper",
            yref="paper",
            x0=0,
            y0=0,
            x1=1,
            y1=1,
            line_width=2
        )
    ],
    height=400,
    width=600,
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/11.png")