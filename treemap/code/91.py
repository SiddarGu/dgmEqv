import plotly.express as px
import plotly.graph_objects as go
import os

# Provided data
data = {
    "Educational Level": [
        "Primary Education", "Secondary Education", "Undergraduate", "Postgraduate",
        "Professional Development", "STEM Fields", "Humanities", "Arts"
    ],
    "Research Funding (%)": [10, 20, 25, 20, 15, 5, 3, 2]
}

# Transform data into variables
data_labels = list(data.keys())[1:]  # ['Research Funding (%)']
line_labels = data['Educational Level']
values = data['Research Funding (%)']

# Create the figure
fig = px.treemap(
    names=line_labels,
    parents=[""] * len(line_labels),
    values=values,
    title='Research Funding Distribution Across Educational Levels and Fields'
)

# Set figure properties, such as making sure the text fits well
fig.update_traces(
    textinfo="label+value+percent root",
    textfont=dict(size=16),
    marker=dict(colors=px.colors.qualitative.Plotly, line=dict(width=2))
)

# Make the treemap fancy
fig.update_layout(
    margin=dict(l=10, r=10, t=30, b=10),
    treemapcolorway=px.colors.qualitative.Pastel2
)

# Create directory if it does not exist
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)

# Save the figure
fig.write_image(f"{save_path}/91.png")

# To clear the current image state if you were using matplotlib, you would use plt.clf()
# However for plotly, the fig object finished its work after saving the image.
# And when you create a new fig, it will be a new state. So it's not necessary here.
