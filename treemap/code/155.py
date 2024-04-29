import os
import plotly.express as px

# Given data separated into three variables
data_labels = ['Energy Source', 'Usage (%)']
line_labels = ['Renewable', 'Natural Gas', 'Coal', 'Nuclear', 'Oil', 'Hydroelectric', 'Biomass', 'Wind']
data = [25, 22, 18, 15, 12, 5, 2, 1]

# Prepare the data for plotting
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Draw the treemap
fig = px.treemap(df, path=['Energy Source'], values='Usage (%)',
                 title='Energy Mix: Utilization Percentage by Source in 2023')

# Add customizations here if necessary. For example, change colors, add patterns, etc.

# Make sure the labels are readable and not overlapping
fig.update_traces(textinfo='label+percent entry')

# Save the fig in the given path, with the proper directories
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1010.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure the directory exists
fig.write_image(save_path)

# Clear the current image state
fig.data = []

