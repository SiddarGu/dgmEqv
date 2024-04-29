

import plotly.graph_objects as go
import plotly.io as pio

# Set stage and number of students
stage = ["Enrollment","Orientation","Classroom Learning","Examination","Graduation","Post-Graduation"]
number = [1000,950,850,500,200,100]

# Create a funnel chart
fig = go.Figure(go.Funnel(
    y = stage,
    x = number,
    textinfo = "value+percent initial",
    marker = dict(
        color = ["royalblue","deepskyblue",'blue','lightblue','skyblue','powderblue']
    )
))

# Set the title of the figure
fig.update_layout(
    title_text = "Educational Journey of Students in 2020",
    font = dict(
        size = 15
    ),
    legend = dict(
        x = 0.2,
        y = 0.8
    ),
    width = 800,
    height = 500,
    xaxis_title = "Number of Students",
    yaxis_title = "Stage",
    paper_bgcolor = "white",
    plot_bgcolor = "white"
)

# Set the figsize to a larger setting to prevent content from being displayed.
fig.update_layout(
    width = 800,
    height = 500
)

# Save the image
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/2.png")