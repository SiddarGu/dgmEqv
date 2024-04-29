import plotly.graph_objects as go
import os

# Given data
data_labels = ['Natural Gas', 'Coal', 'Nuclear', 'Renewables', 'Petroleum', 'Hydroelectric']
data = [28, 21, 19, 17, 10, 5]
line_labels = ['Usage (%)'] * len(data)

# Create a figure with go.Treemap
fig = go.Figure(go.Treemap(
    labels=data_labels,
    parents=[""] * len(data_labels),
    values=data,
    textinfo="label+value+percent parent",
    outsidetextfont={"size": 20, "color": "#377eb8"},
    marker_colors=["#FFD700", "#C0C0C0", "#FF8C00", "#32CD32", "#8B0000", "#0000FF"],
    pathbar={"visible": False},
    ))

# Update layout for a fancy treemap
fig.update_layout(
    title_text='Energy Usage Breakdown by Source in the Utilities Sector',
    title_x=0.5,
    title_font_size=24
)

# Save the figure
output_directory = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
output_filename = "237.png"
output_path = os.path.join(output_directory, output_filename)

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

fig.write_image(output_path)

# Clear the current image state (Not needed for plotly)
# fig.clf()

print(f"Treemap saved as {output_path}")
