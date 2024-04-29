import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ['Crop Type', 'Harvest Yield (%)']
line_labels = ['Cereals', 'Vegetables', 'Fruits', 'Legumes', 'Nuts', 'Dairy', 'Poultry']
data = [35, 25, 20, 10, 5, 3, 2]

# Create a DataFrame for plotly
import pandas as pd
df = pd.DataFrame({
    'Crop Type': line_labels,
    'Harvest Yield (%)': data
})

# Create the treemap
fig = px.treemap(df, path=['Crop Type'], values='Harvest Yield (%)', 
                 title='Proportional Distribution of Harvest Yield in Agriculture')

# Add customizations if needed here. For the sake of example, let's add a color scheme
fig.update_traces(root_color="lightgrey")

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/145.png'
# Ensure the directory exists if not create it
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.write_image(save_path)

# Clear current figure state
fig.data = []
