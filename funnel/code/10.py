
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ['Event Promotion', 'Ticket Sales', 'Onsite Check-in', 'Attended Event', 'Purchased Souvenir'],
    x = [100, 83.5, 68.6, 51.7, 25.8],
    textinfo = 'value',
    orientation = 'h'
))
fig.update_layout(title_text = 'Event Attendance in Sports and Entertainment in 2021',
    font = dict(family = 'Times New Roman'),
    legend_orientation = 'h',
    legend_x = 0.5,
    legend_y = 1.1,
    xaxis_title = 'Number of Visitors',
    yaxis_title = 'Stages',
    width = 1000,
    height = 500,
    grid = {'rows': 1, 'columns': 1, 'pattern': 'independent'},
    margin = {'t': 100})
fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/5.png')