import plotly.express as px
import os

# Given data string.
data_str = """Environmental Aspect,Percentage (%)
Renewable Energy,35
Waste Management,25
Water Conservation,15
Sustainable Agriculture,10
Green Building,5
Pollution Control,5
Biodiversity Conservation,5"""

# Convert the string data into lists for labels and values.
lines = data_str.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Create a DataFrame.
import pandas as pd
df = pd.DataFrame({
    'Environmental Aspect': line_labels,
    'Percentage (%)': data
})

# Draw the treemap.
fig = px.treemap(df,
                 path=['Environmental Aspect'],
                 values='Percentage (%)',
                 title='Proportions of Environment and Sustainability Initiatives')

# Update layout for better visualization.
fig.update_traces(textinfo='label+percent root', textfont=dict(size=16))
fig.update_layout(title_font_size=24)

# Create the directory for the output file if it does not exist.
output_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(output_dir, exist_ok=True)

# Save the figure.
fig.write_image(os.path.join(output_dir, '1013.png'))

# Clear the figure memory.
fig.data = []

