import plotly.express as px
import os

# Data
data = """
Accommodation Type,Revenue Share (%)
Hotels,40
Resorts,20
Vacation Rentals,15
Hostels,10
Bed & Breakfasts,8
Motels,7
"""

# Transforming data into separate variables
lines = data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = []
values = []

for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])
    values.append({data_labels[0]: float(parts[1])})

# Creating DataFrame
import pandas as pd
df = pd.DataFrame(values, index=line_labels)

# Plotting treemap
fig = px.treemap(df,
                 path=[px.Constant('Accommodation Type'), df.index],
                 values=data_labels[0],
                 title='Revenue Distribution in the Tourism and Hospitality Industry by Accommodation Type')

# Configuring the figure to deal with possibly long text strings in labels
fig.update_traces(textinfo="label+value+percent parent")
fig.update_layout(uniformtext=dict(minsize=10, mode='hide'))

# Create output directory if not exist
output_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_path = os.path.join(output_dir, "1037.png")

# Save the figure as a png file
fig.write_image(output_path)

# Show the figure (optional, for testing purposes)
fig.show()   # Comment this out if you don't want to display the figure
