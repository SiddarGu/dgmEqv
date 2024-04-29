import plotly.express as px
import plotly.graph_objects as go
import os

# Preprocessing the data
data_str = "Art Form,Engagement Hours (%)\n Painting,25\n Sculpture,20\n Theater,15\n Dance,13\n Music,12\n Literature,10\n Cinema,3\n Photography,2"
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')
data = []
line_labels = []

for line in data_lines[1:]:
    split_line = line.split(',')
    line_labels.append(split_line[0].strip())
    data.append(float(split_line[1].strip()))

# Create a DataFrame
df = {
    data_labels[0]: line_labels,
    data_labels[1]: data
}

# Create treemap
fig = px.treemap(df, path=[data_labels[0]], values=data_labels[1],
                 title='Public Engagement in Arts and Culture by Art Form')

# Customizing the treemap to be as fancy as possible
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Define the save path
directory = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
file_name = "1034.png"
save_path = os.path.join(directory, file_name)

# Make sure the directory exists before saving
os.makedirs(directory, exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Clear the current image state (only applicable if using matplotlib, here we show it for reference)
#plt.clf()
