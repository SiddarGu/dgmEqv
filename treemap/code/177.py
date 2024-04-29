import plotly.express as px
import os

# Given data
data_str = """Environmental Aspect,Contribution (%)
Greenhouse Gas Emissions,30
Renewable Energy Use,25
Waste Reduction,15
Water Conservation,10
Sustainable Agriculture,10
Biodiversity Preservation,5
Eco-Friendly Transportation,5"""

# Transform the data into three variables
lines = data_str.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [list(map(float, line.split(',')[1:])) for line in lines[1:]]

# Prepare data for the treemap
treemap_data = []
for label, value in zip(line_labels, data):
    treemap_data.append({'labels': label, 'values': value[0]})

# Create a DataFrame for the treemap
import pandas as pd
df = pd.DataFrame(treemap_data)

# Create the treemap
fig = px.treemap(df, path=['labels'], values='values', 
                 title='Global Environmental and Sustainability Efforts: A 2023 View')

# Customize the appearance of the treemap
fig.update_traces(textinfo="label+value", textfont_size=16)
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Create directories if they don't exist
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Save the figure
fig.write_image(os.path.join(save_path, "1014.png"))

# Clear the current image state
fig.data = []
