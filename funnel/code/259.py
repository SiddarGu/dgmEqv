
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Promotion","Ticket Sales","Attendance","Follow Up","Engagement","Others"],
    x = [1000,800,600,400,200,100],
    textinfo = "value+percent initial"
))

fig.update_layout(
    title = "Arts and Culture Event Attendance in 2021",
    font = dict(
        family = "Courier New, monospace",
        size = 12,
        color = "#7f7f7f"
    )
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')

fig.update_layout(legend_orientation="h", legend=dict(x=0.1, y=1))

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/58.png", width=700, height=500, scale=2)