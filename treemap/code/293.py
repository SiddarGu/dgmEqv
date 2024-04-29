import plotly.express as px
import os

# Given data string
data_str = """Subject Area,Research Funding (%)
STEM,35
Humanities,15
Social Sciences,20
Medical Sciences,25
Arts,5"""

# Split data string by lines and then by comma
lines = data_str.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Create a DataFrame
import pandas as pd
df = pd.DataFrame({
    'Subject Area': line_labels,
    'Research Funding (%)': data
})

# Create the treemap using plotly.express
fig = px.treemap(df, path=['Subject Area'], values='Research Funding (%)',
                 title='Allocation of Research Funding by Academic Subject Area')

# Customize the treemap
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Define the path to save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1043.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the image
fig.write_image(save_path)

# Clear the current image state (not necessary when using plotly.express as it does not keep state)
del fig
