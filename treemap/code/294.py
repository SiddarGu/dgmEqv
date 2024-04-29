import plotly.graph_objects as go
import os

# Data and associated labels
data_labels = ['Health Services', 'Education', 'Environmental Protection',
               'Human Rights', 'Arts and Culture', 'Disaster Relief',
               'Animal Welfare', 'International Aid']
data = [25, 20, 15, 13, 10, 9, 5, 3]
line_labels = ['Fundraising Efficiency (%)']  # assuming this is the parent label

# Initialize figure
fig = go.Figure()

# Build treemap
fig.add_trace(go.Treemap(
    labels=data_labels,
    parents=[""] * len(data_labels),
    values=data,
    textinfo='label+value+percent parent',
    outsidetextfont={"size": 20, "color": "#377eb8"},
    marker=dict(colors=px.colors.qualitative.Pastel, line=dict(width=2)),
    pathbar={"visible": False},
))

# Set the layout and title
fig.update_layout(
    title='Fundraising Efficiency Across Nonprofit Sectors',
    margin=dict(t=50, l=25, r=25, b=25)
)

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1044.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.write_image(save_path)

# Clear the current image state (not necessary with plotly as it does not maintain state)
