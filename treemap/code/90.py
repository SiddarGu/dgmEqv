import os
import plotly.express as px
import plotly.graph_objects as go

# Given data
data_labels = ["Revenue Share (%)"]
line_labels = ["Team Sports", "Individual Sports", "Concerts", "Movies", "Video Games", "Streaming Services", "Amusement Parks", "Live Theater"]
data = [25, 20, 15, 15, 10, 7, 5, 3]

# Data for treemap
treemap_data = {
    'labels': line_labels,
    'values': data,
    'parents': [""] * len(line_labels)
}

# Create the treemap
fig = px.treemap(
    treemap_data,
    names='labels',
    values='values',
    parents='parents',
    title='Revenue Distribution in the Sports and Entertainment Industry'
)

# Update the layout
fig.update_layout(
    margin=dict(l=0, r=0, t=30, b=0)
)

# Save figure
file_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/90.png'
os.makedirs(os.path.dirname(file_path), exist_ok=True)
fig.write_image(file_path)

# Clear the current image state (Use this if you're using matplotlib, not necessary with plotly)
# plt.clf()
