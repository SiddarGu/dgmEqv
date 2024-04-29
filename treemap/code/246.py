import plotly.express as px
import plotly.graph_objects as go

# Transforming the data
data_labels = ['Research Funding (%)']
line_labels = ['History', 'Linguistics', 'Literature', 'Philosophy', 'Arts and Culture', 'Anthropology', 'Archaeology', 'Sociology']
data = [18, 12, 16, 14, 14, 11, 9, 6]

# Now, let's visualize the data as a treemap using plotly
df = {
    'values': data,
    'labels': line_labels
}

fig = px.treemap(
    df,
    names=line_labels,
    values=data,
    path=['labels'],
    title='Research Funding Distribution Across Humanities Disciplines'
)

# Additional styling
fig.update_traces(
    textinfo='label+value',
    hoverinfo='label+value',
    textfont=dict(size=18)
)

# Save the figure
fig.write_image('/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/246.png')

# Clear the current image state (there is no persistent state in Plotly that needs clearing)
