import plotly.express as px
import os

# given data for labels and percentages
data_labels = ['Social Media', 'Search Engines', 'Online Shopping', 'Streaming Services', 
               'Online Gaming', 'Email Communications', 'Cloud Services', 'Cybersecurity', 'Internet of Things']
data_values = [25, 20, 15, 15, 10, 5, 5, 3, 2]

# create the treemap
fig = px.treemap(
    names=data_labels,
    parents=[""]*len(data_labels),
    values=data_values,
    title='Internet Usage Distribution Across Digital Services'
)

# make the treemap fancier
fig.update_traces(textinfo="label+value", textfont_size=20)
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# create the path where the image will be saved
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# save the treemap
fig.write_image(save_path + '1112.png')

# Clear the current image state by closing the figure
fig.data = None
