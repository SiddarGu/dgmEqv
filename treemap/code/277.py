import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data = [
    ["Category", "Usage Share (%)"],
    ["Social Media", 25],
    ["Online Shopping", 20],
    ["Streaming Services", 15],
    ["Cloud Computing", 13],
    ["Online Gaming", 12],
    ["Cybersecurity", 8],
    ["Web Development", 4],
    ["Internet of Things", 3]
]

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = data[0][1:]  # ['Usage Share (%)']
line_labels = [row[0] for row in data[1:]]  # Extract first element of each row except header as line_labels
values = [row[1] for row in data[1:]]  # Extract numerical part of each row as values

# Define data for the treemap
fig_data = {
    'labels': line_labels,
    'parents': ["" for _ in line_labels],  # No parents since it's the top level categories
    'values': values
}

# Create treemap using plotly
fig = px.treemap(
    fig_data, 
    path=['labels'], 
    values='values', 
    title='Internet Usage Share by Technology Categories in 2023'
)

# Optional customizations can be added here

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1027.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.write_image(save_path)

# Clear the current image state in case more plotting will be done later
fig.data = []
