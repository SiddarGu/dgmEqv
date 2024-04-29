import plotly.express as px
import os

# Given data
data_labels = ['Legal Branch', 'Percentage (%)']
line_labels = ['Constitutional Law', 'Criminal Law', 'Contract Law', 
               'Tort Law', 'Property Law', 'Family Law', 
               'Employment Law', 'Environmental Law', 'Immigration Law']
data = [18, 17, 16, 14, 12, 10, 8, 3, 2]

# Creating a DataFrame for Plotly
import pandas as pd
df = pd.DataFrame({
    data_labels[0]: line_labels,
    data_labels[1]: data
})

# Create the treemap
fig = px.treemap(df, path=[data_labels[0]], values=data_labels[1],
                 title='Proportional Focus Within Legal Affairs Sectors')

# Optionally add layout customizations
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

# Define the image save path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)
file_name = '142.png'
full_save_path = os.path.join(save_path, file_name)

# Save the figure
fig.write_image(full_save_path)

# To clear the current image state if needed (not required for plotly directly)
# If you were using matplotlib: plt.clf()
