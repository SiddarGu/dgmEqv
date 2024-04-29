import plotly.express as px
import os

# Given data in the desired format
data_labels = ["Technology Segment", "Internet Usage (%)"]
line_labels = ["Social Media", "Search Engines", "Online Shopping", "Streaming Services", "Cloud Computing", "Online Gaming", "Educational Platforms"]
data = [25, 20, 15, 15, 10, 10, 5]

# Preparing the data for treemap
df = {
    data_labels[0]: line_labels,
    data_labels[1]: data
}

# Convert the data into a DataFrame
df = pd.DataFrame(df)

# Create a Treemap using Plotly
fig = px.treemap(df, path=[data_labels[0]], values=data_labels[1],
                 title='Global Internet Usage Distribution Across Technology Segments')

fig.update_traces(textinfo='label+percent entry')

# Adjust layout
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Create the directories if not exist
output_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the figure
fig.write_image(f"{output_dir}/169.png")

# Clear current figure state, if you are running in an interactive environment like Jupyter Notebooks
# In a script, this is not necessary.
#fig.clf()
