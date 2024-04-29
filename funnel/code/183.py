
import plotly.graph_objects as go 
fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Research", "Inquiry", "Quotation", "Negotiation", "Order", "Delivery"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    hovertemplate = 'Stage: %{y}<br>Number of Customers: %{x}<br>Percentage: %{percent}<extra></extra>',
    marker_color='deeppink',
    opacity=0.7,
    connector = {"line":{"color":"deeppink","width":2}},
))
fig.update_layout(
    title={"text": "Logistics Process in Transportation Industry in 2021",
           "y":0.9,
           "x":0.5,
           "xanchor":"center",
           "yanchor":"top"},
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    legend_orientation="h",
    legend=dict(x=0.5, y=1.2),
    width=800,
    height=600,
    paper_bgcolor="LightSteelBlue",
    plot_bgcolor='white',
    margin=dict(l=20, r=20, t=40, b=30),
    showlegend=True,
    # annotations=[
    #     dict(
    #         x=0.5,
    #         y=1.1,
    #         xref="paper",
    #         yref="paper",
    #         text="Source: Logistics Process in Transportation Industry in 2021",
    #         showarrow=False,
    #     )
    # ],
)
fig.write_image("../png/2.png")