import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ["R&D Investment (%)"]
line_labels = ["Artificial Intelligence", "Biotechnology", "Materials Science", "Renewable Energy", 
               "Aerospace", "Robotics", "Chemical Engineering", "Environmental Science"]
data = [17, 16, 15, 14, 13, 10, 8, 7]

# Transform data to the format required for treemaps in plotly
fig_data = {
    "labels": line_labels,
    "parents": [""] * len(data),
    "values": data
}

# Plotly Treemap
fig = go.Figure(go.Treemap(
    labels = fig_data["labels"],
    parents = fig_data["parents"],
    values = fig_data["values"],
    textinfo = "label+value+percent parent",
    marker=dict(colors=px.colors.sequential.RdBu),
    pathbar_textfont_size=20,
    outsidetextfont=dict(size=20, color="#377eb8"),
))

fig.update_layout(
    title='Proportion of R&D Investment Across Science and Engineering Fields',
    margin = dict(t=50, l=25, r=25, b=25)
)

# Creating the directories if they don't exist
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_dir, exist_ok=True)

# Save figure
fig.write_image(f"{save_dir}/1041.png")

# Clear the figure
fig.data = []
