
import plotly.graph_objects as go
import plotly.io as pio

labels = ["Investment", "Research", "Analysis", "Planning", "Execution", "Results"]
values = [10000, 9000, 8000, 7000, 6000, 5000]

fig = go.Figure(go.Funnel(
    y = labels,
    x = values,
    textinfo = "value+percent initial",
    marker_color='#6699FF',
    textposition="inside",
    textfont_size=14,
    opacity=0.8))

fig.update_layout(
    title_text="Financial Profit and Loss Model in Business and Finance in 2021",
    font=dict(family="Courier New, monospace", size=18),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=False,
    width=1000,
    height=600,
    margin=dict(l=0, r=0, t=50, b=0))

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/49.png")