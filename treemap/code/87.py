import plotly.express as px
import os

# Given data
data_labels = ['Market Share (%)']
line_labels = ['Banking', 'Investment', 'Insurance', 'Real Estate', 'Consumer Finance', 'Fintech', 'Asset Management', 'Venture Capital', 'Cryptocurrency']
data = [22, 18, 14, 15, 9, 8, 7, 5, 2]

# Construct the dataframe
df = {'Category': line_labels, 'Market Share (%)': data}

# Creating a treemap
fig = px.treemap(df, path=['Category'], values='Market Share (%)', title='Market Share Distribution in the Business and Finance Sector')

# Update layout for clarity
fig.update_layout(treemapcolorway=["#3B7A57", "#F0E68C", "#556B2F", "#8FBC8F", "#CDDC39", "#FFA07A", "#20B2AA", "#87CEFA", "#778899"],
                  margin=dict(t=10, l=10, r=10, b=10))

# Create the directory if it doesn't exist
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Save the figure
fig.write_image(f"{save_dir}/87.png", format='png')

# Clear the figure to prevent reusing the same properties in any subsequent plots
fig.data = []
