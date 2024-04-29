
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Conservation", "Mitigation", "Adaptation", "Education", "Public Awareness", "Others"],
    x = [1000, 800, 600, 450, 300, 200],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker = dict(
        line = dict(color = '#000000', width = 2)
    ),
    opacity = 0.7,
    connector = {"line":{"color":"#000000","dash":"solid","width":2}},
    hoverinfo='text'
))

fig.update_traces(textposition='outside', textfont_size=12)
fig.update_layout(
    title = "Sustainable Development Participation in Environment and Sustainability in 2020",
    font = dict(family="Courier New, monospace", size=13, color="#000000"),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    autosize=False,
    width=900,
    height=650,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    showlegend=False,
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/90.png")