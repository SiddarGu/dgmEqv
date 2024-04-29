
import plotly.graph_objects as go 
import plotly.io as pio

data = [
    {"Stage": "Initial Inquiry", "Number of Subscribers": 1000},
    {"Stage": "Feasibility Study", "Number of Subscribers": 900},
    {"Stage": "Project Planning", "Number of Subscribers": 800},
    {"Stage": "Implementation", "Number of Subscribers": 700},
    {"Stage": "Operation", "Number of Subscribers": 600},
]

fig = go.Figure(go.Funnel(
    y = [x["Stage"] for x in data],
    x = [x["Number of Subscribers"] for x in data],
    textinfo = "value+percent initial"))

fig.update_layout(
    title = {
        'text': 'Subscriber Growth in Energy and Utilities Sector in 2021',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = {'family':'sans serif', 'size':15},
    showlegend=False,
    plot_bgcolor='white',
    paper_bgcolor='white',
    margin = {'l':50, 'r':50, 't':50, 'b':50},
    width=800,
    height=400,
    hovermode="closest",
    xaxis_title = 'Number of Subscribers',
    yaxis_title = 'Stage',
    legend_orientation="h")

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/46.png")