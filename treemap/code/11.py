import plotly.express as px
import plotly.graph_objects as go
import os

# Given data, transformed into the specified variables

# Labels for each column except the first column
data_labels = ["Production Volume (%)"]

# Labels for each row except the first row (Crop Types)
line_labels = ["Cereals", "Vegetables", "Fruits", "Meat", "Dairy"]

# The numerical array representing the data
data = [30, 25, 20, 15, 10]

# Merge line labels and data for the treemap
treemap_data = [{
    'labels': line_labels,
    'parents': [""] * len(line_labels),
    'values': data
}]

# Create the treemap figure
fig = go.Figure(go.Treemap(
    labels = treemap_data[0]['labels'],
    parents = treemap_data[0]['parents'],
    values = treemap_data[0]['values'],
    textinfo = "label+value+percent parent",
))

# Update the layout with the title
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25),
                  title_text='Proportions of Food Production by Crop Type')

# Generate the complete absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/11.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Show the figure
fig.show()
