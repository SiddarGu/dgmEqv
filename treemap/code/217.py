import plotly.express as px
import plotly.graph_objects as go
import os

# Data from the task description
data_labels = ["Research Funding (%)"]
line_labels = ["Mathematics", "Physics", "Biology", "Chemistry", "Engineering", 
               "Environmental Science", "Biotechnology", "Computer Science", "Astronomy"]
data = [15, 20, 20, 15, 10, 7, 5, 5, 3]

# Transform the numerical data and label into a suitable dictionary for Plotly's treemap
treemap_data = {
    'labels': line_labels,
    'values': data
}

# Create the treemap figure
fig = px.treemap(treemap_data,
                 path=['labels'],
                 values='values',
                 title='Allocation of Research Funding Across Science and Engineering Disciplines')

# Optional: Update the layout to make it fancier (e.g., colors, corners, patterns)
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Create the output directory if it doesn't exist
output_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the figure
fig.write_image(f"{output_dir}/1130.png", scale=2)

# Clear the figure (when using Matplotlib, otherwise not necessary with Plotly)
# plt.clf(), plt.close() if using matplotlib

# Note: Plotly's treemap automatically handles text wrap and rotation to ensure text is readable.
