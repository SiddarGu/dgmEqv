import plotly.express as px
import os

# Data
data_labels = ['Resource Allocation (%)']
line_labels = ['Renewable Energy', 'Conservation Efforts', 'Pollution Control', 'Sustainable Agriculture', 'Waste Management']
data = [30, 25, 20, 15, 10]

# Transform data into a format suitable for the treemap
df = {'Categories': line_labels, 'Resource Allocation (%)': data}

# Create the treemap
fig = px.treemap(df, path=['Categories'], values='Resource Allocation (%)',
                 title='Allocation of Sustainability Resources towards Environmental Initiatives')

# Apply some customizations for a fancier look
fig.update_traces(textinfo='label+value', textfont_size=18, marker=dict(line=dict(width=2), colorscale='greens'))

# Set up the saving directory
save_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
# Check if the save directory exists, and if not, create it
os.makedirs(save_dir, exist_ok=True)
save_path = os.path.join(save_dir, "72.png")

# Save the figure
fig.write_image(save_path)

# Clear the figure to reset state
fig.data = []
