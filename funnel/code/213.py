
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Funnel(
        name = 'Real Estate and Housing Market Expansion in 2020',
        y = ["Initial Inquiry","Feasibility Study","Project Planning","Implementation","Operation"],
        x = [150,125,100,80,50],
        textinfo = "value+percent initial",
        textposition = "inside",
        opacity = 0.7,
        marker = dict(
            color = 'royalblue',
            line = dict(
                color = '#ffffff',
                width = 2
            )
        )
    ))

fig.update_layout(
    title={
        'text': "Real Estate and Housing Market Expansion in 2020",
        'y':0.98,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family="Calibri, monospace",
        size=18,
        color="#000000"
    ))

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#eeeeee')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#eeeeee')
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/62.png",width=800, height=600, scale=2)