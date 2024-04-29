
import plotly.graph_objects as go 
from plotly.subplots import make_subplots
import plotly.io as pio 

fig = make_subplots(rows = 1, cols = 1, specs = [[{"type": "funnel"}]])

fig.add_trace(go.Funnel(
    y = ["Screening", "Diagnosis", "Treatment", "Follow-up", "Outcome"],
    x = [800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    orientation = "h"), 1, 1)

fig.update_layout(title_text = "Patient Care in the Healthcare Industry in 2020")

fig.update_layout(
    width = 800,
    height = 500,
    margin = dict(l = 20, r = 20, t = 20, b = 20),
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)",
    showlegend = False)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/3.png")