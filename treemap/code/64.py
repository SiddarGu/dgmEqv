import plotly.graph_objects as go
import os
import plotly.express as px

# Parse the given data into lists
data_labels = ["Education Level", "Allocation (%)"]
line_labels = ["Preschool", "Primary Education", "Secondary Education", 
               "Tertiary Education", "Vocational Training", "Adult Education", 
               "Research and Development"]
data = [10, 20, 25, 20, 10, 5, 10]

# Combine the line labels and data into a single list of dictionaries
# for easier use with Plotly
data_dict = [{"label": label, "value": value} for label, value in zip(line_labels, data)]

# Create treemap using Plotly
fig = go.Figure(go.Treemap(
    labels=[item['label'] for item in data_dict],
    values=[item['value'] for item in data_dict],
    parents=[""] * len(data_dict),
    textinfo="label+percent root",
    marker=dict(colors=px.colors.qualitative.Plotly, line=dict(width=1.5)),
))

# Update layout to refine the look of the treemap
fig.update_layout(
    title='Percentage Distribution of Academic Funds Across Educational Levels',
    margin=dict(t=50, l=25, r=25, b=25)
)

# Define the absolute path for saving the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/'
# Create directories if they do not exist
os.makedirs(save_path, exist_ok=True)
# File path for saving the image
file_path = os.path.join(save_path, '64.png')

# Save the treemap to the file path as a PNG image
fig.write_image(file_path)

# Clear the current image state (not required for Plotly)
