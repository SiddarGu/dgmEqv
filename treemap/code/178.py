import plotly.express as px
import os

# Prepare data from the provided snippet
data_labels = ["Percentage (%)"]
line_labels = ["Renewable Energy", "Waste Management", "Water Conservation", "Sustainable Agriculture", "Green Building", "Biodiversity Conservation"]
data = [35, 25, 15, 10, 8, 7]

# Combine line labels and data
data_dict = {"Sustainability Topic": line_labels, "Percentage": data}

# Create a DataFrame
df = pd.DataFrame(data_dict)

# Generate a treemap using plotly
fig = px.treemap(df, path=['Sustainability Topic'], values='Percentage',
                 title='Allocation of Sustainability Efforts in Environment Conservation')

fig.update_traces(textinfo="label+percent entry")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Create directories if they do not exist
output_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(output_dir, exist_ok=True)

# Save the figure
file_path = os.path.join(output_dir, "1015.png")
fig.write_image(file_path)

# Clear the current figure state - no need to clear state in plotly, as it doesn't maintain state like matplotlib

# Check for path correctness (Just ensuring the path is exactly as required)
assert file_path == "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1015.png"
