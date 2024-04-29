import plotly.express as px
import os

# Given data
data = {
    "Category": ["Renewable Energy", "Recycling Initiatives", "Conservation Efforts", "Pollution Control", "Sustainable Agriculture"],
    "Percentage (%)": [30, 20, 25, 15, 10]
}

# Data labels and line labels (as per your description, line_labels does not apply here though)
data_labels = list(data.keys())
data_values = list(data.values())

# Prepare data for treemap
treemap_data = {data_labels[0]: data_values[0], data_labels[1]: data_values[1]}

# Draw the treemap
fig = px.treemap(
    treemap_data, 
    path=[data_labels[0]], 
    values=data_labels[1],
    title='Proportion of Sustainability Efforts in Environmental Conservation'
)

fig.update_traces(
    textinfo="label+percent entry", 
    textfont=dict(size=18),
    hoverinfo='label+percent entry'
)

fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25)
)

# Create directories if they don't exist
output_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(output_dir, exist_ok=True)

# Save figure
output_path = os.path.join(output_dir, "66.png")
fig.write_image(output_path)

# There's no current image state in plotly to clear, so we're done here.
