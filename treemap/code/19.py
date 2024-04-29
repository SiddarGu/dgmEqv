import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ['Road Transport', 'Rail Transport', 'Water Transport', 'Air Transport', 'Pipeline Transport']
data = [40, 25, 20, 10, 5]

# Check if the directory exists, if not create it
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Define the treemap figure using Plotly Express

dframe = {
    'values': data,
    'labels': data_labels
}

fig = px.treemap(
    dframe,
    names=data_labels, 
    values=data,
    path=['labels'],
    title='Distribution of Freight Volume in Transportation and Logistics'
)

# Customize the layout
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    treemapcolorway=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"],
    paper_bgcolor="white",
)

# Save the figure
fig.write_image(f'{save_path}/19.png')

# Clear the current image state
fig.data = []
