import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ['Environmental Aspect', 'Percentage (%)']
line_labels = ['Renewable Energy Usage', 'Waste Management & Recycling', 'Greenhouse Gas Emissions', 
               'Water Conservation', 'Sustainable Agriculture', 'Biodiversity Conservation', 'Pollution Control']
data = [25, 20, 15, 15, 10, 10, 5]

# Convert the data into a format suitable for creating a treemap
df = {
    data_labels[0]: line_labels,
    data_labels[1]: data
}

# Create a DataFrame
df = pd.DataFrame(df)

# Create a treemap
fig = px.treemap(df,
                 path=[px.Constant('Environmental and Sustainability Efforts'), data_labels[0]],
                 values=data_labels[1],
                 title="Proportions of Environmental and Sustainability Efforts")

# Update treemap appearance
fig.update_traces(textinfo='label+value', textfont_size=14, selector=dict(type='treemap'))
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/170.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.write_image(save_path)

# To clear the current image state, although in Plotly there is no need to clear it as in matplotlib
fig = None
