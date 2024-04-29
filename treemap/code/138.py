import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ["Market Share (%)"]
line_labels = ["Packaged Foods", "Beverages", "Fresh Produce", "Meat and Poultry", "Dairy Products"]
data = [30, 25, 20, 15, 10]

# Create a DataFrame for the data
import pandas as pd

# Assemble the data into a DataFrame, assuming the labels correspond to the given data
df = pd.DataFrame({
    'Category': line_labels,
    'Market Share (%)': data
})

# Set the absolute path for the output image
output_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(output_dir, exist_ok=True)  # Create directories if they don't exist
output_file = os.path.join(output_dir, '138.png')

# Create a treemap
fig = px.treemap(df, path=['Category'], values='Market Share (%)',
                 title='Market Share Distribution in the Food and Beverage Industry')

# Update layout if necessary to ensure the text does not overlap
fig.update_traces(textinfo='label+value', textfont_size=16)
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Save figure
fig.write_image(output_file)

# Clear the figure after plotting (this step is for environments like Jupyter notebooks)
# In script environments, this line is not needed, but I include it here for thoroughness
fig.data = None
