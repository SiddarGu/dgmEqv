import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ['Usage Share (%)']
line_labels = [
    'Social Media', 'Online Shopping', 'Streaming Services',
    'Gaming', 'Online News', 'Cloud Services', 'Remote Work', 'E-Learning'
]
data = [25, 18, 17, 16, 9, 8, 4, 3]

# Transform into a format suitable for treemap
treemap_data = {
    'Internet Activity': line_labels,
    'Usage Share (%)': data
}

# Create treemap using plotly
fig = px.treemap(
    treemap_data,
    path=['Internet Activity'],  # defines the hierarchical levels
    values='Usage Share (%)',   # specifies the values used to dictate area
    title='Online Usage Distribution Across Internet Activities in 2023'
)

# Customize the figure to make it fancy
fig.update_traces(
    textinfo='label+percent entry',
    textfont_size=14,
    marker=dict(colors=px.colors.qualitative.Pastel, line=dict(color='#000000', width=1))
)

# Set the figure layout
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
)

# Define the path where to save
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)  # Ensure the directory exists
file_name = os.path.join(save_path, "1115.png")

# Save the figure
fig.write_image(file_name)

# Since Plotly doesn't maintain an internal state like matplotlib, we don't need to clear the state after saving.
# The figure is already saved as '1115.png' in the specified directory.
