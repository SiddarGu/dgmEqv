import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ['Percentage (%)']
line_labels = ['Environmental Legislation', 'Criminal Procedures', 'Business Regulations', 
               'Consumer Protection', 'Employment Law', 'Intellectual Property Rights', 
               'Immigration Law', 'Data Privacy', 'Maritime Law']
data = [18, 17, 20, 15, 10, 8, 5, 4, 3]

# Prepare the data for Plotly
df = {
    'Category': line_labels,
    'Percentage': data
}

# Create a treemap
fig = px.treemap(df, path=['Category'], values='Percentage',
                 title='Proportional Focus on Legal Affairs Categories within the Jurisprudence System')

# Update layout to make it fancy
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Update text labels to prevent overlapping
fig.update_traces(textinfo="label+percent entry", textfont_size=12)

# Ensure that directory path exists
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)

# Save the figure
fig.write_image(os.path.join(save_path, "50.png"))

# Clear the current figure state
fig.data = []
