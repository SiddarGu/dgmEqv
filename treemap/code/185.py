import plotly.express as px
import plotly.graph_objects as go
import os

# Data provided
data = {
    "Category": [
        "Accommodation",
        "Food and Beverage",
        "Travel Agencies",
        "Air Travel",
        "Cultural Activities",
        "Outdoor Activities",
        "Cruise Lines",
        "Travel Retail",
        "Tour Operators",
    ],
    "Percentage (%)": [25, 20, 15, 10, 10, 10, 5, 3, 2],
}

# Variables from data
data_labels = ["Percentage (%)"]
line_labels = data["Category"]
values = data["Percentage (%)"]

# Create the treemap
fig = px.treemap(
    data,
    path=[px.Constant("Tourism and Hospitality Industry"), 'Category'],
    values='Percentage (%)',
    title='Tourism and Hospitality Industry Breakdown by Service Category',
    color='Percentage (%)',  # Use Percentage for color scale
)

# Update the layout for a clearer and more intuitive image
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    treemapcolorway=["#D4E6F1", "#85C1E9", "#5DADE2", "#3498DB", "#2874A6"],
    font=dict(size=18)
)

# Update treemap to wrap text and adjust visual aspects
fig.update_traces(
    textinfo="label+value",
    textfont_size=16,
    marker=dict(line=dict(width=1, color='#FFFFFF')),
)

# Check if the directory exists, if not, create it
save_directory = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(save_directory, exist_ok=True)

# Save the image
fig.write_image(f"{save_directory}/185.png")

# Clear the current image state by closing the figure
fig.data = []
