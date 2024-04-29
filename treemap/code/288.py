import plotly.express as px
import os

# Transform the data into variables
data_labels = ['Freight Volume (%)']
line_labels = ['Road', 'Rail', 'Air', 'Maritime', 'Pipeline', 'Intermodal']
data = [40, 25, 15, 10, 5, 5]

fig = px.treemap(
    names=line_labels,
    values=data,
    title='Freight Volume Distribution across Transport Modes',
    path=[line_labels],
)

# Style adjustments to ensure clear text display
fig.update_traces(textinfo="label+percent entry", textfont_size=18)
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Define the path for saving the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1038.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Clear the current image state (Plotly figures do not retain state like matplotlib)
# So this step is not necessary for Plotly
