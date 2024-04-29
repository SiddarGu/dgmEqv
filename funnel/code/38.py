
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    name = "Students",
    y = ["Research Interest", "Course Selection", "Project Initiation", "Data Analysis","Report Writing"],
    x = [100, 80, 60, 40, 20],
    textinfo = "value+percent initial"))

fig.update_layout(
    title = "Student Learning Progress in Social Sciences and Humanities",
    margin = {'t':100},
    font = {'family': 'arial'})

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/37.png", scale=2, width=800, height=800)