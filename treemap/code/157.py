import os
import plotly.express as px

# Given data preparation
data_labels = ['Revenue Percentage (%)']
line_labels = ['Professional Sports', 'Cinema', 'Music Industry', 'Television', 'Video Games',
               'Theater', 'Books and Magazines', 'Amusement Parks', 'Concerts and Festivals', 'Art Exhibitions']
data = [25, 17, 15, 13, 10, 7, 5, 4, 3, 1]

# Creating a dictionary for the treemap
data_dict = {'Categories': line_labels, 'Revenue Percentage': data}

# Create the treemap using Plotly
fig = px.treemap(
    data_dict,
    path=['Categories'],
    values='Revenue Percentage',
    title='Revenue Distribution in Sports and Entertainment Industries',
)

# Update layout to ensure all text fits and doesn't overlap
fig.update_traces(textinfo='label+value')
fig.update_layout(treemapcolorway=['pink', 'lightblue', 'orange', 'green', 'purple', 'red', 'blue', 'yellow', 'grey', 'brown'],
                  margin=dict(l=10, r=10, t=30, b=10))

# Create required directories if not exist
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)

# Save the figure
fig.write_image(os.path.join(save_path, "157.png"))

# End of script (No need to clear the current image state as plotly doesn't have a persistent state like matplotlib)
