
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000, 800, 600, 400, 200],
    textinfo = "value"
))

fig.update_layout(
    title = {"text": "Project Development in Energy Sector in 2021"},
    font = {"family": "Times New Roman"},
    autosize = True
)
fig.update_xaxes(title_text="Number of Projects")

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/1.png")