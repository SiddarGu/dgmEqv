import plotly.express as px
import plotly.graph_objects as go

# Given data
data_str = """Transportation Mode,Logistics Share (%)
Road,40
Rail,20
Sea,15
Air,15
Pipeline,5
Intermodal,5"""

# Parsing the data into variables
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]  # ['Logistics Share (%)']
line_labels = [line.split(',')[0] for line in lines[1:]]  # ['Road', 'Rail', 'Sea', 'Air', 'Pipeline', 'Intermodal']
data = [float(line.split(',')[1]) for line in lines[1:]]  # [40, 20, 15, 15, 5, 5]

# Combine the label and data to create a DataFrame suitable for a treemap
import pandas as pd
df = pd.DataFrame({'Transportation Mode': line_labels, 'Logistics Share (%)': data})

# Create the treemap
fig = px.treemap(df, path=['Transportation Mode'], values='Logistics Share (%)',
                 title='Market Share Distribution in Transportation and Logistics Sector')

# Update layout for readability
fig.update_layout(treemapcolorway=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3"],
                  margin=dict(t=20, l=20, r=20, b=20))

# Save the figure
filepath = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/109.png'
fig.write_image(filepath)

# Clear the current figure state
fig.data = []

# Please note that the actual file system and directory structure may differ.
# The above path is used as per the instructions. Please make sure that the
# /cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/ directory exists and is writable.
