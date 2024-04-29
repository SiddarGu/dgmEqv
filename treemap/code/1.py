import plotly.express as px
import plotly.graph_objects as go
import os

# Given data transformed into variables as instructed
data_labels = ['Category', 'Usage (%)']
line_labels = [
    'Social Networking',
    'Online Shopping',
    'News Portals',
    'Video Streaming',
    'Email Communication',
    'Educational Websites',
    'Forums',
    'Blogs'
]
data = [32, 20, 15, 13, 10, 5, 3, 2]

# Converting the data into a dictionary for visualization
data_dict = {
    'Category': line_labels + ['Total'],  # Add total for the treemap root
    'Usage (%)': data + [sum(data)]
}

# Create a treemap using plotly express
fig = px.treemap(
    data_dict,
    path=['Category'],
    values='Usage (%)',
    title='Internet Usage Distribution Across Web Services in 2023'
)

fig.update_traces(textinfo="label+value+percent parent")  # Show all text info

# Update layout for fancy appearance
fig.update_layout(
    treemapcolorway=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"],
)

# Define the absolute path for saving the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)  # Create directory if it doesn't exist

# Save the figure
fig.write_image(f"{save_path}/1.png")

# Clear the current image state by closing the figure
fig.data = []
