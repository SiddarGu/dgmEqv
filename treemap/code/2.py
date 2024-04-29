import plotly.express as px
import plotly.graph_objects as go

# Split the data string into lines and then into labels and values
raw_data = """Mobile Computing,25
Cloud Services,20
E-Commerce,15
Social Media,15
Cybersecurity,10
Artificial Intelligence,7
Internet Infrastructure,5
Virtual Reality,3"""

# Splitting the raw data into lines
lines = raw_data.split('\n')

# Extracting the labels and data
data_labels = ["Technology Sector", "Internet Usage (%)"]
line_labels = [line.split(',')[0] for line in lines]
data = [float(line.split(',')[1]) for line in lines]

# Now, let's visualize the data as a treemap using plotly
fig = px.treemap(
    names=line_labels,
    parents=[""] * len(data),  # As this is the first level of the treemap, parents are root, hence empty strings
    values=data,
    title='Global Internet Usage Distribution by Technology Sector'
)

# Customize the layout of the treemap if needed
fig.update_traces(
    textinfo="label+value",
    texttemplate="<b>%{label}:</b> %{value}%"
)

# Save the figure
fig.write_image("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/2.png")

# Clear the current image state, which is done automatically when using plotly
