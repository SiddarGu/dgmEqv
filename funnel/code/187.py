
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [20000, 15000, 10000, 7000, 3000, 2000],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_color = "#f1c40f",
    opacity = 0.7,
    hoverinfo = "text+percent initial+name"))

fig.update_traces(textposition='inside')
fig.update_layout(
    title = "Customer Journey in Food and Beverage Industry in 2020",
    font = dict(
        family = "Calibri, monospace",
        size = 16,
        color = "#7f7f7f"))

fig.update_layout(
    legend = dict(
        x = 0.75,
        y = 0.95,
        traceorder="normal"))

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#eeeeee')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#eeeeee')

fig.update_layout(
    autosize=False,
    width=800,
    height=900,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4),
    paper_bgcolor="LightSteelBlue")

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/105.png")