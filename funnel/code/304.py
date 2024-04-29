

import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Education","Information Gathering","Evaluation of Policies","Implementation of Policies","Post-Implementation Assessment","Others"],
    x = [1000,800,600,400,200,100],
    textinfo="value",
    textposition="inside",
    textfont=dict(
        color="black",
        size=16
    ),
    hoverinfo = "none",
    marker = dict(
        color = ["#0d47a1","#1b5e20","#e65100","#ff6f00","#f57f17","#0d47a1"]
    ),
    opacity=0.8
)])

fig.update_layout(
title={
        'text': "Government and Public Policy Engagement in 2021",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=1000,
    height=800,
    font=dict(
        family="Arial",
        size=20,
    ),
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
        zeroline=False
    ),
    margin = dict(
        l = 50,
        r = 50,
        b = 50,
        t = 50,
        pad = 5
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=True
)

fig.write_image(r"../png/22.png")