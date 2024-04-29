
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# set fig size
fig = make_subplots(rows=1, cols=1, specs=[[{"type": "funnel"}]], 
                    subplot_titles=["Managing Employees in Human Resources in 2021"],
                    )

# set data
fig.add_trace(go.Funnel(
    y = ["Recruitment", "Training", "Performance Evaluation", "Retention", "Termination"],
    x = [4000, 3000, 2000, 1000, 500],
    textinfo = "value+percent initial",
    opacity = 0.8,
    marker = {"line": {"width": [0, 0, 0, 0, 0], "color": ["black", "black", "black", "black", "black"]}},
    textposition = "inside",
    textfont_size = 12,
    name = "Stage"
), 1, 1)

# set figure layout
fig.update_layout(
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    showlegend = True,
    width = 800,
    height = 600
)

# save image
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/85.png")