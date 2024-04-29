import plotly.express as px
import plotly.graph_objects as go
import os

# Given data in a multiline string
raw_data = """Product Category,Online Sales (%)
Electronics,30
Clothing,25
Home & Garden,15
Health & Beauty,10
Books & Media,8
Toys & Games,7
Grocery,3
Jewelry,2"""

# Parsing and transforming the data into the desired format
lines = raw_data.split('\n')
# Extract labels for columns and rows
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
# Extract data
data = [float(line.split(',')[1]) for line in lines[1:]]

# Prepare the hierarchy for the treemap
parents = [''] * len(line_labels)  # No parent: top hierarchy

# Plotting the treemap
fig = px.treemap(
    names=line_labels,
    parents=parents,
    values=data,
    title='E-commerce Sales Distribution by Product Category',
    custom_data=[data_labels * len(data)]
)

# Update layout for fancy visual tweaks
fig.update_traces(
    texttemplate='%{label}<br>%{value}%',
    textinfo='label+value',
    hovertemplate='<b>%{label}</b><br>%{customdata[0]}: %{value}%',
    marker=dict(
        colors=data,
        colorscale='Blues',
        line=dict(width=2, color='rgb(255, 255, 255)'),
    ),
    textfont=dict(
        # Adjust font size if necessary
        size=18,
    )
)
fig.update_layout(
    autosize=True,
    margin=dict(t=50, l=25, r=25, b=25),
)

# Ensure the directories exist
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)
# Save the figure
fig.write_image(os.path.join(save_path, "1011.png"))

# Clear the figure
fig.data = []
