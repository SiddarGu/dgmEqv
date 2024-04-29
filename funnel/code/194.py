
import plotly.graph_objects as go
fig = go.Figure(data=[go.Funnel(
    y = ["Initial Contact","Awareness","Interest","Consideration","Intent","Conversion"],
    x = [10000,8000,6000,4000,2000,1000],
    textinfo = "value+percent initial",
    marker_color='#67a9cf',
    textposition="inside",
    opacity=0.7,
    textfont_size=20
)])

fig.update_layout(
    title= {"text":"Donor Acquisition for Charity and Nonprofit Organizations in 2020",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
    legend = {'x':0.8,'y':0.1},
    margin=dict(l=20, r=20, t=40, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    width=800,
    height=600
)

fig.write_image("../png/35.png")