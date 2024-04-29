import os
import plotly.express as px

# Define the data
data_labels = ["Percentage of Workload (%)"]
line_labels = ["Litigation", "Contracts", "Compliance", "Intellectual Property", "Employment", "Real Estate", "Immigration", "Environmental"]
data = [25, 20, 18, 14, 12, 6, 3, 2]

# Transform the data into the format suitable for treemap
df = {
    'Department': line_labels,
    'Percentage of Workload': data
}

# Create a treemap
fig = px.treemap(
    df,
    path=['Department'],  # Define hierarchy
    values='Percentage of Workload',
    title='Workload Distribution among Legal Departments',
    color='Percentage of Workload',
    color_continuous_scale='RdBu'
)

# Customize the layout to make it look fancy
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    treemapcolorway=["#2077b4", "#aec7e8", "#ffbb78", "#2ca02c", "#98df8a", "#d62728", "#ff9896", "#9467bd"],
    font=dict(size=18, color='black'),
    coloraxis_colorbar=dict(title="Workload %"),
)

# Set the path where the image will be saved
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1033.png'
# Create the directories if not exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Show the figure if needed (we don't need to show it since we're saving it)
#fig.show()
