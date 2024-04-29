import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ["Market Share (%)"]
line_labels = ["Single-Family Home", "Condominium", "Townhouse", "Multi-family Housing", "Manufactured Home", "Co-op", "Vacation Home"]
data = [35, 25, 15, 10, 5, 5, 5]

# Transforming data for Plotly treemap
data_for_treemap = {
    'type': line_labels,
    'share': data
}

# Create the Treemap
fig = px.treemap(data_for_treemap, path=['type'], values='share', title='Market Share Distribution Among Property Types in the Housing Market')

# Customizing the treemap for aesthetics
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Define the save path (Note: Please ensure the directory structure exists or create it before saving the file)
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/144.png"

# Create directories if they don't exist
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Clear the figure
fig.data = []
