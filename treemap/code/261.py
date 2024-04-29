import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data = """
Hospitality Segment,Revenue Share (%)
Hotels,35
Restaurants,30
Travel Agencies,15
Tourism Attractions,10
Event Planning,5
Cruise Lines,5
"""

# Preprocessing the data into variables
lines = data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
values = [float(line.split(',')[1]) for line in lines[1:]]

# Create a treemap figure using plotly
fig = px.treemap(
    names=line_labels,
    parents=[""] * len(line_labels),
    values=values,
    title="Revenue Distribution Across Tourism and Hospitality Segments"
)
fig.update_traces(
    textinfo="label+percent parent",
    textfont_size=16,
    marker=dict(colors=px.colors.qualitative.Pastel)  # Custom color scheme
)

# Optionally, set the figure layout or trace properties to make it fancier
# Example: rounded corners for the treemap
fig.update_traces(marker=dict(line=dict(width=3)))

# Set the path where the image will be saved
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1011.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Create directory if it doesn't exist

# Save the figure
fig.write_image(save_path)

# Clear the current image state if necessary (here Plotly does not maintain the state)
# Example for matplotlib: plt.clf()
