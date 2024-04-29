import plotly.express as px
import os

# Prepare the data
data_str = "Art Movement,Popularity (%)\nRenaissance,22\nImpressionism,18\nModernism,16\nBaroque,12\nCubism,10\nSurrealism,8\nPop Art,7\nAbstract,5\nRomanticism,2"
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [[float(line.split(',')[1])] for line in data_lines[1:]]

# Ensure that the directory path exists
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(save_path, exist_ok=True)

# Create the treemap
fig = px.treemap(
    names=line_labels,
    parents=[""] * len(line_labels),
    values=[d[0] for d in data],
    title='Popularity of Art Movements in the Realm of Arts and Culture'
)

# Set the layout configuration if required
fig.update_layout(
    margin=dict(l=10, r=10, b=10, t=30)
)

# Save the figure
fig.write_image(f"{save_path}/245.png")

# Clear the current image state
fig.data = []
