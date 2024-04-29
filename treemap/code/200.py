import plotly.express as px
import plotly.graph_objects as go
import os

# Data organization
data_labels = ['Usage (%)']
line_labels = ['Social Networking', 'Video Sharing', 'Online Shopping', 'Blogging', 
               'News Portals', 'Search Engines', 'Online Education', 'Gaming', 'Other']
data = [30, 25, 15, 10, 7, 5, 4, 2, 2]

# Combining labels and data for treemap
combined_data = {
    'Platform Category': line_labels + ["Total"],
    'Usage (%)': data + [sum(data)],
    'parent': [""] * len(line_labels) + ["Platform Category"]
}

# Create treemap
fig = px.treemap(combined_data, 
                 path=['parent', 'Platform Category'], 
                 values='Usage (%)',
                 title='Web Usage Breakdown Across Different Social Media and Internet Platforms')

# Customizing the treemap
fig.data[0].textinfo = 'label+percent entry'
fig.update_traces(textfont_size=18, selector=dict(type='treemap'))

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/200.png'
if not os.path.exists(os.path.dirname(save_path)):
    os.makedirs(os.path.dirname(save_path)) # Ensure the directory exists

fig.write_image(save_path)

# Clear the current figure state if necessary (Plotly does not maintain state like matplotlib)
# No additional code is needed to clear state for Plotly.
