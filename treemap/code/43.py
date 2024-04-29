import plotly.express as px
import plotly.graph_objects as go
import os

# Define data
data_labels = ['Education Fund Distribution (%)']
line_labels = ['STEM', 'Humanities', 'Social Sciences', 'Business', 'Law', 'Arts', 'Medicine', 'Education']
data = [25, 20, 15, 15, 8, 7, 5, 5]

# Create a structured dictionary from the data
structured_data = {
    'labels': line_labels,
    'values': data
}

# Create the treemap
fig = px.treemap(structured_data, path=['labels'], values='values', title='Allocation of Educational Funding by Academic Field')

# Customize the treemap
fig.update_traces(textinfo="label+value", textfont_size=20, marker=dict(colors=px.colors.qualitative.Pastel))

# Optionally, create directories if they don't exist
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)

# Save the figure
fig.write_image(f"{save_path}/43.png")

# Clear the current image state
fig.data = []
